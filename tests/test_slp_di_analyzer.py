import sys, os, hashlib, shutil
import unittest
from PySide6.QtWidgets import QApplication
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt, QTimer, QDir
import src.slp_di_analyzer
from src.slp_di_analyzer import gui
import pytest
from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api
import numpy as np

@pytest.fixture
def main_window(qtbot):
    qApp = QApplication.instance()
    if qApp is None:
        app = QApplication([""])
    else:
        app = qApp
    widget = gui.MainWindow()
    qtbot.addWidget(widget)
    return widget
    
@pytest.fixture
def test_values():
    return np.loadtxt(os.path.abspath(os.path.dirname(__file__))+"/test_data/test_values.gz", dtype=str).reshape(-1, 2, 9)
    
@pytest.fixture
def default_heatmaps(): 
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/1.png', "rb") as f: screenshot1 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/2.png', "rb") as f: screenshot2 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/3.png', "rb") as f: screenshot3 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/4.png', "rb") as f: screenshot4 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/5.png', "rb") as f: screenshot5 = hashlib.sha256(f.read()).hexdigest()
    return (screenshot1, screenshot2, screenshot3, screenshot4, screenshot5)
    
@pytest.fixture
def active_heatmaps(): 
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/6.png', "rb") as f: screenshot1 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/7.png', "rb") as f: screenshot2 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/8.png', "rb") as f: screenshot3 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/9.png', "rb") as f: screenshot4 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/10.png', "rb") as f: screenshot5 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/11.png', "rb") as f: screenshot6 = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.abspath(os.path.dirname(__file__))+'/test_data/12.png', "rb") as f: screenshot7 = hashlib.sha256(f.read()).hexdigest()
    return (screenshot1, screenshot2, screenshot3, screenshot4, screenshot5, screenshot6, screenshot7)
    
def test_defaults(main_window, qtbot):
    assert main_window.ui.lineEdit.text() == ""
    assert main_window.ui.lineEdit_2.text() == ""
        
    assert main_window.ui.comboBox.currentIndex() == 0
    assert main_window.ui.comboBox.currentText() == "Bowser"
    
    assert main_window.ui.comboBox_2.currentIndex() == 0
    assert main_window.ui.comboBox_2.currentText() == "Jab 1"   
        
    assert main_window.ui.lowerRange.value() == 0
    assert main_window.ui.upperRange.value() == 999
    
    
def test_directory_selection(main_window, qtbot):
    path = QDir(os.path.abspath(os.path.dirname(__file__))+"/test_data")
    def handle_dialog():
        while main_window.load_file_dialog is None:
            qApp.processEvents()
        main_window.load_file_dialog.setDirectory(path)
        main_window.load_file_dialog.accept()

    QTimer.singleShot(100, handle_dialog)
    qtbot.mouseClick(main_window.ui.selectButton, Qt.LeftButton, delay=1)
    assert main_window.ui.lineEdit.text() != ""
    assert main_window.load_file_dialog is None


def test_loading_from_file(main_window, test_values, qtbot):
    main_window.ui.lineEdit.setText(os.path.abspath(os.path.dirname(__file__))+'/test_data')
    qtbot.mouseClick(main_window.ui.loadButton, Qt.LeftButton)
    qtbot.waitUntil(lambda: main_window.ui.messageBox.text() == "All files loaded.")
    assert main_window.stats_array.shape == test_values.shape
    assert np.all(main_window.stats_array[:,:,:] == test_values[:,:,:])
    
  
def test_filters(main_window, test_values, qtbot):
    main_window.ui.lineEdit_2.setText("swsh#195")
    main_window.stats_array = test_values
    main_window.ui.comboBox.setCurrentIndex(1)
    assert np.allclose(main_window.percent_masked_data, [[-0.9875,  0.0]])
    main_window.ui.comboBox_2.setCurrentIndex(15)
    assert np.allclose(main_window.percent_masked_data, [[0.0, 0.975],[-0.9875, 0.0],[0.8125, -0.575],[0.975,0.0]])
    qtbot.mouseClick(main_window.ui.directionButton, Qt.LeftButton)
    assert np.allclose(main_window.percent_masked_data, [[ 0.625, -0.775]])
    qtbot.mouseClick(main_window.ui.directionButton, Qt.LeftButton)
    main_window.ui.upperRange.setValue(50)
    qtbot.mouseClick(main_window.ui.percentButton, Qt.LeftButton)
    assert np.allclose(main_window.percent_masked_data, [[0.0, 0.975],[-0.9875, 0.0]])
    main_window.ui.lowerRange.setValue(20)
    qtbot.mouseClick(main_window.ui.percentButton, Qt.LeftButton)
    assert np.allclose(main_window.percent_masked_data, [[0.0, 0.975]])

# Screenshot tests are independent of stylesheet but may be dependent on platform
def test_default_heatmap(main_window, default_heatmaps, qtbot):
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert default_heatmaps[0] == screenshot
    
    main_window.ui.comboBox.setCurrentIndex(1)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert default_heatmaps[1] == screenshot
    
    main_window.ui.comboBox_2.setCurrentIndex(15)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert default_heatmaps[2] == screenshot
    
    qtbot.mouseClick(main_window.ui.toggleAngles, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert default_heatmaps[3] == screenshot
    
    qtbot.mouseClick(main_window.ui.directionButton, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert default_heatmaps[4] == screenshot
    
def test_active_heatmap(main_window, test_values, active_heatmaps, qtbot):
    main_window.ui.lineEdit_2.setText("swsh#195")
    main_window.stats_array = test_values
    
    main_window.ui.comboBox.setCurrentIndex(1)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[0] == screenshot
    
    main_window.ui.comboBox_2.setCurrentIndex(15)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[1] == screenshot
    
    qtbot.mouseClick(main_window.ui.toggleAngles, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[2] == screenshot
    
    qtbot.mouseClick(main_window.ui.directionButton, Qt.LeftButton)
    main_window.ui.upperRange.setValue(50)
    qtbot.mouseClick(main_window.ui.percentButton, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[3] == screenshot
    
    main_window.ui.lowerRange.setValue(20)
    qtbot.mouseClick(main_window.ui.percentButton, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[4] == screenshot
    
    qtbot.mouseClick(main_window.ui.toggleAngles, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[5] == screenshot
    
    qtbot.mouseClick(main_window.ui.rawButton, Qt.LeftButton)
    screen = qtbot.screenshot(main_window.ui.graphWidget)
    with open(screen, "rb") as f: screenshot = hashlib.sha256(f.read()).hexdigest()
    assert active_heatmaps[6] == screenshot