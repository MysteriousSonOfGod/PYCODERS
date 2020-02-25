# import pyqrcode
# from qrtools import qrtools
# from PIL import Image
# import zbar
# qr = pyqrcode.create("She got two litle horns and they get me a litle bit")
# qr.png("horn.png", scale=6)
# qr = qrtools.QR()
# scanner = zbar.Scanner()
# qr.decode("horn.png")
# print(qr.data)
#----------------------------------------------------------------------------------------------------------------------
#----------------------------List TO Dictionary-----------------
l=[1,2,3,4,5]
em=[]
e=['ravi','kalyan','prasd']
# it, i2=iter(l), iter(e)
# d=dict(zip(it, i2))
# print("---------------------------------------------LIST TO DICTIONARY------------------------")
# print(d)
# print("----------------------------------------------LIST TO TUPLE")
# tp=tuple(l)
# print(tp)
# print("------------------------------------------------LIST TO SETS")
# st=set(l)
# print(st)
#---------------------------
#---------------------------------Convert a list into tuple of lists------------------
# o=tuple([name] for name in l)
# print(o)
#method-2--------------------------------- Using Map + Lambda

# o=tuple(map(lambda x: [x], l))
# print(o)

#Method-3-----------------Using Map + zip
# o=tuple(map(list, zip(l)))
# print(o)
# it=iter(l)
# d=list(zip(it, it, it))
# print(d)