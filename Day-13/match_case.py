def weekdays(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case _: return "Invalid entry"
print (weekdays(3))
print (weekdays(8))
print (weekdays(6))