number=int(input("Enter a number: "))
IsPrime=True
if(number<0):
    print("Enter a positive number: ")
elif(number>0 and number<2):
    print("The smallest prime number is two") 
else:
    for i in range(2,int((number**0.5)+1)):
        if(number % i==0):
            IsPrime=False
            break
    if(IsPrime):
        print(f"The number entered {number} is  a prime number")
    else:
        print(f"The number entered {number} is not a prime number")        


           