class ClassA:
    def hi(self):
        print('Hey A')


class ClassB:
    def hi(self):
        print('Hey B')

    def another(self):
        print('In class B')

# class C inherits from A and B

class ClassC(ClassA, ClassB):
    pass


c = ClassC()
c.hi()
# will search the first occurence of this method and returns it
