import pickle, os

#The name of the file where ew will store the object
shoplistfile = 'shoplist.data'
#The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

#Write to the file
f = open(shoplistfile, 'wb')
#Dump the object to a file
pickle.dump(shoplist, f)
f.close()

#Destory the shoplist variable

#Read back from the storage
f = open(shoplistfile, 'rb')
#Load the objct from the file
storedlist = pickle.load(f)
print(storedlist)