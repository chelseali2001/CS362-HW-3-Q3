valid = 0

while valid == 0:
    valid = 1
    n = input("Enter a year: ")

    for x in n:
        if x < '0' or x > '9':
            print("Error: invalid input, ints only.")
            valid = 0
            break

n = int(n)

if n % 4 == 0:
    if n % 100 == 0 and n % 400 != 0:
        print(n, "is not a leap year")
    else:
        print(n, "is a leap year")
else:
    print(n, "is not a leap year")