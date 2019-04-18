import pickle
from player import Player
items = ["axe", "noon", "gun"]
myobj = Player(1,"hasni",8852.00,items)
print('push data....')
with open("save2.pkl","wb") as outfile:
    pickle.dump(myobj,outfile,pickle.HIGHEST_PROTOCOL)

print('---------------------')
newobj = None
with open('save2.pkl','rb') as infile:
    newobj = pickle.load(infile)

print('reeaaaadddd...',newobj)