#in python datatypes is consider as a class and the variable is consider as the member or instant of that class
'''some data types are:
                        integer
                        float
                        string
                        boolean(T or F)
'''
#integer data type
#you can enter a number of any range (+ or -)
''' a = 1234568737 -----> it would be consider as a decimal number but if use prefixes like
                * 0b or 0B ----> for binary
                * 0o or 0O ----> for octal
                * 0x or 0X ----> for hexadecimal
'''
#Forexample:
a = 10     #---->decimal(0 to 9)
b = 0b0010   #---->binary(0 and 1)
c = 0o1457   #---->octal(0 to 7)
d = 0x16987  #---->hexadecimal(0x16)
print(a,"\n",b,"\n",c,"\n",d) 
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#float numbers
e = 12.5
print(e,"\n",type(e))

#string datatype
name_1 = "zain khan"
print(name_1)
print(name_1[0])
print(name_1[8])
name_2 = " The King"
print(name_1 + name_2)
print("123" + "1") #--->it will print 1231 not 124 bcz both is consider as string
#there are two ways to skip the meaning of "" and '' in a string i-e (1)use of ''' (2)use of \ e.g
print('''"jenny's lectures"''') #or
print("\"jenny\'s lectures\"")
'''so if you want to skip the meaning of any thing or special character,use \ before it. you can also print
    \n by writting another \ before it '''
print(5 * "zain ")

#Bolean datatype(T or F)
f = True
print(f)
print(type(f))
#forexample
a = 3;
b = 5;
var = a < b
print(var)
print(type(var))