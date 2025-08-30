
match favorite_day:= input("Enter your favorite day"):
    case "Friday":
        print("My Favorite Day")
    case "Saturday":
        print("2nd most Favorite Day")
    case "Sunday":
        print("3rd most Favorite Day")
    case _:
        print("Not my favorite day")



# combine values
day = int(input("enter a day: "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("Today is a weekend")
    case _:
        print("Invalid day")