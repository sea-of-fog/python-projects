import re
import pyperclip

def valid(text):            # check if a date is valid
    return True             # TODO: dokończyć

date_regex = re.compile(r"""  #regular expression for dates in DD.MM.YYYY format
(\d{2}) \.  (\d{2}) \. (\d{4})
""", re.VERBOSE)

dates_found = date_regex.findall(pyperclip.paste())
for id in dates_found:
    if valid(id):
        print(id, end = " ")

print()
