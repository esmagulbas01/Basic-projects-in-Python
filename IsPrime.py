number=int(input("Enter a number: "))
Prime_Numbers=[]
if(number<0):
    print("Enter a positive number: ")
elif(number>0 and number<2):
    print("The smallest prime number is two") 
else:
    Prime_Numbers.append(2)
    for j in range(3,number+1,2):
         for i in range(3,int((j**0.5)+1)):
              if(j % i==0):
                  break
         else:
             Prime_Numbers.append(j)       
           
    print(Prime_Numbers)          
           
                   
         
   
          


           