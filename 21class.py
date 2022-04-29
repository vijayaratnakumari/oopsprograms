#instance variables

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def m1(self):  #How to delete instance variables
        del self.a  #inside the class



t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
t1.m1() #inside the class calls by using object
del t2.b #outside the class
t1.c=99 #change the value
print(t1.__dict__)
print(t2.__dict__)

#static variables(class level variables)

class Test1:
    a=10 #static or class level variables
    def __init__(self):
        self.b=20 #instance variable

t1=Test1()
t2=Test1()
print("t1:", t1.a,t2.b)
print("t2:", t1.a, t2.b)
t2.b=66
Test1.a =88
print("t1:", t1.a,t2.b)
print("t2:", t1.a, t2.b)

#Local variables (method level)

class Test2:
    a=20 #static variable or class level variable
    def m1(self):
        self.a=10 #instance variale
        print(self.a)
        #a=10 #local variable
        #print(a)
    def m2(self):
        b=20
        print(b)
t=Test2()
t.m1()
t.m2()

#methods
#instance methods

class Student:
    def __init__(self, m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        return (self.m1+self.m2+self.m3)/3
s1=Student(67,84,78)
s2=Student(58,45,87)
print(s1.average())
print(s2.average())

#classmethod
class Student1:
    institution ="Durga Soft"
    def __init__(self, m1, m2, m3):
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3

    def average(self):
         print ((self.m1 + self.m2 + self.m3) / 3)

    @classmethod
    def m1(cls):
        print(cls.institution)

s1 = Student1(67, 84, 78)
s2 = Student1(58, 45, 87)
s1.average()
s2.average()
Student1.m1()

#static method
class Student2:
    institution ="Durga Soft"
    def __init__(self, m1, m2, m3):
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3

    def average(self):
         print ((self.m1 + self.m2 + self.m3) / 3)

    @classmethod
    def m1(cls):
        print(cls.institution)
    @staticmethod
    def add(a,b):
        print("sum is:", a+b)
    @staticmethod
    def f1():
        print("hello")

s1 = Student2(67, 84, 78)
s2 = Student2(58, 45, 87)
s1.average()
s2.average()
Student2.m1()
s1.add(20,34)
s1.f1()