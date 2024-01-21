import math

n = int(input("Enter n: "))

power = math.log10(n)
p = int(power)
a = int(math.pow(10, p))
ans = int(n/a)
print(ans)