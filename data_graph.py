import matplotlib.pyplot as plt
import csv
import re

ID=[]
angle=[] 
x = []
y = []
  
with open("C:\\Users\\Developer\\Desktop\\project_files\\Python\\data\\33_\\velocity\\velocity_line2_33_controller_off.csv","r") as csvfile:
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