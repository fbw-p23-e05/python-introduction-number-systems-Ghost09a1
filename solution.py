# Task1
# Convert a decimal number to binary

num = 27
binary = bin(num)
print(binary) # 0b11011


# Task2
# Convert a binary number to decimal

num = 11011
decimal = int(num, 2)
print(decimal) # 27


# Task3
# Convert a decimal number to hexadecimal

num = 27
hexadecimal = hex(num)
print(hexadecimal) # 0x1b

# Task4
# Convert a hexadecimal number to decimal

num = "1b"
decimal = int(num, 16)
print(decimal) # 27


# Task5
# Convert a binary number to hexadecimal

num = 11011
decimal =int(num, 2)
hexadecimal = hex(decimal)
print(hexadecimal) # 0x1b

# Task6
# Convert a hexadecimal number to binary

num = "1b"
decimal = int(num, 16)
binary = bin(decimal)
print(binary)  # 0b11011

# Bonus

### Task 7
# Convert a decimal number to octal

num = 27
octal = oct(num)
print(octal)  # 0o33

### Task 8
# Convert a octal number to decimal

num = 0o33
decimal = int(str(num), 8)
print(decimal)  # 27



