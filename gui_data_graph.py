from urllib import response
import matplotlib.pyplot as plt
import re
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QLineEdit, QDialog
from ui.gui import Ui_Dialog
import sys
import os
import numpy as np
import pandas as pd

class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        # uic.loadUi('gui.ui', self) # Load the .ui file

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.readDataset("./dataframe_config.json")

        self.setWindowIcon(QtGui.QIcon('./icons/plot_icon_8_Ywb_icon.ico'))

        self.ui.pathButton.clicked.connect(self.getFilePath) # get path button
        self.ui.plotButton.clicked.connect(self.plot) # plot button
        self.ui.datasetButton.clicked.connect(self.getDataset) # dataset config button

        self.show() # Show the GUI

    def getFilePath(self):
        file_filter = 'Data File (*.csv)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
        )
        self.ui.pathTextBox.setText(response[0])

    def getDataset(self):
        file_filter = 'Data File (*.json)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a dataframe config file',
            directory=os.getcwd(),
            filter=file_filter,
        )
        self.readDataset(response[0])

    def readDataset(self,pathDataset):
        self.dataset = pd.read_json(pathDataset)
        self.ui.datasetList.clear()
        for ds in self.dataset:
            self.ui.datasetList.addItem(ds)

    def readFile(self):
        print(f"Reading data from {self.ui.pathTextBox.text()}")
        print(f"Selected Dataframe set: {self.ui.datasetList.currentText()}")
        self.sellectedSet =  self.dataset[self.ui.datasetList.currentText()]["frame"]

        self.data = pd.read_csv(self.ui.pathTextBox.text(), names = self.sellectedSet)
        self.data = self.data.replace(regex=[r'\D+'], value="").astype(float) # remove all non numeric values

    def movingAverage(self):
        self.angle_ma = np.array([])
        angle = np.array(self.data["angle"])
        ma_frame_size = int(self.ui.maTextBox.text())

        for i in  range(len(self.data["angle"])):
            if i >= ma_frame_size:
                self.angle_ma = np.append(self.angle_ma , np.sum(angle[i - ma_frame_size : i]) / ma_frame_size)
            plt.plot(self.angle_ma, label = "ma")

    def plot(self):
        self.readFile()

        plt.figure("All Results").canvas.manager.window.move(100,100)
        dataQuantity = len(self.sellectedSet)
        dataCount = 1
        for dt in self.sellectedSet:
            plt.subplot(dataQuantity, 1, dataCount)
            self.data[dt].plot()
            if self.ui.maCheckBox.isChecked() and dt == "angle": self.movingAverage()
            plt.ylabel(dt)
            plt.grid()
            dataCount = dataCount + 1
        plt.xlabel('Sample(per semple is 2ms)')
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

