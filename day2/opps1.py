class Test:
    x = "S"  # class variable

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a, self.b)

    @staticmethod
    def f2():
        print("Hello")

    @classmethod
    def f3(cls):
        print(cls.x)


# Create objects
t1 = Test(3, 4)
t2 = Test(5, 6)

# Call instance methods
t1.show()
t2.show()

# Call static and class methods
Test.f2()
Test.f3()
