import enum
class Days(enum.Enum):
    sun=1
    mon=2

print(repr(Days.sun))
print(Days.mon.name)
if Days.mon.name=="on":
    print("yes")
for w in Days:
    print(w)
# class ravi:
#     sun=1
#     mon=2
#
# print(ravi.mon.name)