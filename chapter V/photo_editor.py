from operator import mod
import sys
from tkinter import Label, image_names
from PyQt6.QtWidgets import (QApplication, QMainWindow, 
    QWidget, QLabel, QPushButton, QDockWidget, QDialog,
    QFileDialog, QMessageBox, QToolBar, QStatusBar,
    QVBoxLayout)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import (QIcon, QAction, QPixmap, QTransform, 
    QPainter)
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
import os
os.chdir(os.path.dirname(__file__))


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initilizeUI()
    
    def initilizeUI(self):

        self.setMinimumSize(800,500)
        self.setWindowTitle("private shutz GUI")

        self.setMainWindow()
        self.createToolDock()
        self.createAction()
        self.createMenu()
        self.createToolBar()
        self.show()
    
    def setMainWindow(self):

        self.image = QPixmap()
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.image_label)

        self.setStatusBar(QStatusBar())

    def createToolDock(self):

        dock_widgt = QDockWidget()
        dock_widgt.setWindowTitle("processing")
        dock_widgt.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea |
                                Qt.DockWidgetArea.LeftDockWidgetArea
        )

        rotate_90_bnt = QPushButton("Rotate 90")
        rotate_90_bnt.setMinimumSize(QSize(140,30))
        rotate_90_bnt.setStatusTip("rotate 90 degree")
        rotate_90_bnt.clicked.connect(self.rotateImage)

        rotate_180_bnt = QPushButton("Rotate 180")
        rotate_180_bnt.setMinimumSize(QSize(140,30))
        rotate_180_bnt.setStatusTip("rotate 180 degree")
        rotate_180_bnt.clicked.connect(self.rotateImage)

        flip_H_bnt = QPushButton("flip H")
        flip_H_bnt.setMinimumSize(QSize(140,30))
        flip_H_bnt.setStatusTip("flip Horizontal")
        flip_H_bnt.clicked.connect(self.flipHorizontal)

        flip_V_bnt = QPushButton("flip V")
        flip_V_bnt.setMinimumSize(QSize(140,30))
        flip_V_bnt.setStatusTip("flip Vertical")
        flip_V_bnt.clicked.connect(self.flipVertical)

        v_box = QVBoxLayout()
        v_box.addWidget(rotate_90_bnt)
        v_box.addWidget(rotate_180_bnt)
        v_box.addStretch(1)
        v_box.addWidget(flip_H_bnt)
        v_box.addWidget(flip_V_bnt)
        v_box.addStretch(10)

        dock_layout = QWidget()
        dock_layout.setLayout(v_box)
        dock_widgt.setWidget(dock_layout)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,dock_widgt)

        self.dock_widgt_view = dock_widgt.toggleViewAction()

    def createAction(self):

        self.open_act = QAction(QIcon("./images/open_file.png"),"Open")
        self.open_act.setShortcut("ctrl+o")
        self.open_act.setStatusTip("open a photo")
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon("./images/save_file.png"),"Save")
        self.save_act.setStatusTip("save a photo")
        self.save_act.triggered.connect(self.saveImage)

        self.quit_act = QAction(QIcon("./images/exit.png"),"Quit")
        self.quit_act.setStatusTip("Quit the app")
        self.quit_act.triggered.connect(self.close)

        self.rotate90_act = QAction("Rotate 90º")
        self.rotate90_act.setStatusTip('Rotate image 90º clockwise')
        self.rotate90_act.triggered.connect(self.rotateImage)

        self.rotate180_act = QAction("Rotate 180º")
        self.rotate180_act.setStatusTip("Rotate image 180º clockwise")
        self.rotate180_act.triggered.connect(self.rotateImage)

        self.flip_hor_act = QAction("Flip Horizontal")
        self.flip_hor_act.setStatusTip("Flip image across horizontal axis")
        self.flip_hor_act.triggered.connect(self.flipHorizontal)

        self.flip_ver_act = QAction("Flip Vertical")
        self.flip_ver_act.setStatusTip("Flip image across vertical axis")
        self.flip_ver_act.triggered.connect(self.flipVertical)

        self.clear_act = QAction(QIcon("images/clear.png"), "Clear Image")
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip("Clear the current image")
        self.clear_act.triggered.connect(self.clearImage)

    def createMenu(self):

        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addAction(self.quit_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)

        view_menu = self.menuBar().addMenu("View")
        view_menu.addAction(self.dock_widgt_view)

    def createToolBar(self):

        tool_bar = QToolBar()
        tool_bar.setIconSize(QSize(24,24))

        self.addToolBar(tool_bar)

        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.quit_act)
    
    def openImage(self):

        file_name,_ = QFileDialog.getOpenFileName(
            self,"open Image","/Users/macbookair/Desktop/编程/pyqt6",
            "JPG File(*.jpg *.jpeg);;PNG File(*.png);;GIF File(*.gif);;\
                Bitmap Files (*.bmp)"
            )

        try:
            with open(file_name):
                self.image = QPixmap(file_name)
                self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
                aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                transformMode=Qt.TransformationMode.SmoothTransformation)
                )
        except FileNotFoundError as error:

            QMessageBox.warning(self,"Not Image",
            f"""<p>Error:{error}.</p>
            <p>please check the direction</p>""",
            QMessageBox.StandardButton.Close
            )
    def saveImage(self):

        file_name,_ = QFileDialog.getSaveFileName(
            self,"save Image","/Users/macbookair/Desktop/编程/pyqt6",
            "JPG File(*.jpg *.jpeg);;PNG File(*.png);;GIF File(*.gif);;\
                Bitmap Files (*.bmp)"
        )

        if file_name and self.image.isNull() == False:
            self.image.save(file_name)
        else:
            QMessageBox.information(self, "Not Saved", 
                "Image not saved.", QMessageBox.StandardButton.Ok)
    
    def rotateImage(self):
        """Rotate image 90º clockwise."""
        send = self.sender()
        r = int(send.text().split(" ")[1])
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(r)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, 
                mode=mode)

            self.image_label.setPixmap(rotated.scaled(self.image_label.size(), 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(rotated) 
            self.image_label.repaint() # Repaint the child widget

    def flipHorizontal(self):

        if self.image.isNull() == False:

            transform = QTransform().scale(-1,1)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            pixmap=pixmap.transformed(transform,mode)

            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(),
                aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                transformMode=mode)
                )
            self.image = pixmap
            self.image_label.repaint()
    
    def flipVertical(self):
    
        if self.image.isNull() == False:

            transform = QTransform().scale(1,-1)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            pixmap=pixmap.transformed(transform,mode)

            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(),
                aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                transformMode=mode)
                )
            self.image = pixmap
            self.image_label.repaint()

    def clearImage(self):

        self.image_label.clear()
        self.image = QPixmap() # Reset pixmap so that isNull() = True
    
    def printImage(self):

        printer = QPrinter()
        print_diag = QPrintDialog(printer)

        if print_diag.exec() == QDialog.DialogCode.Accepted:

            painter = QPainter()

            painter.begin(printer)
            rect = QRect(painter.viewport())
            size = QSize(self.image_label.pixmap().size())

            size.scale(rect.size(),Qt.AspectRatioMode.KeepAspectRatio)

            painter.setViewport(rect.x(),rect.y(),size.width(),size.height())
            painter.setWindow(self.image_label.pixmap().rect())

            painter.drawPixmap(0,0,self.image_label.pixmap())
            painter.end()


if __name__ == "__main__":

    app = QApplication([])
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus)

    window = MainWindow()
    sys.exit(app.exec())