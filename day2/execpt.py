try: 
    import time1
    print(4 + 5)
    print(55 + "hello")

except ModuleNotFoundError as m: 
    print("check your module or lib name in import statement ")
    print(f"the error is {m}")
except TypeError: 
    print("check your data type of + operator ")