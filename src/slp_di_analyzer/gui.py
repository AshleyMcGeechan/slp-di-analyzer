import sys, math, os, re
import numpy as np
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsSimpleTextItem, QWidget, QComboBox
from PySide6.QtGui import QFont, QTransform
from PySide6.QtCore import QFile, QThread, QObject, Signal, Slot, QRunnable, QThreadPool, Qt, QTime
from ui_design import Ui_MainWindow
from peppi_py import read_slippi, read_peppi
from slp_di_characters import bowser, captain_falcon, donkey_kong, dr_mario, falco, fox, ganondorf, ice_climbers, jigglypuff, kirby, link, luigi, mario, marth, mewtwo, mr_game_and_watch, ness, peach, pichu, pikachu, roy, samus, sheik, yoshi, young_link, zelda
from file_handler import load_files
import pyqtgraph as pg
import pyqtgraph.exporters
from pathlib import Path
from qt_material import apply_stylesheet
from icon import icon

# Worker handles file loading and filtering for DI events
class Worker(QRunnable):
    def __init__(self, file, main_window):
        super().__init__()
        self.file = file
        self.main_window = main_window
        self.signals = Signals()
    
    @Slot()
    def run(self):
        result = []
        # Multiple early termination checks since a QRunnable can't be stopped once it starts
        if self.main_window.running:
            result.append(load_files(self.file))
        if self.main_window.running:
            flattened = [x for y in result for x in y]
        if self.main_window.running:
            self.signals.finished.emit(flattened)
        
class Signals(QObject):
    finished = Signal(list)
    

