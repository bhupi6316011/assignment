'''Ques 3. Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''


class temperature:


    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit



    def convertfahrenheit(self):
        fahrenheit = (celsius * 2.5) + 48
        print(fahrenheit)


    def convertcelcius(self):
        celsius = (fahrenheit - 48) / 2.5
        print(celsius)


celsius = int(input("enter temperature in celcius: "))
fahrenheit = int(input("enter temperature in fahrenheit: "))

s1 = temperature(celsius, fahrenheit)
s1.convertfahrenheit()
s1.convertcelcius()

