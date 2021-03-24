import pyperclip
import sys
PASSWORDS = {'email':'1234567890','blog':'ASDFGHJKL','luggage':12345}
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = input('enter account to see password:  ')

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+ ' copied to clipboard')
else:
    print('there is no account named'+ account)
