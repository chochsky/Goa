while True:
    number = float(input("გთხოვთ, შეიყვანეთ დადებითი რიცხვი: "))
    
    if number > 0:
        print(f"თქვენ შეიტანეთ დადებითი რიცხვი: {number}")
        break  
    else:
        print("შეცდომა: რიცხვი უნდა იყოს დადებითი. სცადეთ კიდევ.")
