HumanBodyParts=['Head','Hair','ear','Eye','Nose','chest','Neck','Stomach','Arm','Leg','Foot','ForeHead','Mouth','Lip','Chin','Nipple','Amdomen','Navel','Hip',
                'Groin','Leg','Thigh','Hand','Knee','Foot','Instep','Toenail','Armpit','Elbow','Waist','Wrist',
                'Thumb','Forearm','Fingers','Calf','Heal','Ankle','Shoulder','Temple','eyebrow','eyelash','iris','cheek','jaw','nostril','palm','index finger','littel finger','ring finger'
                ]

EnglishWords= ['devastated', 'నాశనం', 'weird', 'అసహజ', 'embrace', 'ఆలింగనం', 'embarrassed', 'అసహనం', 'offend', 'నేరం',
     'abundant', 'సమృద్ధిగా', 'ample', 'పుష్కల','contention','వివాదాస్పద','congestion', 'రద్దీ','Starvation','ఆకలి','alarmed','భయపడిన','Merchant','వ్యాపారి','Meat','మాంసం','Servant','సేవకుడు','Hungry','ఆకలితో'
              ,'Themselves','తాము','Allowances','భత్యం','Thus','ఈ విధంగా','Aspiration','ఆశించిన','Perstigious','ప్రతిష్టాకరమైన','Delighted','ఆనందపరిచింది',
              'felt','భావించాడు','Slight','స్వల్ప','Humiliated','అవమానాలు','Tail','తోక','Hapless','అదృష్టము లేని','Drowned','మునిగిన',
              'Bloated','ఉబ్బిన','Swooped','విస్తుపోయింది','Grabbing','ఈడ్చడం','Flew','వెళ్లింది ఎగిరినది','Hauled','నెట్టబడే','Desperately','నిర్విరామంగా',
              'pit','గొయ్యి','wisdom','జ్ఞానం','fame glory perstige','కీర్తి','Wise','తెలివైన','devilish','పైశాచిక','renowned','ప్రఖ్యాత','perceive','అవగతం',
              'firm','సంస్థ','vouch','హమీ','Startling','కరమైన','seems','తెలుస్తోంది','thoughtful','శ్రద్ద','fuel','ఇంధన','what','ఏమి',
     'why','ఎందుకు','freedom','స్వేచ్ఛ','irritate','చికాకుపరచు','cipher','సాంకేతికలిపి','keenly','ఆత్రుతతో']
print("THE LENGTH OF ENGLISHWORD IS",int(len(EnglishWords)/2))
n=input()
for i in range(0, len(EnglishWords)):
    for j in EnglishWords:
        if j==n:
            k=EnglishWords.index(j)
            print(EnglishWords[k+1])
    break





GRAMMAR=['How are you', 'ఎలా ఉన్నారు','How are you?','మీరు ఎలా ఉన్నారు?','How do you do?','ఎలా ఉన్నారు?','Where are you?','మీరు ఎక్కడ ఉన్నారు?',
         'What can do for you?','మీ కోసం ఏమి చేయవచ్చు?','had you dinner','మీరు విందు చేశారా?','had you lunch','మీరు భోజనం చేశారా?']










#1.LIST LOGIC1
# for i in range(5, -1, -1):
#
#     if i % 1 == 0:
#         pass
#     if i % 2 ==0:
#         pass
#     if i % 3 == 0:
#         pass
#     if i % 4 == 0:
#         break
#     print(i, end='-')


# k=[2,3,4,'Python','Kalyan']
# print(k[:-3])
# print(k[::-1])
