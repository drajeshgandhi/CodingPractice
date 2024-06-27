#----------------------------------------#
#Pandas and Numpy 
#----------------------------------------#
import pandas as pd    
dict_info = {'key1' : 2.0, 'key2' : 3.1, 'key3' : 2.2}  
series_obj = pd.Series(dict_info)    
print (series_obj) 
#----------------------------------------#
import pandas as pd      
data_info = {'first' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),    
       'second' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}    
  
df = pd.DataFrame(data_info)    
#To add new column third
df['third']=pd.Series([10,20,30],index=['a','b','c'])    
print (df)    
#To add new column fourth
df['fourth']=df['first']+info['third']    
print (df)   
#----------------------------------------#
import numpy as np
ndArray = np.array([1, 2, 3, 4], ndmin=6)
print(ndArray)
print('Dimensions of array:', ndArray.ndim)

three_dimensional_list=[[[1,2,3],[4,5,6],[7,8,9]]]
three_dimensional_arr = np.array(three_dimensional_list)
print("3D array is : \n ",three_dimensional_arr) 

two_dimensional_list=[[1,2,3],[4,5,6]]
two_dimensional_arr = np.array(two_dimensional_list)
print("2D array is : \n ",two_dimensional_arr)

one_dimensional_list = [1,2,4]
one_dimensional_arr = np.array(one_dimensional_list)
print("1D array is : ",one_dimensional_arr) 
#----------------------------------------#
import numpy as np
#inputs
inputArray = np.array([[35,53,63],[72,12,22],[43,84,56]])
new_col = np.array([[20,30,40]])
# delete 2nd column
arr = np.delete(inputArray , 1, axis = 1)
#insert new_col to array
arr = np.insert(arr , 1, new_col, axis = 1)
print (arr) 
#----------------------------------------#
import numpy as np
arr = np.array([[8, 3, 2], [3, 6, 5], [6, 1, 4]])
#sort the array using np.sort
#arr = np.sort(arr.view('i8,i8,i8'), order=['f1'], axis=0).view(np.int)
arr.view('i8,i8,i8').sort(order=['f1'], axis=0)
#----------------------------------------#
'''67. How will you find the nearest value in a given numpy array?
We can use the argmin() method of numpy as shown below:'''

import numpy as np
def find_nearest_value(arr, value):
   arr = np.asarray(arr)
   idx = (np.abs(arr - value)).argmin()
   return arr[idx]
#Driver code
arr = np.array([ 0.21169,  0.61391, 0.6341, 0.0131, 0.16541,  0.5645,  0.5742])
value = 0.52
print(find_nearest_value(arr, value)) # Prints 0.5645
#----------------------------------------#
'''How will you find the shape of any given NumPy array?
We can use the shape attribute of the numpy array to find the shape. It returns the shape of the array in terms of row count and column count of the array.
'''

import numpy as np
arr_two_dim = np.array([("x1","x2", "x3","x4"),
             ("x5","x6", "x7","x8" )])
arr_one_dim = np.array([3,2,4,5,6])
# find and print shape
print("2-D Array Shape: ", arr_two_dim.shape)
print("1-D Array Shape: ", arr_one_dim.shape)
#----------------------------------------#