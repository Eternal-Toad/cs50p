# ask user for their name
name = input("what's your name? ")

# remove whitespace from str
name = name.strip()

# capitalize user's name
name = name.title()

# Say hello to user
print(f"hello, {name}")