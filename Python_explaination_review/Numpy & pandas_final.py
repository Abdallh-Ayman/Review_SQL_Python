''' numpy library
it is array with same data type
it locate in same place in the memory unlike list
so it is so fast compare to list and take less size than list
'''
import pandas as pd
import numpy as np
import time
import sys
# a = np.array(10)           #zero Dimensions
# b = np.array([10, 20])     #one Dimensions
# c = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])                        #two Dimensions
# d = np.array( [ [ [5, 6], [7, 9] ], [ [1, 3], [4, 8] ] ] )  #three diemensions
# print(d[1][1][-1])
# print(d[1, 1, 1])
# print(c[1])
# print(c[2:, :2])       #2:=> it is rows :2=> it column
# print(c[2:, :2:2])   #step 2
# print(d.ndim)     #to know number of Dimensions
# y =np.delete(c,0,axis= 0)    #axis zero=> to select rows
# w =np.delete(c,[0,2],axis= 1) #axis one=> is used to select columns
# x= np.append(c,[[30,40,10]],axis=0) #it will append new row
# print(np.append(c,[[50],[60],[10],[20]],axis=1)) #can append 2 dimention not 1 dim must append by the same shape (size) of the array
# z= c[1:,2:].copy() #we make new array if we make change to z it didn't change in c
#
# print("#" * 50)
# # Custom Dimensions
# my_custom_array = np.array([1, 2, 3], ndmin=3)
# print(my_custom_array)
# print(my_custom_array.ndim)
# print(my_custom_array[0, 0, 0])    #output => 1
#
# print("#" * 50)
# # adding two list vs two array
# elements = 150000
# my_list1 = range(elements)
# my_list2 = range(elements)
# list_start = time.time()
# list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
# #print(list_result)
# #print(f"List Time: {time.time() - list_start}")
#
# my_array1 = np.arange(elements) #from 0 to 150000
# my_array2 = np.arange(elements)
# #my_array3 =np.linespace(0,25,10) # we use it if we want steps is not integer ,10 => number of array
# array_start = time.time()
# array_result = my_array1 + my_array2
# #print(array_result)
# #
# print("#" * 50)
# # Create Array With Specific Data Type
# my_array4 = np.array([1, 2, 3], dtype=float) # float Or 'float' Or 'f'
# my_array5 = np.array([1.5, 20.15, 3.601], dtype=int) # int Or 'int' Or 'i'
# # my_array6 = np.array(["Osama_Elzero", "B", "Ahmed"], dtype=int) # Value Error
# print(my_array4.dtype)
# print(my_array5.dtype)
# print(my_array5.min())
# print(my_array5.argmin()) # give index of min
# print(my_array5.max())
# print(my_array5.argmax()) # give index of max
# print(my_array5.sum())
# # print(my_array6.dtype)
#
# print("#" * 50)
# # Change Data Type Of Existing Array
# my_array7 = np.array([0, 1, 2, 3, 0, 4])
# my_array7 = my_array7.astype('float')
# print(my_array7.dtype)
#
# print('#' * 50)
# # Ravel => make it one Dimensions
# my_array8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(my_array8.ndim)
# print(my_array8.ravel().ndim)
#
# print('#' * 50)
# #shape=> it give the size of array (rows ,column)
# my_array3 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])
# print(my_array3.ndim)
# print(my_array3.shape)
#
# arr = [1,2]
# print(np.repeat(arr,2)) # to create array  op => [1 1 2 2]
#
# print("#" * 50)
# #reshape=> it reshape the our array (rows ,column)
# my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(my_array4.ndim)
# print(my_array4.shape)
# reshaped_array4 = my_array4.reshape(3, 4)
# print(reshaped_array4.ndim)
# print(reshaped_array4.shape)
# print(reshaped_array4)
# print(np.arrange(20).reshape(10,2))
# print("#" * 50)
#
# #can save array to use it later
# x = np.array([1,2,3,4,5])
# np.save('my_array',x)
# y= np.load('my_array.npy')
# print(y)
#
#
# zeroo = np.zeros((3,4),dtype=int)
# onee = np.ones((3,4),dtype=int)
# digonal_1= np.eye(5) # Digonal of 1.
# digonal_any = np.diag([10,20,30,50])
# #print(np.diag(d)) #it will give me the diag of this array
# onee = np.full((3,4),5) # 5 => contant you want to fill array with
# rondom_array = np.random.random((3,3)) #make random array from 1 to 0
# rondom_array_int = np.random.randint(4,15,(3,3)) #4=> lower 15=> upper (3,3)=> its shape
# rondom_array_with_spacificstatistic =np.random.normal(0,0.1,size=(100,100))#it will give array with mean =0  and standard deviation of 0.1
# print(np.unique(d)) #it will give the unique value of array
#
# print("#*" * 50)
# arrayy = np.arrange(25).reshape(5,5)
# print(x[x<=7])  #if we didn't know the place of element
# print(x[(x>10)&(x<17)]=-1) # make all value with this condition =-1
# print("#*" * 50)


