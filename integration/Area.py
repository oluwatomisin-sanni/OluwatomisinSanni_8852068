import math

def Circle ():
        radius = float(input("Enter the radius of your Circle"))
        return math.pi*radius**2

def Rectangle():
        length = float(input("Enter the length of your Rectangle"))
        breadth = float(input("Enter the breadth of your Rectangle"))
        return length*breadth

def Triangle():
        base = float(input("Enter the base of your Triangle"))
        height = float(input("Enter the height of your Triangle"))
        return 0.5*base*height

def Square():
        side = float(input("Enter the length of any side "))
        return side*side

def main():
    option = int(input("Choose a shape \nEnter the your choice by typing 1, 2, or 3."))
    print ("Pick a shape from the options below \n1. Circle \n2. Rectangle \n3. Triangle \n4. Square.")

    if option == '1':
         area=Circle()
         print("the area is: {area}")

    elif option == '2':
         area = Rectangle()
         print("the area is : {area}")

    elif option =='3':
          area = Triangle()
          print("the area is: {area}")

    elif option == '4':
          area = Square()
          print("the area is: {area}")

    else :
        print("Enter a valid option from the list above.") 