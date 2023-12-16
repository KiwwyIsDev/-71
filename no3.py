email = input("E-Mail : ")
password = input("Password : ")

vaild_email = ['preecha.ac.th', 'kengdee.ac.th', 'samart.ac.th']
# print(not email.startswith('66'))
# print(email.split("@")[1] not in vaild_email)
if not email.startswith('66') or email.split("@")[1] not in vaild_email:
    print('This email cannot be registered')
else:
    rahat = email.split("@")[0]
    if not rahat.isdigit() or len(rahat) < 5:
        print('This email cannot be registered')
    else:
        #print(email)
        if len(password) < 10:
            print("Password must be at least 10 characters")
        elif email == password:
            print('Password must not be the same as email')
        else:
            print('Complete')



