#用类
# class

#面向对象编程
#面向过程编程

#执行者
#1、4s店，买车
#2、保险公司
#3、税务局 
#4、交管所 上牌

#1、买车处 -》指挥者
    #1、4s店，买车
    #2、保险公司
    #3、税务局 
    #4、交管所 上牌
def buyCar():
    print('买车')
def baoxian():
    print('保险')
def jiaoshui():
    print('交税')
def shangpai():
    print('上牌')
# buyCar()
# baoxian()
# jiaoshui()
# shangpai()


class BuyCar:
    def buyCar(self,):
        print('买车')

    def baoxian(self,):
        print('保险')

    def jiaoshui(self,):
        print('交税')
    def shangpai(self):
        print('上牌')

xw = BuyCar()
xw.buyCar()
xw.buyCar()
xw.baoxian()
xw.jiaoshui()
xw.shangpai()