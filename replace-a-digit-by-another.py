text = input('Enter a text: ')
# replace the vowel 'a' by 'o'
x = text.casefold()
replaced_text = x.replace('a', 'o')
print("The new text after replacing 'a' by 'o' is: ", replaced_text)
