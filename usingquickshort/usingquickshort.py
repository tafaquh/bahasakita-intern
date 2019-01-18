import pandas as pd

#try
def partition(arr,low,high): 
  i = ( low-1 )         # index of smaller element 
  pivot = arr[high]     # pivot 

  for j in range(low , high): 
    if   arr[j] <= pivot: 
      i = i+1 
      arr[i],arr[j] = arr[j],arr[i] 

  arr[i+1],arr[high] = arr[high],arr[i+1] 
  return ( i+1 ) 

def quickSort(arr,low,high): 
  if low < high: 
    pi = partition(arr,low,high) 
    quickSort(arr, low, pi-1) 
    quickSort(arr, pi+1, high) 

filepath = "D:\Kuliah\Lowongan\BahasaKita\program\data/tafaquh.fiddinal@gmail.com_00.csv"

print("Starting to read data...")
df = pd.read_csv(filepath,index_col=None, header=0)

