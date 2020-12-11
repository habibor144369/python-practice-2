# string inverting program and palindrome check----
def string(text):
    new_text = ''
    for i in text:
        new_text = i + new_text
    if text == new_text:
        ans = 'palindrome'
        return ans
    else:
        ans = 'don\'t palindrome'
        return ans

text = str(input('please input your string : '))
result = string(text)
print(result)
