def format_sentence(sentence):
    print("1. პატარა ასოებით:", sentence.lower())
    print("2. დიდი ასოებით:", sentence.upper())
    print("3. პირველი ასო დიდი, დანარჩენი პატარა:", sentence.capitalize())

# გამოვიძახოთ ფუნქცია
user_input = input("შეიყვანეთ წინადადება: ")
format_sentence(user_input)
