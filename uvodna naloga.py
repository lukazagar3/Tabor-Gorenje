n = int(input("Stevilo mentorjev: "))
n = (n-1)*2 + 6

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n):
    print("*" * (n*2 - 1))