#----------------------------------------------------------------------------------------------------------


# ''' pandas library
# it is data structure like dictionaray we can reach to element using its value[0] or index  not same data type as np
# pandas series => it is one dimentional data structure with only label row
# pandas dataframe => it is two dimentional data structure like spreadsheet with label row(index) and column
# '''
# Series

import pandas as pd


# l = np.random.randint(-10,11,size=8)
#ss=pd.Series(l,index = ['01','02','03','04','05','06','07','08'])
# ss.index # it will give the index label
# ss.values # it will give the data
#print('01' in ss) # output -> true
# ss[['01','02']] ; ss[[0,1]] # it will access first two row
# ss.drop('03', inplace = 'true')  # inplace to edit the original Series
# print(ss)

# print("#" * 50)
#pandas dataframe

#1. Using a Dictionary:
#   You can create a DataFrame directly from a dictionary where the keys represent the column names and the values represent the data
# in each column.
# data_dict = {'Name': ['John', 'Anna', 'Peter'],
#                 'Age': [25, 30, 35],
#                 'City': ['New York', 'Paris', 'Tokyo']}
# df_dict = pd.DataFrame(data_dict)
# print(df_dict)
    


# 2. Using a 2D Array:
#     You can create a DataFrame from a 2D array. Each row in the array represents a row in the DataFrame, and the columns are inferred
# from the dimensions of the array.
# data_array = np.array([[1, 2, 3],
#                         [4, 5, 6],
#                         [7, 8, 9]])
# df_array = pd.DataFrame(data_array, columns=['A', 'B', 'C'])
# print(df_array)

# 3. Using a List of Lists:
#     Similar to a 2D array, you can create a DataFrame from a list of lists. Each inner list represents a row in the DataFrame.
# data_lists = [['John', 25, 'New York'],
#                 ['Anna', 30, 'Paris'],
#                 ['Peter', 35, 'Tokyo']]
# df_lists = pd.DataFrame(data_lists, columns=['Name', 'Age', 'City'])
# print(df_lists)
        
# Another example:
# items = {'Bob':pd.Series([245,25,55],index =['bike','pants','watch']),
#         'Alice': pd.Series([40,110,500,45],index = ['book','glasses','bike','pants'])}
# shoping_carts = pd.DataFrame(items,columns = ['Alice','Bob'])
# print(shoping_carts)

# alice_cell = pd.DataFrame(items,index=['glasses','bike'],columns=['Alice']) # it find elements in this selected row(index) and column (filter)
# print(alice_cell)
#print(shoping_carts.loc[['glasses','bike']])  #we should write row first then column (label)
# print(shoping_carts.loc[['glasses','bike'], ['Bob']]) # Access element using loc
# print(shoping_carts.loc[:, 'Bob'])
# print(shoping_carts['Bob']['bike'])    #when we access element we should write column first and then row
# shoping_carts['bedo']= shoping_carts['Bob']+shoping_carts['Alice']   #to add column
# print(shoping_carts)
# new_items= {'Bob':25,'Alice':40}
# print(new_items)
# new_person = pd.DataFrame(new_items,index = ['ahmed'])
# print(new_person)
#print(shoping_carts.append(new_person)) # to add rows or new DataFrame as rows , it did not edit the origion dataframe
#print(shoping_carts.drop(['ahmed'],axis=0)) # to delete row ahmed
# shoping_carts.insert(1,'salah',[48,60,3,5,6]) # to add new column
# shoping_carts.insert(0,'abd',[48,60,9,8,6])
# print(shoping_carts)
#shoping_carts =shoping_carts.rename(columns = {'Bob':'bob'}) # to rename column
# shoping_carts =shoping_carts.rename(index = {'watch':'WATCH'}) # to rename rows
# shoping_carts = shoping_carts.set_index('Bob') # to make any column as index of our dataframe
# print(shoping_carts)
# shoping_carts.sort_index() # to sort our index alphabetically

