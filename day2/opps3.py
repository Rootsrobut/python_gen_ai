class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class")

obj = Child()
obj.display()
obj.show()

class Father:
    def skills(self):
        print("Father: knows driving")

class Mother:
    def skills(self):
        print("Mother: knows cooking")

class Child(Father, Mother):
    def talents(self):
        print("Child: knows dancing")

obj = Child()
obj.skills()   # Python uses Method Resolution Order (MRO)
obj.talents()

class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def hello(self):
        print("Hello from Parent")

class Child(Parent):
    def hi(self):
        print("Hello from Child")

obj = Child()
obj.greet()
obj.hello()
obj.hi()


class A:
    def feature1(self):
        print("Feature 1 from A")

class B(A):
    def feature2(self):
        print("Feature 2 from B")

class C:
    def feature3(self):
        print("Feature 3 from C")

class D(B, C):   # Hybrid: D inherits from both B and C
    def feature4(self):
        print("Feature 4 from D")

obj = D()
obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()
