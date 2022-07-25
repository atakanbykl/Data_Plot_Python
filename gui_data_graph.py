from urllib import response
import matplotlib.pyplot as plt
import re
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QLineEdit, QDialog
import sys
import os
import numpy as np
import pandas as pd

class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('gui.ui', self) # Load the .ui file

        self.setWindowIcon(QtGui.QIcon('plot_icon_8_Ywb_icon.ico'))

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

    def readFile(self):
        print(self.pathTextBox.text())
        self.data = pd.read_csv(self.pathTextBox.text(), names = ["ID","angle","x","y"])
        self.data = self.data.replace(regex=[r'\D+'], value="").astype(float) # remove all non numeric values

    def movingAverage(self):
        self.angle_ma = np.array([])
        angle = np.array(self.data["angle"])
        ma_frame_size = int(self.maTextBox.text())

        for i in  range(len(self.data["angle"])):
            if i >= ma_frame_size:
                self.angle_ma = np.append(self.angle_ma , np.sum(angle[i - ma_frame_size : i]) / ma_frame_size)

    def plot(self):
        self.readFile()
        if self.maCheckBox.isChecked(): self.movingAverage()

        # plots
        # figure 1
        plt.figure("All Results").canvas.manager.window.move(100,100)
        plt.subplot(4,1,1)
        self.data["ID"].plot()
        plt.ylabel('QR ID')
        plt.grid()

        plt.subplot(4,1,2)
        self.data["y"].plot()
        plt.ylabel('Y Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,3)
        self.data["x"].plot()
        plt.ylabel('X Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,4)
        self.data["angle"].plot(label = "raw")
        if self.maCheckBox.isChecked():
            plt.plot(range(len(self.angle_ma)), self.angle_ma, label="moving average")
        plt.legend(loc="upper right")
        plt.ylabel('Angle(deg)')
        plt.grid()

        plt.xlabel('Sample(per semple is 2ms)')
        plt.show()

        # figure 2
        plt.figure("QR ID vs Y deviation").canvas.manager.window.move(750,100)
        self.data["ID"].plot(label = "ID")
        self.data["y"].plot(label = "Y")
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

