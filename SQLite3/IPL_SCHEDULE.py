import sqlite3

class Schedule:
    def __init__(self):
        self.conn=sqlite3.connect('IPL.db')
        self.cur=self.conn.cursor()

    def CreateSchedule(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS IPLSCHEDULE (sno INT, team VARCHAR(50), date VARCHAR(20), venue VARCHAR(20))")
        return "Successfully created"


    def Iser(self, fd):
        self.cur.executemany("INSERT INTO IPLSCHEDULE VALUES(?, ?, ?, ?)", fd)
        self.conn.commit()
        return "dvs"





matches=['CSKXDD','RCBXKIXP','MIXRR','SRHXKL','KKRXVT','CSKXRCB','MIXVT','DDXKIXP','RRXKKR','SRHXCSK','RCBXKL','VTXKIXP',
         'DDXMI','CSKXKKR','RRXRCB','KIXPXKL','VTXDD','RCBXMI','SRHXKKR','RRXCSK','KIXPXDD','KLXVT','MIXKKR', 'SRHXRR',
         'KXIPXCSK','RCBXKKR','KLXSRH','DDXCSK','RRXKL','VTXRCB','KKRXDD','CSKXMI','KIXPXRR','SRHXRCB','DDXKL','KKRXKIXP',
         'VTXRR','SRHXMI','KLXCSK','RCBXDD','KIXPXMI','SRHXVT','KLXKKR','DDXRR','CSKXSRH','MIXKL','KIXPXRCB','DDXVT','SRHXRR',
         'KKRXKL','MIXKIXP','DDXSRH','RCBXCSK','RRXVT','KKRXMI','SRHXKIXP','CSKXKL','DDXRCB','MIXSRH','KIXPXRR','VTXKKR',
         'MIXCSK','SRHXDD','KKRXRCB','VTXKL','RRXMI','CSKXKIXP','DDXKKR','KLXRCB','VTXSRH','RRXDD','KLXMI','KKRXCSK','KIXPXVT',
         'MIXRCB','RRXKL','VTXCSK','KIXPXSRH','KKRXRR','RCBXVT','MIXDD','CSKXRR','KIXPXKKR','RCBXSRH','VTXMI','KLXDD','RCBXRR',
         'KKRXSRH','KLXKIXP','CSKXVT']

dates=['25-03-2020','26-03-20','26-03-20','27-03-20','27-03-20','28-03-20','28-03-20','29-03-20','29-03-20','1-04-2020','01-04-2020'
       ,'02','02','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12','13','13','14','14','15','15',
       '16','16','17','17','18','18','19','19','20','20','21','21','22','22','23','24','24','25','26','26','27','27','28','28','30','30',
       '31','31','01-05-2020','01-05-2020','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','12','12']

venue=['Chennai','Bangalore','Mumbai','Hyderabad','Kolkata','Chennai','Mumbai','Delhi','Rajasthan','Hyderabad','Bangalore','Visakhapatanam',
       'Delhi','Chennai','Rajasthan','Punjab','Visakhapatanam','Bangalore','Hyderabad','Rajasthan','Punjab','Kerala','Mumbai','Hyderabad',
       'Punjab','Bangalore','Kerala','Delhi','Rajasthan','Visakhapatanam','Kolkata','Chennai','Punjab','Hyderabad','Delhi','Kolkata',
       'Visakhapatanam','Hyderabad','Kerala','Bangalore','Punjab','Hyderabad','Kerala','Delhi','Chennai','Mumbai','Punjab','Delhi','Hyderabad',
       'Kolkata','Mumbai','Delhi','Bangalore','Rajasthan','Kolkata','Hyderabad','Chennai','Delhi','Mumbai','Punjab','Visakhapatana',
       'Mumbai','Hyderabad','Kolkata','Visakhapatanam','Rajasthan','Chennai','Delhi','Kerala','Visakhapatanam','Rajasthan','Kerala','Kolkata',
       'Punjab','Mumbai','Rajasthan','Visakhapatanam','Punjab','Kolkata','Bangalore','Mumbai','Chennai','Punjab','Bangalore','Visakhapatanam','Kerala',
       'Bangalore','Kolkata','Kerala','Chennai']
e=[]
for i in range(1,91):
    e.append(i)

it=iter(matches)
it1=iter(e)
l=list(zip(e, matches, dates, venue))

Result = Schedule()
Result.CreateSchedule()
print(Result.Iser(l))
