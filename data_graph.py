import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

data = pd.read_csv ('data_line_test_1.csv', names = ['ID','Angle','X','Y'])
# df = pd.DataFrame(data, columns= ['ID','Angle','X','Y'])
# print (df)
# ID= data.columns.str.strip()

# print (ID)

plt.show()

input()