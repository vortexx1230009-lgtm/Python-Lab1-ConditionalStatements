def main():
    while True:
        print("\n==============================")
        print("   PYTHON LAB 1 - MAIN MENU   ")
        print("==============================")
        print("1. BMI Calculator")
        print("2. Chinese Zodiac Calculator")
        print("3. Birthday Guessing Game")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            print("\n--- BMI Calculator ---")
            try:
                kq = float(input("Enter your weight: "))
                boy = float(input("Enter your height: "))
                
                if kq <= 0 or boy <= 0:
                    print("Error: Weight and height must be greater than zero!")
                    continue
                    
                BMI = (kq) / (boy**2)
                print(f"BMI: {BMI}")
                
                if BMI < 18.5:
                    print("You are underweight, thin")
                elif 18.5 <= BMI < 25:
                    print("you are weight is normal")
                elif 25 <= BMI < 30:
                    print("you are overweight")
                else:
                    print("You are obese, obesity")
                    
            except ValueError:
                print("Invalid input! Please enter numeric values only.")
                
        elif choice == '2':
            print("\n--- Chinese Zodiac Calculator ---")
            try:
                year = int(input("Enter your born year: "))
                a = year % 12
                
                if a == 0:
                    print("your zodiac sign is monkey")
                elif a == 1:
                    print("your zodiac sign is rooster")
                elif a == 2:
                    print("your zodiac sign is dog")
                elif a == 3:
                    print("your zodiac sign is pig")
                elif a == 4:
                    print("your zodiac sign is rat")
                elif a == 5:
                    print("your zodiac sign is ox")
                elif a == 6:
                    print("your zodiac sign is tiger")
                elif a == 7:
                    print("your zodiac sign is rabbit")
                elif a == 8:
                    print("your zodiac sign is dragon")
                elif a == 9:
                    print("your zodiac sign is snake")
                elif a == 10:
                    print("your zodiac sign is horse")
                else:
                    print("your zodiac sign is goat")
                    
            except ValueError:
                print("Invalid input! Please enter a valid integer year.")
                
        elif choice == '3':
            print("\n--- Birthday Guessing Game ---")
            try:
                setfirst = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
                setsecond = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
                setthird = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
                setfourth = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                setfifth = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
                sets = [setfirst, setsecond, setthird, setfourth, setfifth]
                
                day = 0
                for i in range(5):
                    print("set", i + 1, ":", sets[i])
                    print("Is your birthday included in this set?")
                    answer = int(input("Enter 1 for yes and 0 for no: "))
                    
                    if answer == 1:
                        day = day + sets[i][0]
                        
                print("Your Birthday is:", day)
                
            except ValueError:
                print("Invalid input! Please enter 1 or 0.")
                
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()