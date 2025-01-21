#Assingment 1
string = input("Enter some text: ")
string = string.upper()
string = string.replace(" ", "_")
print(f"The modified string is {string}.")
print(f"length of the modified string is {len(string)}.")

#Assingment 2
string = input("Enter some text: ")
string = string.upper()
string = string.replace(" ", "")
reverse = string[::-1]
if string == reverse:
    print("String is palidrome")
else:
    print("String is not a palidrome")