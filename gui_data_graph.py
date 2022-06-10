
from urllib import response
import matplotlib.pyplot as plt
import csv
import re
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QLineEdit
import sys
import os

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.window_width, self.window_height = 800, 200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # self.options = ('Get File Name', 'Save File Name')

        # self.combo = QComboBox()
        # self.combo.addItems(self.options)
        # layout.addWidget(self.combo)

        self.text = QLineEdit()
        layout.addWidget(self.text)


        btn = QPushButton('Launch')
        # btn.clicked.connect(self.launchDialog)
        btn.clicked.connect(self.getFilePath)

        layout.addWidget(btn)

        plotButton = QPushButton('Plot')
        plotButton.clicked.connect(self.plot)
        layout.addWidget(plotButton)

    def plot(self):
        print(self.path)

        ID=[]
        angle=[] 
        x = []
        y = []

        with open(self.path,"r") as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                ID.append(int(re.sub("[^0-9]", "", row[0])))
                angle.append(float(row[1]))
                x.append(float(row[2]))
                y.append(float(row[3]))

        plt.subplot(4,1,1) 
        plt.plot(range(len(ID)), ID)
        plt.ylabel('QR ID')
        plt.grid()

        plt.subplot(4,1,2) 
        plt.plot(range(len(angle)), angle)
        plt.ylabel('Angle(deg)')
        plt.grid()

        plt.subplot(4,1,3) 
        plt.plot(range(len(x)), x)
        plt.ylabel('X Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,4) 
        plt.plot(range(len(y)), y)
        plt.ylabel('Y Deviation(mm)')
        plt.grid()
        
        # plt.xticks(rotation = 25)
        plt.xlabel('Sample')
        # plt.title('Weather Report', fontsize = 20)
        # plt.legend()

        plt.show()

    def getFilePath(self):
        file_filter = 'Data File (*.csv)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            # initialFilter='Excel File (*.xlsx *.xls)'
        )
        self.text.setText(response[0])
        print(response)
        self.path = response[0]

    
    # def getSaveFileName(self):
    #     file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
    #     response = QFileDialog.getSaveFileName(
    #         parent=self,
    #         caption='Select a data file',
    #         directory= 'Data File.dat',
    #         filter=file_filter,
    #         initialFilter='Excel File (*.xlsx *.xls)'
    #     )
    #     print(response)
    #     return response[0]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

