# ask user for input
print("*" * 70)
encrypted_str = input("\n\033[3m\033[1m" "Enter a text to decrypt: " "\033[0m" ) 
decrypted_str = ""
# check each character
for i in range(len(encrypted_str)):
#   if *, change to a
    if encrypted_str[i] == "*":
        decrypted_str += "\033[0;31m" "a" "\033[0m"
#   if &, change to e
    elif encrypted_str[i] == "&":
        decrypted_str += "\033[0;31m" "e" "\033[0m"
# if #, change to i
# if +, change to o
# if !, change to u
# else, do not change 
# print output