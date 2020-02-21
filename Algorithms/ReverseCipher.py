# Algorithm of Reverse Cipher
# The algorithm of reverse cipher holds the following features −
#
# Reverse Cipher uses a pattern of reversing the string of plain text to convert as cipher text.
#
# The process of encryption and decryption is same.
#
# To decrypt cipher text, the user simply needs to reverse the cipher text to get the plain text.

l=['RAVI@143','Kalyan023']
message = 'RAVI@143'
translated = '' #cipher text is stored in this variable
i = len(message) - 1
while i >= 0:
   translated = translated + message[i]
   i = i - 1
print("The cipher text is :", translated)
for j in l:
   if j==message:
      print("Matched")
