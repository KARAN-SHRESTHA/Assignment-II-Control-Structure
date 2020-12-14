""" 2. Write an if statement to determine whether a variable holding a year is
a leap year."""

print("Question 2")

year = int(input("Enter a year:  "))

"""
a year has 365.25 days and 11 minutes extra
so in every 4th year it is a leap year as 0.25 gets added up
so the year completely divided by 4 is a leap year
however a century year is different as in each year 11 minutes extra is added up
meaning in 400 years it becomes 3 days extra meaning 3 leap years
so the century year must be completely divisible by 400 too. 
"""

if year % 4 == 0:
    #checking whether the year is a century year or not
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Not Leap Year")