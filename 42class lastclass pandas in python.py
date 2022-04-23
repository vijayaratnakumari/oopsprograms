import pandas

s=pandas.Series()
print(s)

#int data
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
#s = pd.Series(data,index=[100,101,102,103])
s=pd.Series(data)
print(s)

#float data
import pandas as pd
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

import pandas as pd
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

#slite
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)
print(s['a'])
print (s[:3])

import pandas as pd
df = pd.DataFrame()
print(df)

import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
#print(df.tail(2))
print(df.head(1))

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
#df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
df = pd.DataFrame(data)
print(df)

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print (df2)

import pandas as pd

df1 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df1 = df1.append(df2)
print(df1)

import pandas as pd
import numpy as np
df1 = pd.DataFrame({'name': ['John', 'Smith','Paul'],
                     'Age': ['25', '30', '50']},
                    index=[0, 1, 2])
df2 = pd.DataFrame({'name': ['Adam', 'Smith' ],
                     'Age': ['26', '11']},
                    index=[3, 4])

df_concat = pd.concat([df1,df2])
print(df_concat)

import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
df = df.drop(0)
print(df)

#convert from html into csv
import pandas as pd
a=pd.read_csv("C:/Users/vijay/oopsprograms/durga.html")
a.to_csv('emp.csv')

