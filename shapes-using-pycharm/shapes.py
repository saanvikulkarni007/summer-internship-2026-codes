
print("SHAPE: RECTANGLE")
print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

print("SHAPE: TRIANGLE")
for i in range(1,7):
    print("*"*i)

print("SHAPE: HOLLOW SQUARE")
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")