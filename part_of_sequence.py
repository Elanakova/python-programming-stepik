# Print out first N elements of the sequence 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7...
# N comes as an input

# Sample input:
# 7

# Sample output:
# 1 2 2 3 3 3 4

n = int(input())
l = [1]

for i in range(2, n):
    for j in range(0, i):
        if len(l) <= n - 1:
            l.append(i)
        else:
            break

print(*l)
