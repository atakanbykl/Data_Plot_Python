
from urllib import response
import matplotlib.pyplot as plt
import csv
import re
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QLineEdit
import sys
import os
import numpy


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Plot data")
        
        # window size
        self.window_width, self.window_height = 800, 200
        self.setMinimumSize(self.window_width, self.window_height)

        # set leyout
        layout = QVBoxLayout()
        self.setLayout(layout)       

        # add layout
        self.textBox = QLineEdit()
        self.textBox.setGeometry(0,0,20,1000)
        layout.addWidget(self.textBox)

        # add get path button
        pathButton = QPushButton('Get Path')
        pathButton.clicked.connect(self.getFilePath)
        layout.addWidget(pathButton)

        # add plot button
        plotButton = QPushButton('Plot')
        plotButton.clicked.connect(self.plot)
        layout.addWidget(plotButton)

    def plot(self):
        print(self.path)
        
    # init
        ID =[]
        angle =[] 
        angle_ma = []
        x = []
        y = []
        ma_frame_size = 40

    # read file
        with open(self.path,"r") as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                # ID_ = int(re.sub("[^0-9]", "", row[0]))
                # if lines.line_num < 3: ID.append(ID_)
                # else: ID.append(ID_ if  ID_ > (ID[lines.line_num - 3] + 50) else ID[lines.line_num - 3])
                ID.append(int(re.sub("[^0-9]", "", row[0])))
                angle.append(float(row[1]))
                x.append(float(row[2]))
                y.append(float(row[3]))
    # moving average
        for i in  range(len(angle)):
            if i < ma_frame_size:
                pass
            else:
                angle_ma.append(numpy.sum(angle[i - ma_frame_size : i]) / ma_frame_size)

    # plots
        # figure 2
        plt.figure(1)
        plt.subplot(4,1,1) 
        plt.plot(range(len(ID)), ID)
        plt.ylabel('QR ID')
        plt.grid()

        plt.subplot(4,1,2) 
        plt.plot(range(len(y)), y)
        plt.ylabel('Y Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,3) 
        plt.plot(range(len(x)), x)
        plt.ylabel('X Deviation(mm)')
        plt.grid()

        plt.subplot(4,1,4) 
        plt.plot(range(len(angle)), angle, label="raw")
        plt.plot(range(len(angle_ma)), angle_ma, label="moving average")
        plt.legend(loc="upper right")
        plt.ylabel('Angle(deg)')
        plt.grid()
        
        plt.xlabel('Sample(per semple is 2ms)')
        plt.show()

        # figure 2
        plt.figure(2)
        plt.plot(range(len(ID)), ID,label="ID")
        plt.plot(range(len(y)), y,label="Y")
        plt.legend(loc="upper right")
        plt.grid()

        plt.xlabel('Sample(per semple is 2ms)')
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

