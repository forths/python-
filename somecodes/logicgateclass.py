# -*- coding:utf-8 -*-
# 简单继承
class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    """
    此时,我们并不会执行 performGateLogic 函数,因为我们不知道每个逻辑门将会怎样执行它
    的逻辑操作。这些细节将会包含在每一个被加入到阶层架构的门中,这是一个非常强大的面向对象
    编程思想。我们在写一个使用了尚不存在的代码的方法。参数 self 是实际门调用这个方法的一个引
    用。任何新加入阶层架构的逻辑门只需要执行 performGateLogic 函数,它便会在适当的时候被使
    用。一旦完成,门就可以提供它的输出值。这种可以扩展现存阶层架构并且为需要使用新类的阶层
    架构提供具体功能的能力对再利用现存代码来说是非常重要的。
    """
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
"""
这些类的构造器都开始于一个对于使用父函数的
__init__方法的父类构造器的精确访问。当创建一个 BinaryGate 类的示例的时候,
我们首先希望初始化所有从 LogicGate 继承的数据项。这种情况下,即是门的标签。
之后构造器继续添加两条输入行(pinA 和 pinB)。这是一个我们在构建类的阶层架构时应当使用的非常普遍的模式。
子类构造器需要访问父类构造器然后再转移到它们自己的有区分度的数据上。
Python 还有一个函数名为 super,这是一个可以用来代替对父类精确命名的函数。这是一个更
为普遍的机制,也被广泛使用,尤其是当一个类有不止一个父类时。但是我们不准备在这个介绍中
讨论它。比如在我们上面的例子中,LogicGate.__init__(self,n) 可以被替换为
super(UnaryGate,self).__init__(n)。
BinaryGate 类唯一增加的一个性能是从两条输入行得到值的能力。由于这些值来自某些外部
空间,我们便很简单地要求用户通过一个输入声明来提供它们。同样的执行过程也发生在 UnaryGate
类中,只不过在这一过程中只有一条输入行。
"""
class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
# 非门
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

"""
既然我们已经掌握了基本的门类操作,接下来便可以创建组合逻辑电路了。组合逻辑电路需要
把各个门组合连接起来,让一个门的计算结果流入另一个门成为输入值。为了实现这个操作,我们
将执行一个新的类,叫做 Connector。
Connector 类并不属于门的阶层架构,而是在其两端分别含有门层。这种关系是
面向对象的编程中十分重要的关系,叫做“HAS-A”关系,即非继承关系。在这里复习一下之前学过
的“IS-A”关系,也即继承关系,是指子类与父类的相似性,如 UnaryGate 和 LogicGate。
"""
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate


if __name__ == "__main__":
    g1 = AndGate("G1")
    print(g1.getOutput())

