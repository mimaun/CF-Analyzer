# -*- coding: utf-8 -*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *

# 画面上部のDescription
class TopDescriptionWidget(QWidget):
    # def __init__(self, parent=None, text):
    def __init__(self, parent=None):
        super(TopDescriptionWidget, self).__init__(parent)
        self.text = "test"

        self.title_label = QLabel("<h2>Description</h2>")
        self.details_label = QLabel(self.text)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.details_label) 
        self.setLayout(layout)

    def setDetails(self, text):
        self.details_label.setText(text) 

# Pause / CF 分岐ボタンwidget
class BranchButtonBoxWidget(QWidget):
    def __init__(self, parent=None):
        super(BranchButtonBoxWidget, self).__init__(parent)

        self.pause_analyzer_button = QPushButton("Pause Analyzer", parent=self)
        self.cf_analyzer_button = QPushButton("CF Analyzer", parent=self)

        layout = QHBoxLayout()
        layout.addWidget(self.pause_analyzer_button)
        layout.addWidget(self.cf_analyzer_button) 
        self.setLayout(layout)

# TOP 画面Widget
class TopWindowWidget(QWidget):
    def __init__(self, parent=None):
        super(TopWindowWidget, self).__init__(parent)

        self.layout = QVBoxLayout()

        self.branch_button_widget = BranchButtonBoxWidget()

        # test
        self.test_text = ""
        for i in range(5):
            self.test_text += "ヾ(⌒(ﾉｼ >ω<)ﾉｼ ヾ(:3ﾉｼヾ)ﾉｼ ヾ(°ω｡ヽ=ﾉ°ω｡)ノ ヾ(⌒(ﾉｼ >ω<)ﾉｼ ｼﾞﾀﾊﾞﾀ ヾ(:3ﾉｼヾ)ﾉｼ三ヾ(ﾉｼヾε:)ﾉ (ﾉｼ>△<)ﾉｼ _(⌒ﾉｼ 'ω')ﾉｼ ヾ(⌒(ﾉ'ω')ﾉ \n" 
        #test

        self.description_widget = TopDescriptionWidget()
        self.description_widget.setDetails(self.test_text)

        self.layout.addWidget(self.description_widget)
        self.layout.addWidget(self.branch_button_widget)

        self.setLayout(self.layout) 

class PauseAnalyzerWindowWidget():
    def __init__(self, parent=None):
        super(PauseAnalyzerWindowWidget, self).__init__(parent)

# def clearAllWidgets():
#     for i in reversed(range(layout.count())):
#         layout.itemAt(i).widget().setParent(None)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Main Window")
        # self.setFixedSize(800, 250)
        # self.status_bar.showMessage("Main Window")

        # top window
        self.top_window_widget = TopWindowWidget()
        self.setCentralWidget(self.top_window_widget)

    def changeWindwoWidget(self, window_widget):
        self.setCentralWidget(window_widget)

def main(): 
    app = QApplication(sys.argv)
    
    # 日本語設定.
    QTextCodec.setCodecForCStrings(QTextCodec.codecForLocale()) 

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
    