class MainWindow(QMainWindow):
    
    def selectFolder(self):
        self.load_file_dialog = QFileDialog()
        self.load_file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        try:
            if self.load_file_dialog.exec():
                self.load_dir = self.load_file_dialog.selectedFiles()[0]
            self.ui.lineEdit.setText(self.load_dir)
        finally:
            self.load_file_dialog = None
    
    # Toggle buttons to prevent use during file loading
    def toggle_all_buttons(self):
        self.buttons_enabled = not self.buttons_enabled
        self.ui.selectButton.setEnabled(self.buttons_enabled)
        self.ui.loadButton.setEnabled(self.buttons_enabled)
        self.ui.comboBox.setEnabled(self.buttons_enabled)
        self.ui.comboBox_2.setEnabled(self.buttons_enabled)
        self.ui.directionButton.setEnabled(self.buttons_enabled)
        self.ui.toggleAngles.setEnabled(self.buttons_enabled)
        self.ui.saveHeatmap.setEnabled(self.buttons_enabled)
        self.ui.rawButton.setEnabled(self.buttons_enabled)
        self.ui.percentButton.setEnabled(self.buttons_enabled)
        
    # Load files from given filepath and extract data using worker threads
    def loadFiles(self):
        filedata = []
        filepath = self.ui.lineEdit.text()
        p = Path(filepath)
        if len(filepath) > 0 and p.exists() and p.is_dir():
            files = p.rglob('*.slp')
            files = list(files)
            self.file_count = len(files)
            self.file_counter = 0
            self.results_list = []
            self.stats_array = np.array([])
            if self.file_count > 0:
                self.ui.messageBox.setText("Files loaded: 0/" + str(self.file_count))
                self.toggle_all_buttons()
                for file in files:
                    worker = Worker(file=file, main_window=self)
                    worker.signals.finished.connect(self.loadFilesCompleted)
                    self.pool.start(worker)
        # Error handling
            else:
                self.ui.messageBox.setText("No SLP files found.")
        else:
            self.ui.messageBox.setText("Directory not found.")

    # Each finished worker thread calls this function with the filtered data
    # On final thread completion re-enable buttons and clear thread pool
    def loadFilesCompleted(self, result):
        self.file_counter += 1
        self.ui.messageBox.setText("Files loaded: " + str(self.file_counter) + "/" + str(self.file_count))
        self.results_list.append(result)
        if self.file_counter >= self.file_count:
            flattened = [x for y in self.results_list for x in y]
            self.stats_array = np.array(flattened).reshape(-1, 2, 9)
            self.ui.messageBox.setText("All files loaded.")
            self.toggle_all_buttons()
            self.pool.clear()
            self.update_char_filter(0)
    

    # Creates a boolean mask on DI events where the attacking character ID matches that chosen by the user
    def update_char_filter(self, index):
        
        data = np.array([])
        self.char_masked_data = np.array([])
        self.move_masked_data = np.array([])
        self.percent_masked_data = np.array([])
        
        # SPECIAL CASE: DK has the cargo throws, 4 additional moves exclusive to him
        if self.ui.comboBox.currentIndex() == 2:
            self.ui.comboBox_2.addItems(["Cargo Forward", "Cargo Back", "Cargo Up", "Cargo Down"])
        else:
            while self.ui.comboBox_2.count() != 24:
                self.ui.comboBox_2.removeItem(24)
        
        
        if self.stats_array.size != 0:

            char_id = self.character_index[self.ui.comboBox.currentIndex()]
            
            # Check char ID equal to selected
            char_mask_0 = (self.stats_array[:, 0, 3] == str(float(char_id)))
            char_mask_1 = (self.stats_array[:, 1, 3] == str(float(char_id)))
            
            
            # SPECIAL CASE: Popo and Nana have internal game IDs 10 and 11 but will be considered as one character here
            if char_id == 10:
                char_mask_0 = np.logical_or(char_mask_0, self.stats_array[:, 0, 3] == '11.0')
                char_mask_1 = np.logical_or(char_mask_0, self.stats_array[:, 0, 3] == '11.0')
                
            # Check character is in a taking damage action state or a being thrown state
            action_state_mask_0_0 = np.logical_and(self.stats_array[:, 0, 4].astype(np.float32) >= 75, self.stats_array[:, 0, 4].astype(np.float32) <= 91)
            action_state_mask_0_1 = np.logical_and(self.stats_array[:, 0, 4].astype(np.float32) >= 239, self.stats_array[:, 0, 4].astype(np.float32) <= 243)
            action_state_mask_0 = np.logical_or(action_state_mask_0_0, action_state_mask_0_1)
            
            action_state_mask_1_0 = np.logical_and(self.stats_array[:, 1, 4].astype(np.float32) >= 75, self.stats_array[:, 1, 4].astype(np.float32) <= 91)
            action_state_mask_1_1 = np.logical_and(self.stats_array[:, 1, 4].astype(np.float32) >= 239, self.stats_array[:, 1, 4].astype(np.float32) <= 243)
            action_state_mask_1 = np.logical_or(action_state_mask_1_0, action_state_mask_1_1)
            
            # Check character is in last frame of hitstun
            # Covers some cases where characters exit hitstun on different frames
            hitstun_mask_0 = self.stats_array[:, 0, 8] == "1.0"
            hitstun_mask_1 = self.stats_array[:, 1, 8] == "1.0"
            
            # Check opponents character is selected, check player is in damaged state, check player is in last frame of hitstun
            total_mask_0 = np.logical_and(char_mask_1, action_state_mask_0)
            total_mask_0 = np.logical_and(total_mask_0, hitstun_mask_0)
            total_mask_1 = np.logical_and(char_mask_0, action_state_mask_1)
            total_mask_1 = np.logical_and(total_mask_1, hitstun_mask_1)
            
            # If condition is true get player's control stick coordinates and facing direction and last attack landed
            # (Characters face the direction they are attacked from)
            data_0_0 = self.stats_array[total_mask_0][:, 0, [0,1,2,5,6]]
            data_0_1 = self.stats_array[total_mask_0][:, 1, [7]]
            if data_0_0.size != 0:
                data = np.concatenate((data_0_0, data_0_1), axis=1)
                data = data.reshape((-1,6))
            
            data_1_0 = self.stats_array[total_mask_1][:, 1, [0,1,2,5,6]]
            data_1_1 = self.stats_array[total_mask_1][:, 0, [7]]
            if data_1_0.size != 0:
                data = np.concatenate((data_1_0, data_1_1), axis=1)
                data = data.reshape((-1,6))

            self.char_masked_data = data
        self.update_move_filter(0)
        
    # Creates a boolean mask on DI events where the last attack landed matches the chosen move ID
    # Also handles knockback direction
    def update_move_filter(self, index):
        self.move_masked_data = np.array([])
        self.percent_masked_data = np.array([])
        move_index = self.move_index[self.ui.comboBox_2.currentIndex()]
        
        if self.char_masked_data.size !=0:
            move_mask = self.char_masked_data[:, 5].astype(np.float32) == float(move_index)
            facing_mask = self.char_masked_data[:, 3].astype(np.float32) == self.facing_direction
            total_mask = np.logical_and(move_mask, facing_mask)
            self.move_masked_data = self.char_masked_data[total_mask][: ,[0,1,2,4]]
            
        self.percentage_filter()
        
    # Creates a boolean mask on DI events where the attacked character's percent is between the bounds set in the GUI
    # Connect code filter is done here so that it's checked regardless of which field is updated
    def percentage_filter(self):
        lower_bound = self.ui.lowerRange.value()
        upper_bound = self.ui.upperRange.value()
        self.percent_masked_data = np.array([])
        
        if self.move_masked_data.size != 0:
            
            # Check character is player based on connect code
            connect_code = re.sub(r'\W+', '', self.ui.lineEdit_2.text()).lower()
            connect_code_mask = (self.move_masked_data[:, 0] == connect_code)
            percent_mask = np.logical_and(self.move_masked_data[:, 3].astype(np.float32) >= lower_bound, self.move_masked_data[:, 3].astype(np.float32) <= upper_bound)
            self.percent_masked_data = self.move_masked_data[np.logical_and(percent_mask,connect_code_mask)][:, 1:3].astype(np.float32)
        
        self.update_graph()
        
    # Update the desired knockback direction
    def update_knockback_direction(self):
        self.facing_direction = -1.0 if self.facing_direction == 1.0 else 1.0
        self.update_move_filter(0)
        direction_string = "Right" if self.facing_direction == 1.0 else "Left"
        self.ui.messageBox.setText("Hit from the: " + direction_string + ".")
    
    # Toggles visibility of move knockback angles
    def toggle_display(self):
        self.display_toggle = not self.display_toggle
        self.raw_display_toggle = False
        self.update_graph()
        toggle_string = "Angle display enabled." if self.display_toggle else "Angle display disabled."
        self.ui.messageBox.setText(toggle_string)
        
    # Toggles visibility of raw DI event occurence numbers
    def toggle_raw_display(self):
        self.raw_display_toggle = not self.raw_display_toggle
        self.display_toggle = False
        self.update_graph()
        toggle_string = "Magnitude display enabled." if self.raw_display_toggle else "Magnitude display disabled."
        self.ui.messageBox.setText(toggle_string)
    
    # Export heatmap to png
    def save_graph(self):
        exporter = pg.exporters.ImageExporter(self.p)
        exporter.parameters()['width'] = 800
        direction_string = "Left" if self.facing_direction == 1.0 else "Right"
        filestring = ""+self.ui.lineEdit_2.text()+self.ui.comboBox.currentText()+self.ui.comboBox_2.currentText()+direction_string
        filestring = filestring.replace(" ", "")
        filestring = re.sub(r'[^\w]', '', filestring)
        self.save_file_dialog = QFileDialog()
        self.save_file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        self.save_file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        self.save_file_dialog.setNameFilter("Images (*.png)")
        self.save_file_dialog.setDefaultSuffix(".png")
        self.save_file_dialog.selectFile(filestring)
        try:
            if self.save_file_dialog.exec():
                filename = self.save_file_dialog.selectedFiles()[0]
                exporter.export(filename)
                self.ui.messageBox.setText(str(filename)+" saved.")
            else:
                self.ui.messageBox.setText("Save failed.")
        finally:
            self.save_file_dialog = None
        
    def calculatePoint(self, angle):
        return (100*math.cos(angle), 100*math.sin(angle))
    
    # Converts control stick coordinates to 2d histogram for heatmap display
    def create_histograms(self, masked_data):
        data = masked_data
        # Scale data from (-1,1) to (0, 200)
        data = data*100
        data = data+100
        data = np.rint(data)
        data = data.reshape((-1, 2))
        # Generate histogram
        bins = np.linspace(0, 200, num=202)
        bins2 = np.linspace(0, 200, num=22)
        binned, binx, biny = np.histogram2d(data[:, 0], data[:,1], bins=[bins, bins])
        binned2, binx, biny = np.histogram2d(data[:, 0], data[:,1], bins=[bins2, bins2])
        return(binned, binned2)
    
    # Draws the control stick circle
    def draw_base(self):
        self.p.clear()
        p_ellipse = QGraphicsEllipseItem(0, 0, 200, 200)  # x, y, width, height
        p_ellipse.setPen(pg.mkPen((0, 0, 0, 0)))
        p_ellipse.setBrush(pg.mkBrush((160,160,160)))
        self.p.addItem(p_ellipse)
                
    # Draws additional info like move names and knockback angles
    def draw_info(self, character_data):
        angles = character_data[self.ui.comboBox_2.currentText()]["angles"]
        labels = character_data[self.ui.comboBox_2.currentText()]["labels"]
        
        # Draw move name
        color = self.display_colors[0]
        text = pg.TextItem(self.ui.comboBox.currentText(), anchor=(0.5,0.5), color=color)
        text.setPos(20, 220)
        text.setFont(self.label_font)
        self.p.addItem(text)
        
        try:
            text = pg.TextItem(labels[0], anchor=(0.5,0.5), color=color)
            text.setPos(20, 210)
            text.setFont(self.label_font)
            self.p.addItem(text)
            
            # text = pg.opengl.GLTextItem(pos=(20,210), color=color, text=labels[0], font=self.label_font)
            # self.p.addItem(text)
            if self.display_toggle:
                # Draw knockback angle line
                for i, angle in enumerate(angles):
                    test_point_1 = self.calculatePoint(math.radians(angle))
                    color = self.display_colors[i]
                    p_line_1 = QGraphicsLineItem(100, 100, (test_point_1[0]*-self.facing_direction)+100, test_point_1[1]+100)
                    p_line_1.setPen(pg.mkPen(color, width = 5))
                    self.p.addItem(p_line_1)

                    # Draw additional labels
                    if len(labels) > 1:
                        text = pg.TextItem(labels[i+1], anchor=(0.5,0.5), color=color)
                        text.setPos(20, 210 - (10*(i+1)))
                        text.setFont(self.label_font)
                        self.p.addItem(text)
        except:
            self.ui.messageBox.setText("Error loading character properties.")
    
    # Draws the heatmap 
    def draw_data(self, graph_data):
     
        # https://stackoverflow.com/a/44874588
        def create_circular_mask(h, w, center=None, radius=None):
            if center is None: # use the middle of the image
                center = (int(w/2), int(h/2))
            if radius is None: # use the smallest distance between the center and image walls
                radius = min(center[0], center[1], w-center[0], h-center[1])

            Y, X = np.ogrid[:h, :w]
            dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

            mask = dist_from_center <= radius
            return mask
            
        data = graph_data
        data.reshape(201, 201, 1)
        # Filter data for visual clarity
        max = np.max(data)
        data = pg.gaussianFilter(data, (3))
        data_norm = (data-np.min(data))/(np.max(data)-np.min(data))

        cmap = pg.colormap.get("plasma").getSubset(0.0, 1.0)
        # Convert to format for rgba pixels
        data = np.dstack((data, np.zeros((201,201))))
        data = np.dstack((data, np.zeros((201,201))))
        data = np.dstack((data, np.full((201,201), 255)))
        # Color pixels based on magnitude according to CET-L3 colormap
        data[:, :, 0:3] = cmap.map(data_norm)[:, :, 0:3]
        mask = create_circular_mask(201, 201, (101, 101), 101)
        data[~mask, 3] = 0
        # Reduce transparency of low magnitude pixels for visual clarity
        if self.raw_display_toggle:
            threshold = 256
        else:
            threshold = 32
        mask = data[:, :, 0] <= threshold
        data[mask, 3] *= (data[mask, 0] / threshold)
        tr = QTransform()
        tr.translate(-1, -1)
        img = pg.ImageItem()
        img.setTransform(tr)
        img.setImage(data)
        self.p.addItem(img)
        
        # Color bar
        cbar = pg.GradientLegend((10, 300), (10, 100))
        cbar.setParentItem(img)
        cbar.setColorMap(cmap)
        cbar.setLabels({str(int(max)): 1, "0": 0})
        self.p.addItem(cbar)
        
    # Draws the magnitude of DI events in corresponding zones of the heatmap
    def draw_magnitudes(self, magnitude_data):
        for i in range(magnitude_data.shape[0]):
            for j in range(magnitude_data.shape[1]):
                color = "#000000"
                text = pg.TextItem(str(int(magnitude_data[i, j])), anchor=(0.5,0.5), color=color)
                text.setPos(i*10, j*10)
                text.setFont(self.mag_font)
                self.p.addItem(text)
    
    # Draws the heatmap and associated graph elements
    def update_graph(self):
        
        graph_data = np.array([])
        magnitude_data = np.array([])

        if self.percent_masked_data.size != 0:
            graph_data, magnitude_data = self.create_histograms(self.percent_masked_data)
        
        self.draw_base()
        
        character_data = self.character_display_info[self.ui.comboBox.currentIndex()]
        if self.ui.comboBox_2.currentText() in character_data:
            self.draw_info(character_data)
        
        if graph_data.size != 0:
            self.draw_data(graph_data)

        if self.raw_display_toggle and magnitude_data.size != 0:
            self.draw_magnitudes(magnitude_data)
    
    def __init__(self):
        super(MainWindow, self).__init__()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(icon)
        appIcon = QtGui.QIcon(pixmap)
        self.setWindowIcon(appIcon)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # UI function connections
        self.ui.selectButton.clicked.connect(self.selectFolder)
        self.ui.loadButton.clicked.connect(self.loadFiles)
        self.ui.comboBox.currentIndexChanged.connect(self.update_char_filter)
        self.ui.comboBox_2.currentIndexChanged.connect(self.update_move_filter)
        self.ui.directionButton.clicked.connect(self.update_knockback_direction)
        self.ui.toggleAngles.clicked.connect(self.toggle_display)
        self.ui.saveHeatmap.clicked.connect(self.save_graph)
        self.ui.rawButton.clicked.connect(self.toggle_raw_display)
        self.ui.percentButton.clicked.connect(self.percentage_filter)
        
        
        # Initializations
        self.buttons_enabled = True
        self.file_count = 0
        self.file_counter = 0
        self.facing_direction = -1.0
        self.results_list = []
        self.stats_array = np.array([])
        self.char_masked_data = np.array([])
        self.move_masked_data = np.array([])
        self.percent_masked_data = np.array([])
        self.load_file_dialog = None
        self.load_dir = ""
        self.save_file_dialog = None
        self.pool = QThreadPool.globalInstance()
        self.running = True

        
        
        # Converts character list from alphabetical to internal game ID order
        self.character_index = [5, 2, 3, 21, 22, 1, 25, 10, 15, 4, 6, 17, 0, 18, 16, 24, 8, 9, 23, 12, 26, 13, 7, 14, 20, 19]
        # Converts move list to internal game ID order
        self.move_index = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 53, 54, 55, 56, 57, 58, 59, 60]
        # Stores knockback angle data for character moves
        self.character_display_info = [bowser.display_info, captain_falcon.display_info, donkey_kong.display_info, dr_mario.display_info, falco.display_info, fox.display_info, 
                        ganondorf.display_info, ice_climbers.display_info, jigglypuff.display_info, kirby.display_info, link.display_info, luigi.display_info,
                        mario.display_info, marth.display_info, mewtwo.display_info, mr_game_and_watch.display_info, ness.display_info, peach.display_info, pichu.display_info, 
                        pikachu.display_info, roy.display_info, samus.display_info, sheik.display_info, yoshi.display_info, young_link.display_info, zelda.display_info]
                    

        # Heatmap setup
        self.label_font = QFont("Roboto", 16)
        self.mag_font = QFont("Roboto", 14)
        self.display_colors = ["#E93016", "#163ee9", "#e98316", "#9916E9", "#D32C8F", "#D3C42C"]
        self.display_toggle = False
        self.raw_display_toggle = False
        self.p = self.ui.graphWidget.addPlot(title='')
        self.update_graph()
        self.p.setMenuEnabled(False)
        self.p.setMouseEnabled(x=False, y=False)
        self.p.setRange(xRange=(-20, 220), yRange=(0, 230))
        self.p.showAxes(False, showValues = False)
        self.ui.graphWidget.setBackground('#cbbfd5')
        self.p.hideButtons()
        self.p.setAspectLocked(lock = True, ratio = 1)
        self.update_graph()

        

        
    def closeEvent(self, e):
        print("Exiting program.")
        self.running = False
        self.pool.clear()
        



    
