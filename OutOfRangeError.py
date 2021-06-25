class OutOfRangeError(Exception):
    pass


def name_the_number():
    a_num = int(input("enter a number: "))
    if a_num == 1:
        print("one")
    elif a_num == 2:
        print("two")
    elif a_num == 3:
        print("three")
    else:
        raise OutOfRangeError


try:
    name_the_number()
except OutOfRangeError:
    print("That's not one of the allowed values!")
