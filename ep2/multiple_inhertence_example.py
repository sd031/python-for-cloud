# Multiple Inheritence example

class SapleBase1:
    pass

class SampleBase2:
    pass

class MultiInheritenceExample(SapleBase1, SampleBase2):
    pass

multipleInheritenceObject = MultiInheritenceExample()

print(multipleInheritenceObject.__class__.__bases__)

#multi level inheritence

class Level1:
    pass

class Level2(Level1):
    pass

class MultipleLevel(Level2):
    pass
multiLevelInheritenceObject = MultipleLevel()
print(MultipleLevel.__mro__)
print(MultipleLevel.__bases__)



