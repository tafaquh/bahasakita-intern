import glob
import pandas as pd

path ="D:\Kuliah\Lowongan\BahasaKita\program\data" # datapath
allFiles = glob.glob(path + "/*.csv")

list_ = []

print("Starting to read data...")
for file_ in allFiles:
  datum = pd.read_csv(file_,index_col=None, header=0)
  list_.append(datum)

df = pd.concat(list_, axis = 0, ignore_index = True)
print("Finish")

df = df.sort_values('distance_to_earth')
topthousand = df.iloc[0:1000]

# Print top ten shortes planet
print(".::Top Ten Closest Planets to Earth::.")
print(topthousand.iloc[0:10])

# Print average of closest thousand planet
average = topthousand['distance_to_earth'].mean()
print("Average Top Thousand Planets Distance to Earh = ",average)