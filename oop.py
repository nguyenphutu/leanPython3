# ---------------

class hinh:

    def tinhCV(self):
        pass
    def tinhDT(self):
        pass


class hinhTron(hinh):

    def __init__(self,banKinh):
        self.banKinh = banKinh

    def tinhCV(self):
        return 2*3.14*self.banKinh

    def tinhDT(self):
        return 3.14*(self.banKinh**2)


class hinhCN(hinh):

    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong

    def tinhCV(self):
        return 2*(self.dai+self.rong)

    def tinhDT(self):
        return self.dai*self.rong

# test
htron = hinhTron(4)
print(htron.tinhCV())
print(htron.tinhDT())

hcn = hinhCN(10,5)
print(hcn.tinhCV())
print(hcn.tinhDT())



