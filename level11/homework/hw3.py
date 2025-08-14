correct_password = "abc123"
password = ""

while password != correct_password:
    password = input("შეიყვანეთ პაროლი: ")
    if password != correct_password:
        print("პაროლი არასწორია. სცადეთ კიდევ.")
print("თქვენ წარმატებით შეხვდით სისტემაში!")
