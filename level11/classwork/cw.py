total_sum = 0

for i in range(10):
    number = int(input(f"შეიყვანეთ მთელი რიცხვი #{i+1}: "))
    total_sum += number 

average = total_sum / 10

print("რიცხვების ჯამი არის:", total_sum)
print("რიცხვების საშუალო არითმეტიკული არის:", average)
