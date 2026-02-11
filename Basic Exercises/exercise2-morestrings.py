text = "  Hello, World! Welcome to Python Programming.  "
words = text.split()
text = text.strip()






print('Stripped:',text)
print('Word Count', len(words))
print('Title case:',text.title())
print('Starts with Hello',text.startswith('Hello'))
print('Ends with ing.:',text.endswith('ing.'))
print('Python position:',text.find('Python'))
print('Joined:'," - ".join(words))
