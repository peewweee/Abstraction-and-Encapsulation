# Designing a class named Fan to represent a fan
# Phoebe Rhone L. Gangoso | BSCpE 1-4

# PSEUDOCODE
# import class fan
from fan_class import Fan

# create class TestFan
class TestFan:
    def run_test(self):
        # two Fan objects
        fan_1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan_2 = Fan(Fan.MEDIUM, 5, 'blue', False)

        # print fan1
        print("Fan 1:")
        print("Speed:", fan_1.get_speed())
        print("Radius:", fan_1.get_radius())
        print("Color:", fan_1.get_color())
        print("On:", fan_1.is_on())

        # print fan2
        print("Fan 2:")
        print("Speed:", fan_2.get_speed())
        print("Radius:", fan_2.get_radius())
        print("Color:", fan_2.get_color())
        print("On:", fan_2.is_on())

# instance of TestFan and run the test
test = TestFan()
test.run_test()