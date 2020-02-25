# import itertools
# a, a1, a2, a3, a4, a5, a6, a7, a8 = ['csk', 'dd'], ['csk', 'rcb'], ['csk', 'rr'], ['csk','srh'], ['csk', 'kixp'], ['csk', 'mi'], ['csk', 'kkr'], ['csk', 'kl'], ['csk', 'vt']
# b, b1, b2, b3, b4, b5, b6, b7 = ['dd', 'rcb'], ['dd', 'rr'], ['dd', 'srh'], ['dd', 'kixp'], ['dd', 'mi'], ['dd', 'kkr'], ['dd', 'kl'], ['dd', 'vt']
# c, c1, c2, c3, c4, c5, c6 = ['rcb', 'rr'], ['rcb', 'srh'], ['rcb', 'kixp'], ['rcb', 'mi'], ['rcb', 'kkr'], ['rcb', 'kl'], ['rcb', 'vt']
# d ,d1, d2, d3, d4, d5 = ['rr', 'srh'], ['rr', 'kixp'], ['rr', 'mi'], ['rr', 'kkr'], ['rr', 'kl'], ['rr', 'vt']
# e, e1, e2, e3, e4 = ['srh', 'kixp'], ['srh', 'mi'], ['srh', 'kkr'], ['srh', 'kl'], ['srh', 'vt']
# f, f1, f2, f3 = ['kixp', 'mi'], ['kixp', 'kkr'], ['kixp', 'kl'], ['kixp','vt']
# g ,g1, g2 = ['mi', 'kkr'], ['mi', 'kl'], ['mi', 'vt']
# h, h1 = ['kkr', 'kl'], ['kkr', 'vt']
# i = ['kl', 'vt']
# r, r1, r2, r3, r4, r5, r6, r7, r8 = list(itertools.permutations(a)), list(itertools.permutations(a1)),list(itertools.permutations(a2)), list(itertools.permutations(a3)), list(itertools.permutations(a4)), list(itertools.permutations(a5)), list(itertools.permutations(a6)), list(itertools.permutations(a7)), list(itertools.permutations(a8))
# s, s1, s2, s3, s4, s5, s6, s7 = list(itertools.permutations(b)), list(itertools.permutations(b1)),list(itertools.permutations(b2)), list(itertools.permutations(b3)), list(itertools.permutations(b4)),list(itertools.permutations(b5)), list(itertools.permutations(b6)), list(itertools.permutations(b7))
# t, t1, t2, t3, t4, t5, t6 = list(itertools.permutations(c)), list(itertools.permutations(c1)),list(itertools.permutations(c2)), list(itertools.permutations(c3)), list(itertools.permutations(c4)),list(itertools.permutations(c5)), list(itertools.permutations(c6))
# x, x1, x2, x3, x4, x5 = list(itertools.permutations(d)), list(itertools.permutations(d1)), list(itertools.permutations(d2)), list(itertools.permutations(d3)), list(itertools.permutations(d4)), list(itertools.permutations(d5))
# y, y1, y2, y3, y4 = list(itertools.permutations(e)), list(itertools.permutations(e1)), list(itertools.permutations(e2)), list(itertools.permutations(e3)),list(itertools.permutations(e4))
# z, z1, z2, z3 = list(itertools.permutations(f)), list(itertools.permutations(f1)), list(itertools.permutations(f2)), list(itertools.permutations(f3))
# w, w1, w2 = list(itertools.permutations(g)), list(itertools.permutations(g1)), list(itertools.permutations(g2))
# p, p1 = list(itertools.permutations(h)), list(itertools.permutations(h1))
# q = list(itertools.permutations(i))
# fn = r+r1+r2+r3+r4+r5+r6+r7+r8+s+s1+s2+s3+s4+s5+s6+s7+t+t1+t2+t3+t4+t5+t6+x+x1+x2+x3+x4+x5+y+y1+y2+y3+y4+z+z1+z2+z3+w+w1+w2+p+p1+q
# print(fn)
#
#
#
#
#
#
#

