numbers = []
for i in range(10):
    num = int(input(f"შეიყვანეთ რიცხვი №{i+1}: "))
    numbers.append(num)
for num in numbers:
    if num % 2 == 0:
        print(f"{num} არის ლუწი")
    else:
        print(f"{num} არის კენტი")
