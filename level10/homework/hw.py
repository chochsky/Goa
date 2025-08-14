correct_password = "1234"
password = ""

while password != correct_password:
    password = input("შეიყვანეთ პაროლი: ")
    print("Incorrect password. Try again" * (password != correct_password))

print("Correct password. You have successfully logged in.")
