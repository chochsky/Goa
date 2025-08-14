names = []
for i in range(5):
    name = input(f"შეიყვანეთ სახელი №{i+1}: ")
    names.append(name)
for name in names:
    if len(name) > 5:
        print(f"{name}: the name consists of more than five letters")
