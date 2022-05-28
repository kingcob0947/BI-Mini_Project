##### REGEX(REgular Expression):-
import re
s = "My personal mobilne number is +098765432112 and office number is +123456789098"
phone = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
phone_number = phone.search(s)
print('the mobile number is:', phone_number.group())

## if find the all mobile number in given string:-
phone1 = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
Emplyoee_Number = phone1.findall(s)
for my_number in Emplyoee_Number:
 print('the number is:', my_number)