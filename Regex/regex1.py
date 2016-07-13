#Needed to allow regex to work
import re
PhoneRegex = re.compile(r'(\d) (\d\d\d-)*\d\d\d-\d\d\d\d')
mo = PhoneRegex.search('My numbr is 1 800-977-0548')
print('Phone number found: ' + mo.group())

#phoneRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneRegex1.search('My digits are 653-997-2932')
#areaCode, mainnumber = mo.groups()
#print(areaCode)
#print(mainnumber)

#If the specific filename is present, print
fileRegex = re.compile(r'(\w)+(\d\d\d.log)')
mo = fileRegex.search('test343.log')
print('The file\'s name is: ' + mo.group())

#Using findall to look throughout a string and find phone numbers
PhoneRegex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
PhoneRegex2.findall('Cell: 415-454-3433 Work: 759-887-3232')