"""
                                                     
     /\                                              
    /  \   _ __ ___  _ __   ___ _ __ __ _  __ _  ___ 
   / /\ \ | '_ ` _ \| '_ \ / _ \ '__/ _` |/ _` |/ _ \
  / ____ \| | | | | | |_) |  __/ | | (_| | (_| |  __/
 /_/    \_\_| |_| |_| .__/ \___|_|  \__,_|\__, |\___|
  _____           _ | |       _        _   __/ |     
 |_   _|         | ||_|      | |      (_) |___/      
   | |  _ __   __| |_   _ ___| |_ _ __ _  ___  ___   
   | | | '_ \ / _` | | | / __| __| '__| |/ _ \/ __|  
  _| |_| | | | (_| | |_| \__ \ |_| |  | |  __/\__ \  
 |_____|_| |_|\__,_|\__,_|___/\__|_|  |_|\___||___/                                  
                                                     
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QCheckBox, QFileDialog
from Pokegrab import PKGRAB

class PokerabGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create labels and text boxes
        self.dex_label = QLabel('DEX:', self)
        self.dex_label.move(20, 20)
        self.dex_textbox = QLineEdit(self)
        self.dex_textbox.move(100, 20)
        self.dex_textbox.resize(280, 20)

        self.path_label = QLabel('Path:', self)
        self.path_label.move(20, 50)
        self.path_textbox = QLineEdit(self)
        self.path_textbox.move(100, 50)
        self.path_textbox.resize(200, 20)
        self.path_button = QPushButton('Browse', self)
        self.path_button.move(300, 50)
        self.path_button.clicked.connect(self.browse_path)

        self.ability_checkbox = QCheckBox('Ability', self)
        self.ability_checkbox.move(20, 80)
        self.ability_checkbox.setChecked(False)

        self.types_checkbox = QCheckBox('Types', self)
        self.types_checkbox.move(100, 80)
        self.types_checkbox.setChecked(False)

        self.handw_checkbox = QCheckBox('Handw', self)
        self.handw_checkbox.move(180, 80)
        self.handw_checkbox.setChecked(False)

        self.output_label = QLabel('Output:', self)
        self.output_label.move(20, 110)
        self.output_textbox = QTextEdit(self)
        self.output_textbox.move(100, 110)
        self.output_textbox.resize(280, 120)

        # Create a button to run the PKGRAB function
        self.run_button = QPushButton('Run PKGRAB', self)
        self.run_button.move(20, 240)
        self.run_button.clicked.connect(self.run_pkgrab)

        # Set the window properties
        self.setGeometry(100, 100, 400, 280)
        self.setWindowTitle('Pokerab GUI')
        self.show()

    def browse_path(self):
        # Open a file dialog to select a file path
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filepath, _ = QFileDialog.getSaveFileName(self, "Select a file", "", "CSV Files (*.csv)", options=options)
        self.path_textbox.setText(filepath)

    def run_pkgrab(self):
        # Get the user inputs
        dex = self.dex_textbox.text()
        path = self.path_textbox.text()
        ability = self.ability_checkbox.isChecked()
        types = self.types_checkbox.isChecked()
        handw = self.handw_checkbox.isChecked()

        # Call the PKGRAB function with the user inputs
        output = PKGRAB(int(dex), path, ability, types, handw)

        # Display the output in the output text box
        self.output_textbox.setText(output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PokerabGUI()
    sys.exit(app.exec_())
