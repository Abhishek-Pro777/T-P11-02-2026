password = input("Enter password: ")

has_digit = False
has_upper = False

if len(password) >= 8:
    for ch in password:
        if ch >= '0' and ch <= '9':
            has_digit = True
        if ch >= 'A' and ch <= 'Z':
            has_upper = True

    if has_digit and has_upper:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Password too short")