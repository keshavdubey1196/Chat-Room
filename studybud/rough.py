class Hello(Exception):
     def __init__(this, arg):
         this.message= arg+ "was not allowed in python!"


class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def multiplication(self,a,b):
        a=a*b
        raise Hello("Multiplication")
        return a
    
    def divison(self,a,b):
        a=a//b
        raise Hello("Divison")
        return a

obj =A(5, 75)

try:
  print(obj.multiplication(4,6))
except Hello as h:
    print(h)


"""def square (n):
    return n*n

def cube(n):
    return n*n*n

list1=[1,2,3]
s1=list(map(cube, list1))

s2=list(map(square,s1))
s3=[]
for i in s2:
    if i%2==0:
      s3.append(i)
    else:
      s3.append(i+1)

s3.extend(['hello',"",[]])

s4=list(filter(bool,s3))
print(s4)"""