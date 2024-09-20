import string
import random
letters = list(string.ascii_letters)
numbers = list(range(0,9))
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-',  '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

n_letters = int(input("Enter the number of letters you want in the passwd : "))
n_numbers = int(input("Enter the number of whole numbers you want in the passwd : "))
n_symbol = int(input("Enter the number of symbols you want in the passwd : "))
##easy method generation
passwd = []
for i in range(1,n_letters+1):
    passwd+=random.choice(letters)
for i in range(1,n_numbers+1):
    passwd+=str(random.choice(numbers))
for i in range(1,n_symbol+1):
    passwd+= random.choice(symbols)
random.shuffle(passwd)

gen_password = "".join(passwd)
print(f"Your generated password is {gen_password}")
