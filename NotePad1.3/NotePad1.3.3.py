import os.path

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import *
from PyQt5 import QtPrintSupport
from PyQt5 import QtGui, QtCore
import sys


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("NotePad")
        self.setWindowIcon(QIcon('notes.png'))
        self.resize(400, 200)
        self.Text = QTextEdit()
        self.Text.setAlignment(Qt.AlignVCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.Text)
        self._createActions()
        self._createMenuBar()
        self._createContextMenu()

        self.saveAction.triggered.connect(self.FileSave)
        self.saveAction.setShortcut('Ctrl+S')
        self.helpAction.triggered.connect(self.Help)
        self.helpAction.setShortcut('Ctrl+H')
        self.printAction.triggered.connect(self.print_file)
        self.printAction.setShortcut('Ctrl+P')
        self.openAction.triggered.connect(self.file_open)
        self.openAction.setShortcut('Ctrl+O')
        self.previewAction.triggered.connect(self.preview)
        self.previewAction.setShortcut('Ctrl+W')
        self.aboutAction.triggered.connect(self.About)
        self.aboutAction.setShortcut('Ctrl+I')
        self.fontAction.triggered.connect(self.Font)
        self.fontAction.setShortcut('Ctrl+T')
        self.colorAction.triggered.connect(self.Color)
        self.colorAction.setShortcut('Ctrl+R')
        self.themeDarkAction.triggered.connect(self.Dark)
        self.themeDarkAction.setShortcut('Ctrl+D')
        self.themeLightAction.triggered.connect(self.Light)
        self.themeLightAction.setShortcut('Ctrl+L')
        self.copyAction.triggered.connect(self.copy)
        self.copyAction.setShortcut('Ctrl+C')
        self.pasteAction.triggered.connect(self.paste)
        self.pasteAction.setShortcut('Ctrl+V')
        self.cutAction.triggered.connect(self.cut)
        self.cutAction.setShortcut('Ctrl+X')
        self.exitAction.triggered.connect(qApp.exit)
        self.exitAction.triggered.connect(self.closeEvent)
        self.exitAction.setShortcut('Ctrl+E')

        self.settings = QtCore.QSettings('Настройки', 'Использование ключей')
        if self.settings.contains('Окно/Местоположение'):
            self.setGeometry(self.settings.value('Окно/Местоположение'))
        else:
            self.resize(200, 50)
        if self.settings.contains('Окно/Тема'):
            self.setStyleSheet(self.settings.value('Окно/Тема1'))
            self.Text.setStyleSheet(self.settings.value('Окно/Тема2'))
        else:
            self.setStyleSheet('')
            self.Text.setStyleSheet('')

    def closeEvent(self, evt):
        self.settings.beginGroup('Окно')
        self.settings.setValue('Местоположение', self.geometry())
        self.settings.setValue('Тема1', self.styleSheet())
        self.settings.setValue('Тема2', self.Text.styleSheet())
        self.settings.endGroup()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        fileMenu.setIcon(QIcon('file.png'))
        menuBar.addMenu(fileMenu)

        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.printAction)
        fileMenu.addAction(self.exitAction)

        helpMenu = menuBar.addMenu("&Help")
        helpMenu.setIcon(QIcon('help.png'))
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)

        viewMenu = menuBar.addMenu("View")
        viewMenu.setIcon(QIcon('preview.png'))
        viewMenu.addAction(self.previewAction)

        self.themeMenu = viewMenu.addMenu('Theme')
        self.themeMenu.setIcon(QIcon('mode.png'))
        self.themeMenu.addAction(self.themeLightAction)
        self.themeMenu.addAction(self.themeDarkAction)

        editMenu = menuBar.addMenu("Edit")
        editMenu.setIcon(QIcon('edit.png'))
        editMenu.addAction(self.fontAction)
        editMenu.addAction(self.colorAction)
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)

    def _createActions(self):
        self.newAction = QAction(self)
        self.saveAction = QAction('Save as', self)
        self.printAction = QAction('Print', self)
        self.helpAction = QAction('Help', self)
        self.openAction = QAction('Open File', self)
        self.previewAction = QAction('Preview', self)
        self.aboutAction = QAction('About', self)
        self.fontAction = QAction('Font', self)
        self.colorAction = QAction('Color', self)
        self.themeLightAction = QAction('Light', self)
        self.themeDarkAction = QAction('Dark', self)
        self.copyAction = QAction('Copy', self)
        self.pasteAction = QAction('Paste', self)
        self.cutAction = QAction('Cut', self)
        self.exitAction = QAction('Exit', self)

        self.openAction.setIcon(QIcon('openfile.png'))
        self.saveAction.setIcon(QIcon('save_as.png'))
        self.printAction.setIcon(QIcon('print.png'))
        self.helpAction.setIcon(QIcon('help1.png'))
        self.previewAction.setIcon(QIcon('preview1.png'))
        self.aboutAction.setIcon(QIcon('about.png'))
        self.fontAction.setIcon(QIcon('font.png'))
        self.colorAction.setIcon(QIcon('palette.png'))
        self.themeLightAction.setIcon(QIcon('sun.png'))
        self.themeDarkAction.setIcon(QIcon('moon.png'))
        self.copyAction.setIcon(QIcon('copy.png'))
        self.pasteAction.setIcon(QIcon('paste.png'))
        self.cutAction.setIcon(QIcon('cut.png'))
        self.exitAction.setIcon(QIcon('exit.png'))

    def _createContextMenu(self):
        self.Text.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Text.addAction(self.saveAction)
        self.Text.addAction(self.openAction)
        self.Text.addAction(self.printAction)
        self.Text.addAction(self.previewAction)
        self.Text.addAction(self.copyAction)
        self.Text.addAction(self.pasteAction)
        self.Text.addAction(self.cutAction)

    def About(self):
        pixmap = QPixmap('atom.png')
        self.msg = QMessageBox(self)
        self.msg.setWindowIcon(QIcon("about.png"))
        self.msg.setWindowTitle("About")
        self.msg.setIconPixmap(pixmap)
        self.msg.setText("App Version-1.3.2 \n"
                         "Creator: Vildanov Almas")
        self.msg.exec_()

    def Help(self):
        self.msg1 = QMessageBox(self)
        self.msg1.setWindowIcon(QIcon("help.png"))
        self.msg1.setWindowTitle("Help")
        self.msg1.setText("При нажатии на 'Save as' текст сохраняется в выбранном формате\n"
                          "При нажатии на 'Print' производится печать содержимого текстового поля\n"
                          "При нажатии на 'Open File' открывается проводник с помощью которого можно открыть файл(формат-TXT)\n"
                          "При нажатии на 'Preview' открывается окно для предварительного просмотра текста\n"
                          "При нажатии на 'Copy' производится копирование выделенного текста\n"
                          "При нажатии на 'Paste' производится вставка скопированного текста\n"
                          "При нажатии на 'Cut' производится вырезание выделенного текста\n"
                          "При наведении на 'Theme' появляются ещё два действия: 'Light' и 'Dark'\n"
                          "При нажатии на 'Light' производится переход в светлый режим\n"
                          "При нажатии на 'Dark' производится переход в тёмный режим\n"
                          "'Font' отвечает за выбор шрифта и размера текста\n"
                          "'Color' отвечает за выбор цвета текста\n"
                          "При нажатии на 'Exit' происходит выход из приложения")
        self.msg1.exec_()

    def FileSave(self):
        text = self.Text.toPlainText()
        filename, _ = QFileDialog.getSaveFileName(None, "Save as", ".","Документ Word 97-2003 (*.doc);;Документ Word с поддержкой макросов (*.docm);;Документ Word (*.docx);;Документ Strict Open XML (*.docx);;Шаблон Word 97-2003 (*.dot);;Шаблон Word с поддержкой макросов (*.dotm);;Шаблон Word (*.dotx);;Веб-страница (*.htm;*.html);;Веб-страница с фильтром (*.htm;*.html);;Веб-страница в одном файле (*.mht;*.mhtml);;Текст OpenDocument (*.odt);;PDF (*.pdf);;Rich Text Format (*.rtf);;Обычный текст (*.txt);;Документ Works 6-9 (*.wps);;XML-документ Word 2003 (*.xml);;XML-документ Word (*.xml);; Документ XPS (*.xps);;Все файлы(Возможны ошибки!) (*)")
        if filename:
            with open(filename, 'w') as file:
                file.write(text)
                file.write('\n')

    def file_open(self):
        fname, ok = QFileDialog.getOpenFileName(self, 'Open file', "",
                                                "Документ Word 97-2003 (*.doc);;Документ Word с поддержкой макросов (*.docm);;Документ Word (*.docx);;Документ Strict Open XML (*.docx);;Шаблон Word 97-2003 (*.dot);;Шаблон Word с поддержкой макросов (*.dotm);;Шаблон Word (*.dotx);;Веб-страница (*.htm;*.html);;Веб-страница с фильтром (*.htm;*.html);;Веб-страница в одном файле (*.mht;*.mhtml);;Текст OpenDocument (*.odt);;PDF (*.pdf);;Rich Text Format (*.rtf);;Обычный текст (*.txt);;Документ Works 6-9 (*.wps);;XML-документ Word 2003 (*.xml);;XML-документ Word (*.xml);; Документ XPS (*.xps);;Все файлы(Возможны ошибки!)  (*)")
        if ok:
            f = open(fname, 'r')

            with f:
                data = f.read()
                self.Text.setText(data)

    def print_file(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.Text.print_(printer)

    def preview(self):
        pp = QtPrintSupport.QPrintPreviewDialog()
        pp.paintRequested.connect(self.Text.print_)
        pp.exec_()

    def Font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.Text.setFont(font)

    def Color(self):
        color = QColorDialog.getColor()
        self.Text.setTextColor(color)

    def Dark(self):
        self.Text.setStyleSheet('background-color: rgb(60, 60, 60); color: rgb(255, 255, 255);')
        self.setStyleSheet('background-color: rgb(175, 175, 175);')

    def Light(self):
        self.Text.setStyleSheet('')
        self.setStyleSheet('')

    def copy(self):
        self.Text.copy()

    def paste(self):
        self.Text.paste()

    def cut(self):
        self.Text.cut()

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())