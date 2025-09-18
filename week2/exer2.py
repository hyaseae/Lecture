"""using copilot for making a big structure."""


class Temperature:
    """A class that represents a tremperature."""
    unit = "Celsius"
    
    def __init__(self, value):
        """initailizng a value."""
        # I... just started to believe that theere is type issues from now and on.
        self.value = value

    def display(self):
        """print a temperature."""
        print(str(self.value) + " " + self.unit)
        
    @classmethod
    def change_unit(cls, new_unit):
        """changing the unit of temperature."""
        cls.unit = new_unit
    
    @staticmethod
    def to_fahrenheit(temperature):
        """convert celsius to fahrenheit."""
        # maybe can reuse code from CS101?
        # fahren = (celsius * 9 / 5) + 32 <copied from CS 101's lab2 XD
        return (temperature * 9 / 5) + 32
    

t1 = Temperature(100)

f_100 = Temperature.to_fahrenheit(100)

print(f_100)

t2 = Temperature(25)

Temperature.change_unit("kelvin")

t1.display()
t2.display()

# D. because, it is an class method. so it change the class variable unit, and since it is class variable, any other
# class function looking at unit will be affected.
