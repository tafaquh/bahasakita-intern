import pandas as pd

filepath = "D:\Kuliah\Lowongan\BahasaKita\program\data/tafaquh.fiddinal@gmail.com_00.csv"

print("Starting to read data...")
df = pd.read_csv(filepath,index_col=None, header=0)

df = df.sort_values('distance_to_earth')
print("Finish")
topthousand = df.iloc[0:1000]

# Print top ten shortes planet
print(".::Top Ten Closest Planets to Earth::.")
print(topthousand.iloc[0:10])

# Print average of closest thousand planet
average = topthousand['distance_to_earth'].mean()
print("Average Top Thousand Planets Distance to Earh = ",average)