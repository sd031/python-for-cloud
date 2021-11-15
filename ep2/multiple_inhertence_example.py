# Multiple Inheritence example

# class SapleBase1:
#     def sampleBase1Function(self):
#         print("Sample Base 1 Function")

# class SampleBase2:
#     def sampleBase2Function(self):
#         print("Sample Base 2 Function")

# class MultiInheritenceExample(SapleBase1, SampleBase2):
#     pass

# multipleInheritenceObject = MultiInheritenceExample()
# multipleInheritenceObject.sampleBase1Function()
# multipleInheritenceObject.sampleBase2Function()

# print(multipleInheritenceObject.__class__.__bases__)

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



