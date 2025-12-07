###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r') as f:
    email = f.read()


# regular expression pattern
# for amounts
pattern = r'\d+\.\d{2}|\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amounts in amounts:
   total = total + int(amounts)

# print result
print(total)
