# string search---
def my_function():
    string = str(input('Please type your string : '))

    first = ""
    second = ""
    three = ""
    four = ""
    for i in string:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            first = first + i

        elif i in "abcdefghijklmnopqrstuvwxyz":
            second = second + i

        elif i in "0123456789":
            three = three + i

        else:
            four = four + i

    print(first)
    print(second)
    print(three)
    print(four)

my_function()
