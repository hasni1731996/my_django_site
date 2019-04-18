import pickle
dict1 = {
    'a':200,
    'b':400,
    'c':500
}
list1 = [
    500,800,300
]
print('DIc...',dict1)
print('list...',list1)
output = open("save1.pkl","wb")
pickle.dump(dict1,output,pickle.HIGHEST_PROTOCOL)
pickle.dump(list1,output,pickle.HIGHEST_PROTOCOL)
output.close()
print('---------------------------------------------------')
inputfile = open("save1.pkl","rb")
dict2 = pickle.load(inputfile)
list2 = pickle.load(inputfile)
print('dict2...',dict2)
print('list2....',list2)