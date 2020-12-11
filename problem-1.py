# string counting here
def my_function(string):
    text = ' '
    text_2 = ' '

    for i in string:
        if i == i.capitalize():
            text += i

        elif i == i.lower():
            text_2 += i

    print(text)
    print(text_2)

my_function('Hello Programmer Welcome to my world')
