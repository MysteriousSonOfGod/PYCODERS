# import json
# HumanBodyParts=['Head','Hair','ear','Eye','Nose','chest','Neck','Stomach','Arm','Leg','Foot','ForeHead','Mouth','Lip','Chin','Nipple','Amdomen','Navel','Hip',
#                 'Groin','Leg','Thigh','Hand','Knee','Foot','Instep','Toenail','Armpit','Elbow','Waist','Wrist',
#                 'Thumb','Forearm','Fingers','Calf','Heal','Ankle','Shoulder','Temple','eyebrow','eyelash','iris','cheek','jaw','nostril','palm','index finger','littel finger','ring finger'
#                 ]
# # n=input()
# # if n in HumanBodyParts:
# #     print("founded")
# # else:
# #     print("Not Found")
# e=[]
# for i in range(len(HumanBodyParts)):
#     e.append(i)

# h1=iter(HumanBodyParts)
# h2=iter(e)
# d=dict(zip(h2,h1))
# print(d)
# app_json=json.dumps(d)
# print(app_json)

import json

class Ravi:
    def __init__(self):
        self.HumanBodyParts=['Head','Hair','ear','Eye','Nose','chest','Neck','Stomach','Arm','Leg','Foot','ForeHead','Mouth','Lip','Chin','Nipple','Amdomen','Navel','Hip',
                'Groin','Leg','Thigh','Hand','Knee','Foot','Instep','Toenail','Armpit','Elbow','Waist','Wrist',
                'Thumb','Forearm','Fingers','Calf','Heal','Ankle','Shoulder','Temple','eyebrow','eyelash','iris','cheek','jaw','nostril','palm','index finger','littel finger','ring finger'
                ]
        self.e=[]


    def Kal(self):
        for self.i in range(len(self.HumanBodyParts)):
           self.e.append(self.i)

        return self.e

    def dictionaryDisplay(self):
        self.Kal()
        h1=iter(self.HumanBodyParts)
        h2=iter(self.e)
        self.d=dict(zip(h2, h1))
        return self.d

    def DisJson(self):
        self.dictionaryDisplay()
        self.appJson=json.dumps(self.d)
        self.r=open('jsonformat.json', 'w')
        self.r.write(self.appJson)
        self.r.close()
        return "successfully Updated"
r=Ravi()
rs=r.DisJson()
print(rs)


# import json
# json_file=open('ravi.txt', 'r', encoding="utf-8")
# re=json_file.read()
# # print(re)
# movie=json.loads(re)
# json_file.close()
# print(type(movie))
# print(movie)
# e=[]
# for i in movie.values():
#     # print(i)
#     e.append(i)
#
# print(e)
# for j in e:
#     print(type(j))


# import json
# movie={}
# movie["title"]="Inception"
# movie["director"]="Steven Spielbreg"
# movie["actors"]=["Tom Cruise","Colin Farrell"]
# movie["is_awesome"]=True
# file2=open('/home/ravi/Documents/PYCODERS/movieslist.txt', 'w', encoding='utf-8')
# r=json.dump(movie, file2, ensure_ascii=False)
# file2.close()




#THE BELOW CODE IS USED FOR TO SAVE DIFFERENT FILES IN YOUR SYSYATEM USING PYTHON
# file = open('filename', 'w')
# file.write(your_multiline_string)
# file.close()