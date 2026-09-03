#concatenation = combining strings 


talent = "" 

t = input("What are your talents --> ")
talents = t + ","

t = input("What else? --> ")
talents += t + ","

t = input("What else? --> ")
talents += t + ","

t = input("What else? --> ")
talents += t + ","

t = input("What else? --> ")
talents += "and " + t 

print("My talents are ", talents)
