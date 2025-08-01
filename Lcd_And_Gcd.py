number1=int(input("Enter a number: "))
number2=int(input("Enter a number: "))
smallest=min(number1,number2)
biggest=max(number1,number2)
for i in range(smallest,0,-1):
    if ( biggest%i==0 and smallest%i==0):
        gcd=i
        break
lcm=int((number1*number2)/gcd)

print(f"The GCD of {number1} and {number2} is {gcd}")
print(f"The LCM of {number1} and {number2} is {lcm} ")