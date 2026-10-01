'''
Type checking

a=10
b=5.6
c="Naidu"
d=[1,2,3,4,5]
e=(1,2,3,4,5)
f={1,2,3,4,5}
g={"name":"Naidu"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#isinstance(): to check the value or object is particular class or datatype

a=10
b=5.6
c="Naidu"
d=[1,2,3,4,5]
e=(1,2,3,4,5)
f={1,2,3,4,5}
g={"name":"Naidu"}
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,set))
print(isinstance(e,set))
print(isinstance(f,tuple))
print(isinstance(g,dict))


#checking multiple values

x="Naidu"
if isinstance(x,(int,float)):
    print("given x is a int or float")
else:
    print("given x is a string")  
'''
'''
class Animal:
    pass
class Dog(Animal):
    pass
class cat:
    pass
d=Dog()
c=cat()
print(isinstance(d,Dog))   
print(isinstance(d,Animal))  

print(isinstance(c,cat))
'''
