# Hacer Akıncı
# 150200007

rationalNum = float( input("Enter the rational number (Use '.' for decimal point): "))

sign = ""
if rationalNum < 0:
    sign += '-'
    rationalNum *= -1

fractional = rationalNum % 1
integral = rationalNum - fractional


binary_integral = ""
binary_fractional = ""

i = 0 # to prevent overflow for 23 bit

# To find binary form of integral part

while integral > 0:
    if integral % 2 == 1:
        binary_integral = "1" + binary_integral 
    else:
        binary_integral = "0" + binary_integral
    integral //= 2
    i += 1

if binary_integral.__len__() == 0:
    binary_integral = "0"


# To find binary form of fractional part

while fractional != 0 and i < 23:
    if fractional < 0.5:
        binary_fractional += '0'
        fractional *=2
    else:
        binary_fractional += '1'
        fractional = (fractional * 2) - 1
    i += 1
    
final = sign

if binary_fractional.__len__() != 0:
    final += binary_integral + '.' + binary_fractional 
else:
    final += binary_integral

print(final)
 
