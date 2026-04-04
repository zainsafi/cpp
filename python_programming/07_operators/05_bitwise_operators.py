#bitwise operators works on bits
"""bitwise operators are: *bitwise AND(&) *bitwise OR(|) *bitwise XOR(^) *bitwise NOT or compliment(~)
   *left shift(<<) *right shift(>>)
"""
a,b = 5 , 4;

print(a & b) #first a and b wil be converted into binary then & is applied and the result is converted into decimal again
print(a | b)
print(a ^ b)
print(~a) #output is -6 but how ?
#a = 5 = 0101 so ~a = ~5 = 1010
#As negative numbers are store in the computer memory using two's compliment method i -e 2's = 1's + 1
#6 = 0110 =>1's of 6 = 1001 =>2's of 6 = 1001 + 1 =1010 =>and 1010 is exactly = ~5
#shortcut => ~n = -(n + 1) e-g ~10 = -(10 + 1) = -11


print(a << 2)#a = 5 = 0000 0101 =>0001 0100 =>16 + 4 = 20 =>in lift shift bits are not discarded although 0's are does.
#shorcut formula => x<<n => x*2^n


print(a >> 2)#a = 5 = 0101 => 0001 => 1 => in right shift the right most bits are discarded.
#shorcut formula => x<<n => x/2^n