import functools
import math

def chuanHoa(s):
    arr = s.split()
    res = ""
    for i in arr:
        res += i + " "
    return res.strip()

class ThiSinh:
    def __init__(self, maThiSinh, hoTen, diemThi, danToc, khuVuc):
        self.maThiSinh = "TS{0:0>2}".format(maThiSinh)
        self.hoTen = chuanHoa(hoTen.title())
        self.diemThi = diemThi
        self.danToc = danToc
        self.khuVuc = khuVuc

    def diemUuTienTheoKhuVuc(self):
        if self.khuVuc == "1":
            return 1.5
        elif self.khuVuc == "2":
            return 1.0
        else:
            return 0.0

    def diemUuTienTheoDanToc(self):
        if self.danToc != "Kinh":
            return 1.5
        else:
            return 0.0

    def tongDiem(self):
        return self.diemThi + self.diemUuTienTheoKhuVuc() + self.diemUuTienTheoDanToc()

    def tinhTrang(self):
        if self.tongDiem() >= 20.5:
            return "Do"
        else:
            return "Truot"

    def inThiSinh(self):
        print(self.maThiSinh, self.hoTen, "{:.1f}".format(self.tongDiem()), self.tinhTrang())

def cmp(a, b):
    if a.tongDiem() != b.tongDiem():
        if a.tongDiem() > b.tongDiem():
            return -1
        return 1
    else:
        if a.maThiSinh < b.maThiSinh:
            return -1
        return 1

n = int(input())
listThiSinh = []
for i in range(n):
    s1 = input()
    s2 = float(input())
    s3 = input()
    s4 = input()
    listThiSinh.append(ThiSinh(i + 1, s1, s2, s3, s4))

listThiSinh = sorted(listThiSinh, key = functools.cmp_to_key(cmp))
for i in listThiSinh:
    i.inThiSinh()