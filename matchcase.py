# day = 4
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invailid day")

value ="Hello"
match value:
    case int:
        print("An integer")
    case str:
        print("A string")
    case float:
        print("A float")
    case list:
        print("A list")
    case _:
        print("unknown type")