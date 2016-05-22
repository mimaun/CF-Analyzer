#! /usr/bin/python
## -*- coding: utf-8 -*-
import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
# from PySide.QtUiTools import QUiLoader


# 画面上部のDescription
class DescriptionWidget(QWidget):
    # def __init__(self, parent=None, text):
    def __init__(self, parent=None):
        super(DescriptionWidget, self).__init__(parent)
        self.text = ""
        self.setUpUi()

    def setUpUi(self): 
        title_label = QLabel("<h2>Description</h2>")
        self.details_label = QLabel(self.text)

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.details_label) 
        self.setLayout(layout)

    def setDetails(self, text):
        self.details_label.setText(text) 

#input / outputファイル参照Widget
class FileDialogGridWidget(QWidget):
    def __init__(self, parent=None):
        super(FileDialogGridWidget, self).__init__(parent) 
        self.setUpUi()

    def setUpUi(self):
        grid_layout = QGridLayout()

        input_label = QLabel(u'ファイル選択')
        self.input_line_edit = QLineEdit() 
        self.input_line_edit.setReadOnly(True) 
        input_button = QPushButton(u'参照')

        output_label = QLabel(u'出力先選択')
        self.output_line_edit = QLineEdit() 
        self.output_line_edit.setReadOnly(True) 
        output_button = QPushButton(u'参照')

        # button Signal 
        input_button.clicked.connect(self.openFile)
        output_button.clicked.connect(self.openDirectory) 

        grid_layout.addWidget(input_label, 0, 0)
        grid_layout.addWidget(output_label, 0, 2)
        grid_layout.addWidget(self.input_line_edit, 1, 0)
        grid_layout.addWidget(input_button, 1, 1)
        grid_layout.addWidget(self.output_line_edit, 1, 2)
        grid_layout.addWidget(output_button, 1, 3)
        self.setLayout(grid_layout) 

    def openFile(self):
        # file_path = QFileDialog.getOpenFileName(self, filter = 'Text file (*.txt)')
        file_path = QFileDialog.getOpenFileName(self)
        self.input_line_edit.setText(file_path[0])
        return

    def openDirectory(self):
        dir_path = QFileDialog.getExistingDirectory(self)
        self.output_line_edit.setText(dir_path)

# dropdown, 時間options widget
class GroupOfOptionWidget(QWidget):
    def __init__(self, parent=None):
        super(GroupOfOptionWidget, self).__init__(parent)
        self.setUpUi()

    def setUpUi(self):
        self.combo_1 = QComboBox()
        self.combo_1.addItem("xxxxxxxxxxxx")
        self.combo_1.addItem("yyyyyyyyyyyy")
        self.combo_1.addItem("zzzzzzzzzzzz")

        self.combo_2 = QComboBox()
        self.combo_2.addItem("xxxxxxxxxxxx")
        self.combo_2.addItem("yyyyyyyyyyyy")
        self.combo_2.addItem("zzzzzzzzzzzz")

        self.combo_3 = QComboBox()
        self.combo_3.addItem("xxxxxxxxxxxx")
        self.combo_3.addItem("yyyyyyyyyyyy")
        self.combo_3.addItem("zzzzzzzzzzzz")

        # 音声ファイルの使用範囲
        self.start_min_edit = QLineEdit()
        self.start_sec_edit = QLineEdit()
        self.finish_min_edit = QLineEdit()
        self.finish_sec_edit = QLineEdit()
        self.start_min_edit.setFixedWidth(50)
        self.start_sec_edit.setFixedWidth(50)
        self.finish_min_edit.setFixedWidth(50)
        self.finish_sec_edit.setFixedWidth(50) 

        group_box = QGroupBox()
        time_range_h_layout = QHBoxLayout()
        time_range_h_layout.addWidget(self.start_min_edit)
        time_range_h_layout.addWidget(QLabel(":"))
        time_range_h_layout.addWidget(self.start_sec_edit)
        time_range_h_layout.addWidget(QLabel("~"))
        time_range_h_layout.addWidget(self.finish_min_edit)
        time_range_h_layout.addWidget(QLabel(":"))
        time_range_h_layout.addWidget(self.finish_sec_edit)
        group_box.setLayout(time_range_h_layout)

        layout = QHBoxLayout()
        layout.addWidget(self.combo_1)
        layout.addWidget(self.combo_2)
        layout.addWidget(self.combo_3)
        layout.addWidget(group_box) 

        self.setLayout(layout)


# output欄、操作ボタンセットのwidget
class OutputWidget(QWidget):
    def __init__(self, parent=None):
        super(OutputWidget, self).__init__(parent)
        self.setUpUi()

    def setUpUi(self):
        h_layout = QHBoxLayout()
        output_label = QLabel('<h2>Output</h2>')
        self.run_button = QPushButton('Run')
        self.clear_button = QPushButton('Clear')
        h_layout.addWidget(output_label)
        h_layout.addWidget(self.run_button)
        h_layout.addWidget(self.clear_button) 
        h_layout.setAlignment(self.run_button, Qt.AlignRight)
        h_layout.setAlignment(self.clear_button, Qt.AlignRight)

        self.output_text_edit = QTextEdit()
        self.output_text_edit.setPlainText('The output will be shown here')
        self.output_text_edit.setReadOnly(True)

        layout = QVBoxLayout() 
        layout.addLayout(h_layout)
        layout.addWidget(self.output_text_edit)
        self.setLayout(layout)

class PauseWidget(QWidget):
    def __init__(self, parent=None):
        super(PauseWidget, self).__init__(parent)
        self.setUpUi()

    def setUpUi(self):
        layout = QVBoxLayout() 
        description_widget = DescriptionWidget()
        file_dialog_widget = FileDialogGridWidget()
        options_widget = GroupOfOptionWidget()
        output_widget = OutputWidget()

        # test
        test_text = "The chilling Saga of Darren Shan, the ordinary schoolboy plunged into the vampire world. Darren goes to a banned freak show with his best mate Steve. \nIt's the wonderfully gothic Cirque Du Freak where weird, frightening half human/half ..."

        description_widget.setDetails(test_text)

        layout.addWidget(description_widget)
        layout.addWidget(file_dialog_widget)
        layout.addWidget(options_widget)
        layout.addWidget(output_widget)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("File Dialog Test")
        self.setFixedSize(800, 600)

        self.pause_widget = PauseWidget()
        self.setCentralWidget(self.pause_widget)

    def changeWindwoWidget(self, window_widget):
        self.setCentralWidget(window_widget)

def main(): 
    app = QApplication(sys.argv)

    # 日本語設定.
    QTextCodec.setCodecForCStrings(QTextCodec.codecForLocale()) 

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

