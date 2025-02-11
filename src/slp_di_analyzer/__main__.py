import sys, os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from slp_di_analyzer import gui
from qt_material import apply_stylesheet

if __name__ == "__main__":    
    app = QApplication(sys.argv)

    # Disables combobox animation to avoid rare flicker issue
    app.setEffectEnabled(Qt.UIEffect(3), False)
    window = gui.MainWindow()
    extras = { 'font_family': "Roboto" }
    apply_stylesheet(app, theme=os.path.abspath(os.path.dirname(__file__))+'/karinemachine.xml', css_file=os.path.abspath(os.path.dirname(__file__))+'/custom.css', extra=extras)
    window.update_graph()
    window.show()
    


    sys.exit(app.exec())