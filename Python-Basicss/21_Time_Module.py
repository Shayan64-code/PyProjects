import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
Hour = int(time.strftime("%H"))
print(Hour)

if 5 >= Hour <= 11:
    print("Good Morning")

elif 12 >= Hour <= 16:
    print("Good Afternoon")

elif 17 >= Hour <= 20:
    print("Good Evening")

else :
    print("Good Night")