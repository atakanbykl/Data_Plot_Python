from urllib import response
import matplotlib.pyplot as plt
import csv
import re
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QLineEdit, QDialog
import sys
import os
import numpy


# class MyApp(QWidget):
class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__() 
        uic.loadUi('gui.ui', self) # Load the .ui file

        self.ID =[]
        self.angle =[] 
        self.angle_ma = []
        self.x = []
        self.y = []
              
        self.pathButton.clicked.connect(self.getFilePath) # get path button         
        self.plotButton.clicked.connect(self.plot) # plot button

        self.show() # Show the GUI

    def getFilePath(self):
        file_filter = 'Data File (*.csv)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
        )
        self.pathTextBox.setText(response[0])
        self.path = response[0]
    
    def openFile(self):
        with open(self.path,"r") as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                # ID_ = int(re.sub("[^0-9]", "", row[0]))
                # if lines.line_num < 3: ID.append(ID_)
                # else: ID.append(ID_ if  ID_ > (ID[lines.line_num - 3] + 50) else ID[lines.line_num - 3])
                self.ID.append(int(re.sub("[^0-9]", "", row[0])))
                self.angle.append(float(row[1]))
                self.x.append(float(row[2]))
                self.y.append(float(row[3]))

    def movingAverage(self):        
        ma_frame_size = int(self.maTextBox.text())
        for i in  range(len(self.angle)):
            if i < ma_frame_size:
                pass
            else:
                self.angle_ma.append(numpy.sum(self.angle[i - ma_frame_size : i]) / ma_frame_size)


    def plot(self):
        self.path = self.pathTextBox.text()
        print(self.path)
        
        self.openFile()
        if self.maCheckBox.isChecked(): self.movingAverage()    

        # plots
        # figure 1
        plt.figure("All Results").canvas.manager.window.move(100,100)
        plt.subplot(4,1,1) 
        plt.plot(range(len(self.ID)), self.ID)
        plt.ylabel('QR ID')
        plt.grid()

        plt.subplot(4,1,2) 
        plt.plot(range(len(self.y)), self.y)
        plt.ylabel('Y Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,3) 
        plt.plot(range(len(self.x)), self.x)
        plt.ylabel('X Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,4) 
        plt.plot(range(len(self.angle)), self.angle, label="raw")
        if self.maCheckBox.isChecked():
            plt.plot(range(len(self.angle_ma)), self.angle_ma, label="moving average")
        plt.legend(loc="upper right")
        plt.ylabel('Angle(deg)')
        plt.grid()
        
        plt.xlabel('Sample(per semple is 2ms)')
        plt.show()

        # figure 2
        plt.figure("QR ID vs Y deviation").canvas.manager.window.move(750,100)
        plt.plot(range(len(self.ID)), self.ID,label="ID")
        plt.plot(range(len(self.y)), self.y,label="Y")
        plt.legend(loc="upper right")
        plt.grid()

        plt.xlabel('Sample(per semple is 2ms)')
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)    
    myApp = MyApp()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

