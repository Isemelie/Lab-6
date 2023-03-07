
def password_changer(changer):
    for x in changer:
            changer=int(x+3)
    return changer

print(
"""Menu 
-------------
1. Encode  
2. Decode  
3. Quit """)
options=input("Please enter an option:")
password=input("Please enter your password to encode:")

print(password_changer(password))

