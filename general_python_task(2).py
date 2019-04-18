##########Getting prime numbers before the input Numbers######################
# user_numer = input("Enter Number.")
# lis=[]
# print('you have enter',user_numer)
# for i in range(1,int(user_numer)):
#     if (i % 2)== 0:
#         pass
#         #print('no prime..')
#     else:
#         lis.append(i)
# print('final',lis)

####################ENDS##################


###############Replace space in give string with '%20'#################
# user_string =input('Enter String Here..')
# print('u have entered string',user_string)
# res=''
# for i in user_string:
#     if i ==' ':
#         #print('Space here')
#         i='%20'
#     else:
#         #print('no space here')
#         pass
#     res +=i
#     print('value res...',res)
# print('new string..',res)

###############ENDS###############################

###########Sort numbers from list ###################

#repeating loop len(a)(number of elements) number of times
# a = [16, 19, 25, 15, 10, 50, 75]
# for j in range(len(a)):
#     i = 0
#     while i<len(a)-1:
#         #comparing the adjacent elements
#         if a[i]>a[i+1]:
#             #swapping
#             a[i],a[i+1] = a[i+1],a[i]
#         i = i+1
   
# print (a)
##########Ends#######################

############Reverse string #########
# string_user ='hassan'
# i=1
# while i <= len(string_user):
    # print (string_user[len(string_user)-i])
    # i = i + 1
############Ends###################

############Find Largest & Smallest number from list########
# lis=[5,7,1,2,15,10,6]
# for j in range(len(lis)):
#     i=0
#     while i < len(lis)-1:
#         if lis[i] > lis[i+1]:
#             lis[i], lis[i+1] = lis[i+1] , lis[i]
#         i = i+1
# print('Sorted List...',lis)
# print ('Gratest Number In List',lis[len(lis)-1])
# print('Smallest Number in list..',lis[0])
###########ENDS##############

#################Write function that translates a text to Pig Latin and back. English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay###########
user_str="The quick brown fox"
lis_str=[]
a=''
for i in user_str:
    if i == ' ':
       lis_str.append(a)
       a=''
    else:
        a+=i
lis_str.append(a) ##This lopp will works for the last index of list to append the last append last assigned value of a into list
print(lis_str)
i=0
k=0
elem=0
while i<= len(lis_str)-1:
    #print(len(lis_str[i]))
    #print('1 ch from i',lis_str[i][1],'2nd ch from i',lis_str[i][2])
    while k <=len(lis_str[i])-1:
        print('word',lis_str[i])
        # print(type(lis_str[i]))
        #if k == len(lis_str[i]):
        # print('value of elem..',elem)
        # print('1st Elment from str',lis_str[k][0],'2nd element from str..',lis_str[k][1])
        print('print from loop',lis_str[k][elem])
        #exit()
        elem+=1
        k+=1
        
    i+=1
    #break
#print(a)