matches=['CSKXDD','RCBXKIXP','MIXRR','SRHXKL','KKRXVT','CSKXRCB','MIXVT','DDXKIXP','RRXKKR','SRHXCSK','RCBXKL','VTXKIXP',
         'DDXMI','CSKXKKR','RRXRCB','KIXPXKL','VTXDD','RCBXMI','SRHXKKR','RRXCSK','KIXPXDD','KLXVT','MIXKKR', 'SRHXRR',
         'KXIPXCSK','RCBXKKR','KLXSRH','DDXCSK','RRXKL','VTXRCB','KKRXDD','CSKXMI','KIXPXRR','SRHXRCB','DDXKL','KKRXKIXP',
         'VTXRR','SRHXMI','KLXCSK','RCBXDD','KIXPXMI','SRHXVT','KLXKKR','DDXRR','CSKXSRH','MIXKL','KIXPXRCB','DDXVT','SRHXRR',
         'KKRXKL','MIXKIXP','DDXSRH','RCBXCSK','RRXVT','KKRXMI','SRHXKIXP','CSKXKL','DDXRCB','MIXSRH','KIXPXRR','VTXKKR',
         'MIXCSK','SRHXDD','KKRXRCB','VTXKL','RRXMI','CSKXKIXP','DDXKKR','KLXRCB','VTXSRH','RRXDD','KLXMI','KKRXCSK','KIXPXVT',
         'MIXRCB','RRXKL','VTXCSK','KIXPXSRH','KKRXRR','RCBXVT','MIXDD','CSKXRR','KIXPXKKR','RCBXSRH','VTXMI','KLXDD','RCBXRR',
         'KKRXSRH','KLXKIXP','CSKXVT']
print(len(matches))
dates=['25-03-2020','26-03-20','26-03-20','27-03-20','27-03-20','28-03-20','28-03-20','29-03-20','29-03-20','1-04-2020','01-04-2020'
       ,'02','02','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','11','12','12','13','13','14','14','15','15',
       '16','16','17','17','18','18','19','19','20','20','21','21','22','22','23','24','24','25','26','26','27','27','28','28','30','30',
       '31','31','01-05-2020','01-05-2020','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','11','12','12']
print(len(dates))
venue=['Chennai','Bangalore','Mumbai','Hyderabad','Kolkata','Chennai','Mumbai','Delhi','Rajasthan','Hyderabad','Bangalore','Visakhapatanam',
       'Delhi','Chennai','Rajasthan','Punjab','Visakhapatanam','Bangalore','Hyderabad','Rajasthan','Punjab','Kerala','Mumbai','Hyderabad',
       'Punjab','Bangalore','Kerala','Delhi','Rajasthan','Visakhapatanam','Kolkata','Chennai','Punjab','Hyderabad','Delhi','Kolkata',
       'Visakhapatanam','Hyderabad','Kerala','Bangalore','Punjab','Hyderabad','Kerala','Delhi','Chennai','Mumbai','Punjab','Delhi','Hyderabad',
       'Kolkata','Mumbai','Delhi','Bangalore','Rajasthan','Kolkata','Hyderabad','Chennai','Delhi','Mumbai','Punjab','Visakhapatana',
       'Mumbai','Hyderabad','Kolkata','Visakhapatanam','Rajasthan','Chennai','Delhi','Kerala','Visakhapatanam','Rajasthan','Kerala','Kolkata',
       'Punjab','Mumbai','Rajasthan','Visakhapatanam','Punjab','Kolkata','Bangalore','Mumbai','Chennai','Punjab','Bangalore','Visakhapatanam','Kerala',
       'Bangalore','Kolkata','Kerala','Chennai']
print(len(venue))
e=[]
for i in range(1,91):
    e.append(i)

it=iter(matches)
it1=iter(e)
l=list(zip(e, matches, dates, venue))
print(l)