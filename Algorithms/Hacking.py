# message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
# LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for key in range(len(LETTERS)):
#    translated = ''
#    for symbol in message:
#       if symbol in LETTERS:
#          num = LETTERS.find(symbol)
#          num = num - key
#          if num < 0:
#             num = num + len(LETTERS)
#          translated = translated + LETTERS[num]
#       else:
#          translated = translated + symbol
#
# print('Hacking key #%s: %s' % (key, translated))
# import base64
# encoded_data = base64.b64encode("Ravi")
# print("Encoded text with base 64 is")
# # print(encoded_data)
# import uuid
# import hashlib
#
# def hash_password(password):
#    # uuid is used to generate a random number of the specified password
#    salt = uuid.uuid4().hex
#    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
#
# def check_password(hashed_password, user_password):
#    password, salt = hashed_password.split(':')
#    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
#
# new_pass = input('Please enter a password: ')
# hashed_password = hash_password(new_pass)
# print('The string to store in the db is: ' + hashed_password)
# old_pass = input('Now please enter the password again to check: ')
#
# if check_password(hashed_password, old_pass):
#    print('You entered the right password')
# else:
#    print('Passwords do not match')



import onetimepad
import sqlite3
import psycopg2
name="ravi"
passw="Ravi@143"
cipher = onetimepad.encrypt(passw, 'random')
# with sqlite3.connect("teams.db") as con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS iplravi (name VARCHAR(50), password VARCHAR(50), cry VARCHAR(50))")
#     cur.execute("INSERT into iplravi (name,password, cry) values (?,?,?)", (name, passw, cipher))
#     con.commit()
conn=psycopg2.connect(database="ravi", user='postgres', password='Ravi@143', host='127.0.0.1', port='5432')
cursor=conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS ravipil (name VARCHAR(50) NOT NULL, password VARCHAR(50), ciepherText VARCHAR(100))")
# postgres_insert_query = """ INSERT INTO ravipil (name, password, ciepherText) VALUES (%s, %s, %s)"""
# record_to_insert = (name, passw, cipher)
# cursor.execute(postgres_insert_query, record_to_insert)
# conn.commit()

cursor.execute("SELECT password FROM ravipil")
rows=cursor.fetchall()
for i in rows:
    for j in i:
        if j==passw:
            print("Matched")
# e=[]
# for i in rows:
#     for j in i:
#         e.append(j)
# msg = onetimepad.decrypt(e[2], 'random')
# print(msg)
# print("FROM THE REFERENCE: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm")

# print("Plain text is ")
# msg = onetimepad.decrypt(cipher, 'random')

# print(msg)










