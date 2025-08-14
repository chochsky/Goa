secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("შეიყვანეთ რიცხვი 1-დან 10-მდე: "))
    if guess == secret_number:
        print("მოგილოცავთ! სწორად გამოიცანით.")
    else:
        print("არასწორია, სცადეთ კიდევ.")
