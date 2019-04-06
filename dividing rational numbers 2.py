'''Given a list of rational numbers,find their product in reduced form.'''
import math
a=int(input("Enter the number of numerators and denominator"))
list_for_num=[]
list_for_denom=[]
new_num=1
new_denom=1
for i in range(0,a):
    x=int(input("Enter number of list elements"))
    list_for_num.append(x)
print(list_for_num)
for j in range(0,a):
    y=int(input("Enter number of list elements"))
    list_for_denom.append(y)
print(list_for_denom)
for i in range(0,a):
    new_num=new_num*list_for_num[i]
print(new_num)
for j in range(0,a):
    new_denom=new_denom*list_for_denom[j]
print(new_denom)
GCD=math.gcd(new_num,new_denom)
print(GCD)
final_num=new_num//GCD
final_denom=new_denom//GCD
print(final_num,end=' ')
print(final_denom)



            

                                
            
