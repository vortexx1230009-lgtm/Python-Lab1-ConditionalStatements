setfirst=[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
setsecond = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
setthird = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
setfourth = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
setfifth = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
sets = [setfirst,setsecond,setthird,setfourth,setfifth]
day = 0
for i in range(5):
    print("set", i+ 1, ":", sets[i])
    print("is your birthday include in this set?")
    answer = int(input("ENter 1 for yes and 0 for no:"))
    if answer == 1:
        day = day + sets[i][0]
print("Your Birthday is :", day)
