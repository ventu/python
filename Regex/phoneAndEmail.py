import re, pyperclip

#TODO: Create a regex for phone numbers
#415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345,, ext. 12345, x12345
phoneRegex = re.compile(r"""
(
((\d\d\d) | (\(\d\d\d\)))?  #area code (optional)
(\s|-)  #first separator
\d\d\d #first 3 digits
-   #spearator
\d\d\d\d    #last 4 digits
(((ext (\.)?\s) |x)
(\d{2,5}))?  #extension (optional)
)
""", re.X)

#TODO: Create a regex for email addresses
emailRegex = re.compile(r"""

[a-zA-Z0-9_.+]+    # name part
@   # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
""", re.X)
#TODO: Get the text off the clipboard
text = pyperclip.paste()

#TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)