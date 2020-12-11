# string inverting program ----
def string(text):
    new_text = ''
    for i in text:
        new_text = i + new_text
    return new_text

text = str(input('please input your string : '))
result = string(text)
print(result)
