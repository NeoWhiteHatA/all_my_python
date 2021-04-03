import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = input()
num = phoneNumberRegex.search(message)
print('Found number' + num.group())