# print("#" * 50)
# # import files and manipulate it
# df_csv = pd.read_csv('annual-enterprise-survey-2021-financial-year-provisional-csv.csv')
# print(df_csv)
# df_excel = pd.read_excel('file_example_XLSX_100.xlsx')
# print(df_excel)
# print(df_csv.info)
# print(df_csv.loc[0,'Value']) # it find element acording its name-- 0=> row,'value'=>column- if we wnat not continous list of row we but it in list[1,4], but if continous we didn't need[]> 1:3
# #print(df_csv.loc[df_csv[' Value']>6000 , :])
# print(df_csv.iloc[0,0]) # it find element acording its index we should write row first then column
# print(df_csv.columns.get_loc('Value'))  # to know the index number of this column
# print(df_excel['Age']> 25)
# print(df_excel[df_excel['Age']> 25]) #it will show all values above 25 only
#
# print("#" * 50)
# #important function helps
# df_csv.info()
# print(df_csv.head())
# print(df_csv.columns)
# print(df_csv.describe()) #it will give all statstic value
#  print(df_csv.describe(include = "all")) #it will give all statstic value and give me unique , freq , top
# print("#" * 50)
# cleaning data
# df = pd.read_csv('product_view_data.csv')

#----------------------------------------------------------------------------------------

# dog = {
#     'name': ['Bella', 'Charlie', 'Lucy', 'Cooper', 'Bella', 'Stella', 'Bernie','Bernie'],
#     'breed': ['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador', 'Chihuahua', 'St. Bernard','St. Bernard'],
#     'color': ['Brown', 'Black', 'Brown', 'Gray', 'Black', 'Tan', 'White','White'],
#     'height_cm': [56, 43, 46, 49, 59, 18, 77,77],
#     'weight_kg': [24, 24, 24, 17, 29, 2, 74,74],
#     'date_of_birth': ['2013-07-01', '2016-09-16', '2014-08-25', '2011-12-11', '2017-01-20', '2015-04-20', '2018-02-27','2018-02-27']
# }

# dogs = pd.DataFrame(dog)
# print(dogs)
#                                         # Exploring a DataFrame
# print(dogs.head())
# print(dogs.shape)
# print(dogs.info())
# print(dogs.describe())
# print(dogs.values)
# print(dogs.columns)
# print(dogs.index)

                                      # Sorting and subsetting
# dogs.sort_values("weight_kg")
# dogs.sort_values("weight_kg", ascending=False)
# dogs.sort_values(["weight_kg","height_cm"]) -- Sorting by multiple variables
# dogs.sort_values(["weight_kg","height_cm"] , ascending=[False, True])
 
                                
                                      # Subsetting columns
# dogs["name"]    -- subset one column

# dogs[["breed","height_cm"]]     -- subset multiple columns
# cols_to_subset = ["breed","height_cm"]
# dogs[cols_to_subset]

# dogs["height_cm"] > 50    -- subset row (true , false)
# dogs[dogs["height_cm"] > 50] -- subset row with values

# dogs[dogs["breed"] == "Labrador"]  -- filter based on one condition
# dogs[dogs["date_of_birth"] < "2015-01-01"]  -- filter based on one condition

# is_lab = dogs["breed"] == "Labrador" -- filter based on multiple condition
# is_brown = dogs["color"] == "Brown"
# dogs[is_lab & is_brown]
# dogs[ (dogs["breed"] == "Labrador") & (dogs["color"] == "Brown") ]

# is_black_or_brown = dogs["color"].isin(["Black","Brown"])   -- Subsetting using .isin()
# dogs[is_black_or_brown]
# dogs[dogs["name"].isin(["Bella","Stella"])]

#dogs["height_m"] = dogs["height_cm"] / 100  -- Adding a new column
# print(dogs)


                                    # Summary statistics
# dogs["height_cm"].mean()
# dogs["date_of_birth"].min()
# dogs["date_of_birth"].max()
# def pct30(column):
     #return column.quantile(0.3)
# dogs["weight_kg"].agg(pct30)
# dogs[["weight_kg","height_cm"]].agg(pct30)

# def pct40(column):
# return column.quantile(0.4)
# dogs["weight_kg"].agg([pct30, pct40])

# dogs["weight_kg"].cumsum()
# dogs["weight_kg"].cummin()
# dogs["weight_kg"].cummax()

