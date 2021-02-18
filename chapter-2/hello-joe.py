#chapter 2

while True:
    name = input("Who are you? ")
    if name != "Joe":
        continue
    psswd = input("Hello Joe, what is the password?(It is a fish) ")
    if psswd == "swordfish":
        break

print("Access granted")

