class Emp:
    def __init__(self, id, nm, sal):
        self.eid = id
        self.name = nm
        self.sal = sal
    def __str__(self):
        data = str(self.eid) +","+ (self.name) +","+ str(self.sal)
        return data

'''if (__name__ == '__main__'):
    e = Emp(111, "bam", 80000)
    print(e)'''