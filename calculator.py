x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

# use f string to format number output with comma
print(f"{z:,}")

z = x / y

# fstring can be used to round digits
print(f"{z:.2f}")