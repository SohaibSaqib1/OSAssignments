process = []
dictionary = {}
parameters = []
file = open("temp.txt","r")
line = file.readline()
for word in line.split():
    parameters.append(word)
data = file.readlines()
index = 0
for line in data:
    for word in line.split():
        dictionary[parameters[index]] = word
        index = index+1
    process.append(dictionary.copy())
    index = 0 
import time
process = sorted(process,key = lambda k: k['AT'])
a = 0
print("First Come First Serve")
for dictionary in process:
    if a < int(dictionary["AT"]):
        print(a,end='')
        while a < int(dictionary["AT"]):
            print('.',end='')
            a = a+1;  
        print(a,end = '')
    for i in range(1,int(dictionary["Duration"])+1):
        print("_",end = '')
    print(dictionary["Processes"],end = '')
    print("(",end = '')
    print(int(dictionary["Duration"])+a,end = '')
    a = a+int(dictionary["Duration"])
    print(")",end = '')
    		

        
