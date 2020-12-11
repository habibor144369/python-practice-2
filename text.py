import turtle

name = turtle.textinput('name', 'what is your name ? ')
name = name.lower()

if name.startswith('mr'):
    print('hello sir, how are you ?')
elif name.startswith('mrs') or name.startswith('miss') or name.startswith('ms'):
    print('hello madam, how are you')

else:
    name = name.capitalize()
    hello = 'Hi ' + name + '! how are you ?'
    print(hello)

turtle.exitonclick()
print('program terminated!')
