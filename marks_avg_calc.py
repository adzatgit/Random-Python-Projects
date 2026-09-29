#!/usr/bin/env python3

from ast import While
import time
time.sleep(0.5)
print(r'''
    __  ___           __        ______      __    
   /  |/  /___ ______/ /_______/ ____/___ _/ /____
  / /|_/ / __ `/ ___/ //_/ ___/ /   / __ `/ / ___/
 / /  / / /_/ / /  / ,< (__  ) /___/ /_/ / / /__  
/_/  /_/\__,_/_/  /_/|_/____/\____/\__,_/_/\___/  
                                                  
                                              
''')
time.sleep(0.5)
print("Enter your marks for all 6 subjects (out of 80):")
time.sleep(0.5)
om1=float(input("Marks for the first subject: "))
om2=float(input("Marks for the second subject: "))
om3=float(input("Marks for the third subject: "))
om4=float(input("Marks for the fourth subject: "))
om5=float(input("Marks for the fifth subject: "))
om6=float(input("Marks for the sixth subject: "))
def main():
    u=int(input("Do u want to calculate your average marks or average percentage marks? (Enter 1 for average, 2 for percentage, 3 to exit): "))

    def average_marks():
        n=om1+om2+om3+om4+om5+om6
        return n/6

    def average_percentage_marks():
        n=om1+om2+om3+om4+om5+om6
        return (n/480)*100

    if u==1:
        time.sleep(0.5)
        print("Your average marks are:", average_marks())
    elif u==2:
        time.sleep(0.5)
        print("Your average percentage marks are:", average_percentage_marks())
    elif u==3:
        time.sleep(0.5)
        print("Exiting...")
        time.sleep(0.5)
        exit()
while True:
    main()
    time.sleep(1)