# print(sum(dogs.duplicated()))
# dogs.drop_duplicates(inplace= True) # to remove all duplicated values
# dogs.drop_duplicates(subset="name")
# unique_dogs = dogs.drop_duplicates(subset=["name","breed"]) # it remove the duplicate if the name and breed value is similar 
# print(unique_dogs)

# print(unique_dogs["breed"].value_counts())  # count each value in the category data
# unique_dogs["breed"].value_counts(sort=True)
# print(unique_dogs["breed"].value_counts(normalize=True))

#print(dogs[dogs["color"] == "Black"]["weight_kg"].mean())
# dogs[dogs["color"] == "Brown"]["weight_kg"].mean()
# dogs[dogs["color"] == "White"]["weight_kg"].mean()
# dogs[dogs["color"] == "Gray"]["weight_kg"].mean()
# dogs[dogs["color"] == "Tan"]["weight_kg"].mean()
              # OR
# print(dogs.groupby("color")["weight_kg"].mean().loc["Black"])
# result = dogs.groupby(dogs['color'] == 'Black')['weight_kg'].mean()
# print(result)
# print(dogs.groupby("color")["weight_kg"].agg([min, max, sum]))
# dogs.groupby(["color","breed"])["weight_kg"].mean()
# dogs.groupby(["color","breed"])[["weight_kg","height_cm"]].mean()  -- Many groups, many summaries
# print(pd.cut(df['view_duration'],bin =2,labels =('first','second')))    #it will divide view_duration to 2 group ( partition by )                                                      # if there is lots of different in categories


# dogs.groupby("color")["weight_kg"].mean()  -- Group by to pivot table
#print(dogs.pivot_table(values="weight_kg",index="color"))
#print(dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.mean, np.median]) ) #-- Multiple statistics
#ddd=dogs.pivot_table(values="weight_kg", index="color", columns="breed" , fill_value=0 , margins=True)
# print(ddd)
#print(dogs.loc["Chow Chow":"Poodle"])
# print(ddd.mean(axis="index"))
# print(ddd.mean(axis="columns"))



# dogs_ind = dogs.set_index("name") # Setting a column as the index
# print(dogs_ind)
# dogs_ind2 = dogs.set_index("breed")  -- Index values don't need to be unique
# print(dogs_ind2)
# dogs_ind3 = dogs.set_index(["breed","color"])  #-- Multi-level indexes
# print(dogs_ind3)
# dogs_ind.reset_index()  -- Removing an index
# dogs_ind.reset_index(drop=True) -- Dropping an index
# dogs_ind3.sort_index()  -- Sorting by index values
# dogs_ind3.sort_index(level=["color","breed"], ascending=[True, False]) -- Controlling sort_index
# dogs_srt = dogs.set_index(["breed","color"]).sort_index()
# print(dogs_srt)


# breeds = ["Labrador","Poodle","Chow Chow","Schnauzer","Labrador","Chihuahua","St. Bernard"]
# breeds[2:5]
# breeds[:3]
# breeds[:]

# print(dogs_ind.loc[["Bella","Stella"]])
# print(dogs_ind3.loc[["Labrador","Chihuahua"]] ) # -- Subset the outer level with a list
# print(dogs_ind3.loc[[("Labrador","Brown"), ("Chihuahua","Tan")]])  #Subset inner levels with a list of tuples
# print(dogs_srt.loc["Chow Chow":"Poodle"]) #  Slicing the outer index
# print(dogs_srt.loc[("Labrador","Brown"):("Schnauzer","Grey")]) # -- Slicing the inner index
# print(dogs_srt.loc[:,"name":"height_cm"]) # -- Slicing columns
# print(dogs_srt.loc[("Labrador","Brown"):("Schnauzer","Grey"),"name":"height_cm"])
# print(dogs.iloc[2:5, 1:4])


# dogs.isna() -- Detecting missing values
# dogs.isna().any()
# dogs.isna().sum()
# print(df.isnull().sum().sum())  #to sum the null value
# dogs.dropna()
# print(dogs.dropna(axis=0)) # to delete any row with null values
# print(dogs.dropna(axis=1,inplace = 'true')) # to delete any column with null values
# dogs.fillna(0) # to replace null values
# print(df.fillna(mean,inplace = true)) # to replace all null value with mean
# print(df.fillna(method = 'ffill',axis =0)) # null will take its value from bervious row value
# print(df.fillna(method = 'ffill',axis =1)) # null will take its value from bervious column value

