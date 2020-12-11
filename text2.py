# text input----
from tkinter import *
root = Tk()
root.geometry('400x300')
root.title("Input Text")

def my_function():
    name = entry.get()
    name = name.lower()
    print(name)
    if name.startswith('mr') or name.startswith('md') or name.startswith('professor'):
        print('hello sir, how are you ?')
    elif name.startswith('miss') or name.startswith('begum') or name.startswith('madam'):
        print('hello madam, how are you')

    else:
        name = name.capitalize()
        hello = 'Hi ' + name + '! how are you ?'
        print(hello)


entry = Entry(root, width =  50)
entry.pack()

Button(root, text = 'button', command = my_function).pack()

mainloop()
print('program terminated!')
