year = int(input("Enter your birth year:"))
a = year % 12
if a == 0:
    print("Your Chinese Zodiac Sign is: Monkey")
elif a == 1:
    print("Your Chinese Zodiac Sign is: Rooster")
elif a ==2:
    print("Your Chinese Zodiac Sign is: Dog")
elif a == 3:
    print("Your Chinese Zodiac Sign is: Pig")
elif a == 4:
    print("Your Chinese Zodiac Sign is: Rat")
elif a == 5:
    print("Your Chinese Zodiac Sign is: Ox")
elif a == 6:
    print("Your Chinese Zodiac Sign is: Tiger")
elif a == 7:
    print("Your Chinese Zodiac Sign is: Rabbit")
elif a == 8:
    print("Your Chinese Zodiac Sign is: Dragon")
elif a == 9:
    print("Your Chinese Zodiac Sign is: Snake")
elif a == 10:
    print("Your Chinese Zodiac Sign is: Horse")
else:
    print("Your Chinese Zodiac Sign is: Goat")
