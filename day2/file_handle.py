file_name = input("enter file name : ")
# file_content = input("type some data or message to store in file : ")
# # create empty file 
# with open(file_name,'w') as f:
#     f.write(file_content) 
#     f.close()

# reading file 
with open(file_name,'r') as f:
    data=f.read()
    print(data)
    f.close()