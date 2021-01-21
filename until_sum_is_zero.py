# Read numbers (one by one) until total sum of them is 0.
# Right after that print out sum of  squares of numbers that were read.

# Sample input:
# 1
# -3
# 5
# -6
# -10
# 13 - here total sum is 0 and we don't read following numbers
# 4
# -8

# Sample output:
# 340

a = int(input())
total_sum = a
i = 1
res = [a]
while total_sum != 0:
    a = int(input())
    total_sum = total_sum + a
    res.insert(i, a)
    i = i + 1
total_sum = 0
for el in res:
    total_sum = total_sum + el ** 2
print(total_sum)
