import string

a_string = input("enter string here:")
new_string = a_string.translate(str.maketrans('', '', string.punctuation))

print(new_string)