# ask user for input
print("*" * 70)
encrypted_str = input("\n\033[3m\033[1m" "Enter a text to decrypt: " "\033[0m" ) 
decrypted_str = ""
# check each character
for i in range(len(encrypted_str)):
# if *, change to a
# if &, change to e
# if #, change to i
# if +, change to o
# if !, change to u
# else, do not change 
# print output