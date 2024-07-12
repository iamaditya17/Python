# if-else

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are ready to Vote")
else:
    print("Sorry! you are under age to give vote !!!")

# if-elif-else

trafficLight = input("Enter the color of traffic light: ")

if(trafficLight == 'green'):
    print("You are ready to go")
elif (trafficLight == 'yellow'):
    print("Slow down your vehicle")
else:
    print("Stop your vehicle")

#nested-if

age = 20
drivingLicense = False

if(age >= 18):
    if(drivingLicense):
        print("You can ride your bike!!")
    else:
        print("please issue your driving license asap")
else:
    print("Sorry you can't ride your bike!!")

    