number = int(input("Enter a number to see its multiplication table: "))
for int in range(1, 11):
    result = number * int
    print(f"{number} * {int} = {result}")