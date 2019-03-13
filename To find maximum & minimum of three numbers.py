#Program to find max and min of three numbers
var1=int(input("Enter 1st number"))
var2=int(input("Enter 2nd number"))
var3=int(input("Enter 3rd number"))
max = var1                  #Assume it to be maximum
min = var3                  #Assume it to be minimum
if (max<var2):
    max = var2
if (max<var3):
    max=var3
if (min>var2):
    min=var2
if (min>var1):
    min=var1
mid = var2
if (var1>var2 and var1<var3):
    mid=var1
if(var3>var2 and var3<var1):
    mid=var3
print("Maximum number is : "+str(max)+"\n"+"Middle number is : "+str(mid)+"\n"+"Minimum number is : "+str(min))
