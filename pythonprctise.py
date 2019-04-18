#########################################start########################
def add(*args):
    return sum(args)

print (add(4,5,6,7))

def multiargu(**kwargs):
    print( kwargs)

multiargu(name="hassan",age="75",gender="Male")
#
def combineconcepts(first_arg,*args,**kwargs):
    print(first_arg,args,kwargs)

combineconcepts('TESTFIRST_ARGUMENT','FIRST_POSITIONALARGUMENT','SECONDARGUMENT','THIRDARGUMENT',name="Muhammad Hassan",profession="Django Developer",product="ChoiceGenie")

#########################################ends########################

#########################################start########################

import dateutil.parser
import datetime
from pytz import utc
date_time1 ='2017-04-15 00:00:00'
date_time2='2017-04-17 15:35:19+00:00'
date_time3='2017-04-16 12:11:42+00:00'

#parsed1 = dateutil.parser.parse(date_time1).astimezone(utc)
parsed2 = dateutil.parser.parse(date_time2)
parsed3 = dateutil.parser.parse(date_time3)
#input_parsed = dateutil.parser.parse(input_date_time)

if parsed2 > parsed3:
    print('parsed2 is grater')
else:
    print('parsed3 is lesser')

#########################################ends########################

list = [5,5,9]
for i in enumerate (list):
    print('i values..',i)

# Program to multiply two matrices using nested loops
#
# take a 3x3 matrix
A = [
     [12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]
print('length...',len(A))
# take a 3x4 matrix
B = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]
print('length...',len(B))
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterating by row of A
for i in range(len(A)):

    # iterating by coloum by B
    for j in range(len(B[0])):

        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)