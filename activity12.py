import getpass

username = 'hindiakosiryan'
password = 'akoposiryan143'

u = input('Input Username ---> ')
p = getpass.getpass('Input Password ---> ')


if password != u and p != password : 
        print("ACCESS DENIED")
        print("MALIII, HINDI IKAW SI RYAN")
else:
        print("DONE")
        print("WELCOME, RYAN!")
