class Ravi:
    def __init__(self, ravi):
        self._ravi=ravi
        self.__ra=ravi#PROTECTED VARIABLES

    def pr(self):
        print(self._ravi)


if __name__=="__main__":
    r=Ravi(1000)
    r.pr()
    print(r._ravi)
    try:
        print(r.__ravi)
    except AttributeError:
        print("PLEASE DON'T WITH PROTECTED VARIABLE(__)")
        print("FROM THE SOURCE https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python")