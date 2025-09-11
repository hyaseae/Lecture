# Temperature conversion program Fahrenheit->Celsius

# program greeting:
print('This program will convert degrees Fahrenheit to degrees Celsius')

# get temperature in Celsius:
celsius = float(input('Enter degrees Celsius: '))
# convert Celsius to Fahrenheit:
fahren = (celsius * 9 / 5) + 32

# print result:
print(celsius, 'degrees Celsius equals',
      format(fahren, '.1f'), 'degrees Fahrenheit')