# -*- coding:utf-8 -*-

class Fraction():
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    # 操作符
    def __add__(self,other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common, newden//common)
    # 判断两个分数相等。我们可以通过重建_eq_方法来建立深相等——即一种数值上相等,却并不一定是相
    # 同指向的相等方式。_eq_方法是另一种在很多类中均可用的标准方法。_eq_方法比较两个对象,若
    # 它们在数值上相等就返回真值,否则就返回假值。
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    def __lt__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    def __gt__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum
    # 打印结果print
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

# 约分,欧几里得算法，对于两个整数m,n，如果n能整除m，那么就将n除以m的结果作为新的n，如果n不能再整除m,那么最大公因数
    # 就是n或者m被n整除的余数。只适用于分母为正数的情况。
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

if __name__ == "__main__":
    myfraction = Fraction(1,4)
    otherfraction = Fraction(1,4)
    # 打印处理
    print(myfraction)
    # 加法处理
    print(myfraction + otherfraction)
    print("相等",myfraction == otherfraction)
    print("小于",myfraction < otherfraction)
