import string

alb = string.ascii_lowercase

code_to_break = input("Enter the cipher text: ").lower()

print(code_to_break)
special_char = "~`!@#$%^&*()_-+=';:<,>.?/\"{[}]|\\ 0123456789"


for i in range(25):
    final_code = "";
    key_shift = i
    for letter in code_to_break:
        if letter in special_char:
            final_code += letter
            continue

        index = string.ascii_lowercase.index(letter)

        if (index + key_shift) > 25:
            index = (index + key_shift) - 26
            final_code += string.ascii_lowercase[index]
        elif (index + key_shift) < 0:
            index = 26 - (index + key_shift)
            final_code += string.ascii_lowercase[index]
        else:
            final_code += string.ascii_lowercase[index + key_shift]
    print(f"{i} . {final_code}")

