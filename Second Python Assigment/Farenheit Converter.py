def FahToCel(f):
    return (f-32)/1.8

def FahToKel(f1):
    return 5 * (f1-32)/9 + 273.15

print("Enter Temperature in Fahrenheit: ", end="")
fah = float(input())

cel = FahToCel(fah)
print("\nEquivalent Temperature in Celsius = {:.2f}".format(cel))

kel = FahToKel(fah)
print("\nEquivalent Temperature in Kelvin = {:.2f}".format(kel))