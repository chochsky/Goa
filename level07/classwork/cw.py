num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
print("\n--- არითმეტიკული ოპერაციები ---")
print("ჯამი:", num1 + num2)
print("კლება:", num1 - num2)
print("გამრავლება:", num1 * num2)

if num2 != 0:
    print("გაყოფა:", num1 / num2)
    print("მთელი გაყოფა:", num1 // num2)
    print("ნაშთი:", num1 % num2)
else:
    print("გაყოფა შეუძლებელია — ნულზე გაყოფა არ შეიძლება.")

print("ხარისხში აყვანა:", num1 ** num2)

print("\n--- შედარების ოპერაციები ---")
print("ტოლია:", num1 == num2)
print("არ ტოლია:", num1 != num2)
print("მეტია:", num1 > num2)
print("ნაკლებია:", num1 < num2)
print("მეტია ან ტოლია:", num1 >= num2)
print("ნაკლებია ან ტოლია:", num1 <= num2)
