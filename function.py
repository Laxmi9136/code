#lambda ,map , filter,reduce
            #lambda
"""cube=lambda n:n*n*n
print(cube(4))"""
"""
add=lambda a,b: a+b
print(add(10,20))
"""
"""
add=lambda a,b: a+b
fun=add(10,20)
"""
            #map
"""
li=[x for x in range(1,11)]
li=list(map(lambda x: x*x,li))
print(li)
"""

#write a program  to find factorial of all number of list.
"""
li=[1,2,3,4,5]
def fact(num):
     f=1
     if num!=0:
         for i in range(1,num+1):
             f=f*i
         return f
     else:
        return 1
li=list(map(fact,li))
print(li)
        """

         #filter
"""
li=[x for x in range(1,31)]
print(li)"""


#even number
"""
li=[x for x in range(1,31)]
li=list(filter(lambda n:n%2==0,li))
print(li)"""

#WAP to find only palindrome string using filter.
"""
li=['RAM','NAMAN','MADAM','RIYA','ANU','MAM','SIYA']
li=list(filter(lambda n:n==n[ : :-1],li))   
print(li)
"""
#WAP TO FIND MODE.
"""
li=[1,2,3,1,2,3,5,6]
li2=[]
dic=dict()

for i in li:
    dic.update({i:li.count(i)})
    
for i in dic:
    if dic[i]==max(dic.values()):
        li2.append(i)
   
print(li2)"""
   
        #reduce
from functools import reduce
li=[x for x in range(1,11)]
s=reduce(lambda a,b: a+b,li)
print(s)









    
    



