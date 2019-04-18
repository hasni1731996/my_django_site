######################## MOVE ALL ZEROS TO RIGHT SIDE OF ARRAY######################
#lis=[0,1,2,3,4,0,0]

# for i in lis:
#     if i == 0:
#         # print ('O is here...')
#         # print ('index of 0', lis.index(0))
#         lis.append(lis.pop(lis.index(0)))
#     else:
#         pass
#         # print ('other numbers')

# print ('actual list:',lis)
####################### ENDS####################################################

####################Floyd Triangle 
# 1
# 2 3
# 4 5 6
# 7 8 9 10
###########
# print("Enter 'x' for exit.")
# ran = input("Upto how many line ? ")
# if ran == 'x':
#     exit()
# else:
    # rang = int(ran)
    # k = 1
    # for i in range(1, rang+1):
    #     for j in range(1, i+1):
    #         print(k, end=" ")
    #         k = k + 1
    #     print()

############ENDS#####################################

#############Generate Sum up to entered number ###########
# user_inpt = input('Enter Number...')
# print('you have entered ...',user_inpt)
# q=0
# for i in range(1,int(user_inpt)):
#     print('i..',i)
#     q +=i
# print('val..',q)
############Ends#############

#############print multiplication table upto 12 ############
# user_inpt = input('Enter Number...')
# print('you have entered ...',user_inpt)
# for i in range(1,13):
#     print(str(i) + '*'+ user_inpt + '=' + str(i*int(user_inpt)))
############Ends################

############Calculating next 20 leap years #############
# res=[]
# year= 2020
# while True:
#     res.append(year)
#     year = year + 4 
#     if len(res) == 20:
#         break
# print('Final..',res)
############Ends##############

###########Reversing List of Numbers #########
# num=[32,45,90,45,87]
# i=1
# while i <= len(num):
    # print (num[len(num)-i])
    # i = i+1
##########Ends###############

######## returns the elements on odd positions in a list.##########
# L=[32,76,90,43,5,7,9]
# index = 0
# sum_list=0
# for i in L:
#     if index % 2 == 1:
#         print(i)
#     index += 1
#     sum_list+=i
# print('SUm...',sum_list)
#########Ends############

##########Check string is palindrome i.g (radar) ######
# user_str=input('Enter String..')
# i=1
# rev_st=''
# print('Yu have entered..',user_str)
# while i<= len(user_str):
#     rev_st +=user_str[len(user_str)-i]
#     i +=1
# print(rev_st)
# if user_str == rev_st:
#     print('Entered String is palindrome')

# else:
#     print('String is not palindrome.')
#########Ends###########

##########Calculating first 20 numbers with their perfect squares ########
# for i in range(1,21):
#     print(str(i) + '*' + str(i) + '=' + str(i*i))
##########Ends###############

############ concatenates two lists ########
# lis1=['a','b','c'] 
# lis2=[1,2,3]
# fin=[]
# for i in lis1,lis2:
#    fin+=i
# print(fin)
###########Ends##########

############ combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3] ####
# lis1= ['a','b','c']
# lis2= [1,2,3]
# res=[]
# i=0
# try:
#     while True:
#         final=str(lis1[i]) + ',' + str(lis2[i])
#         res.append(final) ###we can here use  res+=final but it gives ['a','1','b','2','c','3']
#         i +=1

# except:
#     print('in except')
#     pass
# print(res) ### it gives as ['a,1', 'b,2', 'c,3']
###########Ends #########

#### Gets sorted list by combining two unsorted lists [1,4,6],[2,3,5] → [1,2,3,4,5,6]########
# lis1=[1,4,6]
# lis2=[2,3,5]
# fin=[]
# for i in lis1,lis2:
#     fin+=i
# print('unsorted',fin)
# #j=0 ## Never initialize here because inner loop always need to start from zero index
# for i in range(len(fin)):
#     j=0
#     while j < len(fin)-1:
#         if fin[j] > fin[j+1]:  #### reverse order well by changing > to < it will reverse list
#             fin[j] , fin[j+1] = fin[j+1], fin[j]
#         j +=1
#     print('value of i.',str(j))
# print('final sorted',fin)
#####Ends ##########

#################[1,2,36,44,56,60] rotated by two becomes [3,4,5,6,1,2]#########
# lis_=[1,2,36,44,56,60]
# i=0
# j=0
# lis2=[]
# while i<=len(lis_)-1:
#     if i == 2 or i == 3 or i==4 or i==5 or i==6:
#         lis2.append(lis_[i])
#     i +=1
# while j<=1:
#     print('i 2nd lopp..',j)
#     lis2.append(lis_[j])
#     j+=1
# print(lis2)
################Ends#######################

############ list ["Hello", "World", "in", "a", "frame"] into rectangular form ##########
# lis=["Hello", "World", "in", "a", "frame"]
# lis2=['*','*','*','*','*']
# print('**********************')
# i=0
# try:
#     while True:
#         print(lis2[i] + '  ' + lis[i] + '  ' +lis2[i])
#         i +=1
# except:
#     print('**********************')

##########Ends############

##############Fabnoci Sequence Generation 0,1,1,2,3,5,8,13###########
# user_input=input('ENter length for fabnoci sequence...')
# print('length you have entered is...',user_input)
# a=0
# b=1
# sum_=0
# while a<int(user_input):
#     print(sum_)
#     sum_,b=b,sum_+b
#     a=a+1

#############Ends###########

#########Factorial of number ########
# user_input=input('Enter Number....')
# print('you have entered number..',user_input)
# i=1
# j=1
# total=1
# while i<=int(user_input):
#     if i+1 > int(user_input):
#         break
#     total=total*(i+1)
#     i+=1
# print('Fictorial of number is ...',total)
#########Ends#######

##############Remove duplicates from list #########
# use_list=[5,1,4,1,8,6,1]
# i=0
# les=[]
# while i<=len(use_list)-1:
#     if use_list[i] in les:
#         print('already existed...')
#     else:
#         print('no first tym..')
#         les.append(use_list[i])
#     i+=1
# print('final..',les)
#############Ends#####      ######Starting from right side here the spicified index for element include it self for both list,str -------but from left side slicing specified index element would skip further elemnts will included
lis=[2,8,6,9,4,7,9,3]
str_user='hassan'
print(lis[1:])
print(str_user[1:])
print(lis[1:-4])
print(str_user[1:-4])
