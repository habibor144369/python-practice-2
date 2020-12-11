# it's right way to working the program-------
string = input("enter here string : ")
length = len(string)
new_str = ""
i = 0
if length % 2 == 0:
    while i < length:
        first_value = string[i]
        new_str = new_str + string[i + 1]
        new_str = new_str + first_value
        i = i + 2

else:
    while i < length - 1:
        first_value = string[i]
        new_str = new_str + string[i + 1]
        new_str = new_str + first_value
        i = i + 2
        if i == length - 1:
            new_str = new_str + string[i]

print(new_str)

