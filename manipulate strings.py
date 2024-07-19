text="Hello World!"
#convert to uppercase
uppercase_text = text.upper()
print("Uppercase:",uppercase_text)
#convert to lowercase
lowercase_text = text.lower()
print("Lowercase:",lowercase_text)
# length of the string
length_of_text = len(text)
print("Length:",length_of_text)
#Replace a substring
replaced_text = text.replace("World","Python")
print("Replaced:",replaced_text)
#split the string into a list
split_text = text.split(",")
print("split:",split_text)
#Join a list of strings into a single string
joined_text = "-".join(split_text)
print("Joined:",joined_text)