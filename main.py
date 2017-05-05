#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui,uic
from PyQt4.QtCore import *
from PyQt4.QtGui import QPalette,QBrush,QPixmap,QMovie

import time

import picamera

class MainWindow(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)
      
        #Dimensiones originales
        size_x_Original = 1080
        size_y_Original = 1920

        #Direcciones de Imágenes de fondo
        MAIN_VIEW = "resources/mainView.ui"

        # Se monta la interfaz de usuario para la pantalla principal
        self.ui = uic.loadUi(MAIN_VIEW)

        #Se bloquea el marco superior 
        self.ui.setWindowFlags(self.ui.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.ui.setWindowFlags(self.ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        #Full Screen
        self.ui.showFullScreen()
        screen = QtGui.QDesktopWidget().screenGeometry()  

        #Dimensiones de la pantalla
        self.size_x = screen.width()
        self.size_y = screen.height()

        print self.size_x, self.size_y

        #Relación imagen/pantalla
        rel_x = float(self.size_x)/float(size_x_Original)
        rel_y = float(self.size_y)/float(size_y_Original)

        #-----Pantalla Principal-----
        #------Boton de foto--------
        self.ui.photoBtn.move(self.size_x - 300,self.size_y/4)
        self.ui.photoBtn.mouseReleaseEvent = self.takePhoto

        #------Boton de video--------
        self.ui.videoBtn.move(self.size_x - 300,2*self.size_y/4)
        self.ui.videoBtn.mouseReleaseEvent = self.recordVideo

        #------Menu------
        #----Archivo-----
        self.ui.menuArchivo.addAction('Salir', self.closeApp)

        """
        with picamera.PiCamera() as picam:
            picam.start_preview()
            time.sleep(5)
            picam.capture('Foto01_Prueba.jpg')
            picam.stop_preview()
            picam.close()
        """

        
        self.ui.show()

    def takePhoto(self,event):
        print "Tomando foto..."

    def recordVideo(self,event):
        print "Tomando video..."
        self.ui.close()

    def closeApp(self):
        self.ui.close()


#Ejecución del programa
app = QtGui.QApplication(sys.argv)
MyWindow = MainWindow()
sys.exit(app.exec_())
