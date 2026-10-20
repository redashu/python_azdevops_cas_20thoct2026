# testing variables & data type 
# please do read variable naming rules as home work
user_name =  "Ashu"
age = 30
height = 5.7
print("my name is ",user_name)
print("My age is ",age)
print("my height is ",height , "feet")

# checking data type 

print(type(user_name))
print(type(age))
print(type(height))

# lets explore string storage understanding 

print(user_name[2])
print(user_name[0:3])

print(user_name[-1])
# count len of string 
print(len(user_name))


# define tuple 

city = ("jk","nz","pr")

names = ("as","ok","fine")

mydata = ("hello",1000,5.8,"fine")

print(type(city),type(names),type(mydata))

### dealing with list 

```
>>> l1=["ashu","brand","chris","jas"]
>>> 
>>> len(l1)
4
>>> l1[0]
'ashu'
>>> l1.append(1000)
>>> l1
['ashu', 'brand', 'chris', 'jas', 1000]
>>> l1.insert(0,"python")
>>> l1
['python', 'ashu', 'brand', 'chris', 'jas', 1000]
>>> l1.pop(0)
'python'
>>> l1
['ashu', 'brand', 'chris', 'jas', 1000]
>>> l1.remove('ashu')
>>> l1
['brand', 'chris', 'jas', 1000]

```