import shelve, pyperclip,sys
password_shelf = shelve.open('password')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    password_shelf[sys.argv[2]] == pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(password_shelf.keys())))
    elif sys.argv[1] in password_shelf:
        pyperclip.copy(password_shelf[sys.argv[1]])
password_shelf.close