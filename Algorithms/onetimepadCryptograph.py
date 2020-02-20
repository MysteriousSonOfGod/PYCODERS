import onetimepad
passw="KALYAN@#"
cipher=onetimepad.encrypt(passw, 'ra')
print(len(cipher))
msg=onetimepad.decrypt(cipher, 'ra')
print(msg)
