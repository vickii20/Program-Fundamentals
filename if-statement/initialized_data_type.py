input_datatype = input("Enter your Value: ")

if input_datatype.isalpha():
    print("Alphabet")
elif input_datatype.isdigit():
    print("Digit")
else:
    print("Special Character")