# print(df.count()) #to count data in each column
# df['timestamp']= pd.to_datetime(df['timestamp']) # this for data type cleaning



# census = {
#     'ward': [1, 2, 3, 4, 5],
#     'alderman': ['Proco "Joe"', 'Brian Hopkins', 'Pat Dowell', 'William D. Burns', 'Leslie A. Hairston'],
#     'address': ['2058 NORTH W...', '1400 NORTH ...', '5046 SOUTH S...', '435 EAST 35T...', '2325 EAST 71...'],
#     'zip': [60647, 60622, 60609, 60616, 60649]
# }
# census = pd.DataFrame(census)

# wards= {
#     'ward': [1, 2, 3, 4, 5],
#     'pop_2000': [52951, 54361, 40385, 51953, 55302],
#     'pop_2010': [56149, 55805, 53039, 54589, 51455],
#     'change': ['6%', '3%', '31%', '5%', '-7%'],
#     'address': ['2765 WEST SA...', 'WM WASTE MAN...', '17 EAST 38TH...', '31ST ST HARB...', 'JACKSON PARK...'],
#     'zip': [60647, 60622, 60653, 60653, 60637]
# }
# wards = pd.DataFrame(wards)

# wards_census = wards.merge(census, on='ward') # inner join
# print(wards_census.head(4))
# print(wards_census.shape)
# print(wards_census.columns)
# wards_census = wards.merge(census, on='ward', suffixes=('_ward','_cen'))
# print(wards_census)
# wards_census = wards.merge(census, on='ward', how='left', suffixes=('_ward','_cen'))
# print(wards_census)
# print(wards_census.shape)



# inv_jan = {
#     'iid': [1, 2, 3],
#     'cid': [2, 4, 8],
#     'invoice': [None, None, None],  # Replace None with actual invoice values
#     'date': ['2009-01-01', '2009-01-02', '2009-01-03'],
#     'total': [1.98, 3.96, 5.94]
# }
# inv_jan = pd.DataFrame(inv_jan)


# inv_feb = {
#     'iid': [7, 8, 9],
#     'cid': [38, 40, 42],
#     'invoice': [None, None, None],  # Replace None with actual invoice values
#     'date': ['2009-02-01', '2009-02-01', '2009-02-02'],
#     'total': [1.98, 1.98, 3.96]
# }
# inv_feb = pd.DataFrame(inv_feb)

# result =pd.concat([inv_jan, inv_feb]) # two table must be the same columns
# print(result)
# result =pd.concat([inv_jan, inv_feb],ignore_index=True)
# print(result)
# result =pd.concat([inv_jan, inv_feb],ignore_index=False,keys=['jan','feb'])
# print(result)
# result =pd.concat([inv_jan, inv_feb],sort=True)
# print(result)

                             # Append
# www =inv_jan.append([inv_feb],ignore_index=True,sort=True)
# print(www)


                         # Why verify integrity : Real world data is often not clean 
                         # and what to do : Fix incorrect data - Drop duplicate rows

# wards_census = wards.merge(census, on='ward', validate='one_to_many')
# print(wards_census)
# wards_census = wards.merge(census, on='ward', validate='one_to_one')
# print(wards_census)

# result =pd.concat([inv_jan, inv_feb],verify_integrity=True) # Indexes have overlapping values
# print(result)
# result =pd.concat([inv_jan, inv_feb],verify_integrity=False) 
# print(result)



                                        # The .query() method
# stocks= pd.DataFrame({
#     'date': ['2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01', '2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01'],
#     'disney': [143.009995, 137.259995, 130.320007, 129.919998, 151.580002, 144.630005, 138.309998, 117.650002, 96.599998, 99.580002],
#     'nike': [86.029999, 84.5, 93.919998, 89.550003, 93.489998, 101.309998, 96.300003, 89.379997, 82.739998, 84.629997]
# })
# print(stocks.query('nike >= 90'))
# stocks.query('nike > 90 and disney < 140')
# stocks.query('nike > 96 or disney < 98')


# stocks_long = pd.DataFrame({
#     'date': ['2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01'],
#     'stock': ['disney', 'disney', 'disney', 'disney', 'disney', 'nike', 'nike', 'nike', 'nike', 'nike'],
#     'close': [143.009995, 137.259995, 130.320007, 129.919998, 151.580002, 86.029999, 84.5, 93.919998, 89.550003, 93.489998]
# })
# print(stocks_long.query('stock=="disney" or (stock=="nike" and close < 90)'))