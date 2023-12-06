# ask user for their name and format for whitespace and capitalization
name = input("What's your name? ").strip().title()

# split user's name into first and last
first, last = name.split(" ")

# say hello to user
print(f"Hello, {first}")