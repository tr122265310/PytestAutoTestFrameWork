"""
------------------------------------
@Time : 2019/4/12 12:28
@Auth : linux超
@File : HomePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from Page.BasePage import BasePage, cf

# ---------------------------------------------------------------------------------
# 页面元素
# homePage = ('id', '_mail_tabitem_0_3text') # 首页
# mailList = ('id', '_mail_tabitem_1_4text')  # 通讯录
# applicationCenter = ('id', '_mail_tabitem_2_5text') # 应用中心
# inBox = ('id', '_mail_tabitem_3_6text')
# 配置文件读取元素
homePage = cf.getLocatorsOrAccount('HomePageElements', 'homePage')
mailList = cf.getLocatorsOrAccount('HomePageElements', 'mailList')
applicationCenter = cf.getLocatorsOrAccount('HomePageElements', 'applicationCenter')
inBox = cf.getLocatorsOrAccount('HomePageElements', 'inBox')
# ---------------------------------------------------------------------------------

class HomePage(BasePage):

    '''首页菜单选项'''
    def selectMenu(self, Menu='mailList'):

        if Menu == 'mailList':
            self.click(*mailList)
        elif Menu == 'homePage':
            self.click(*homePage)
        elif Menu == 'applicationCenter':
            self.click(*applicationCenter)
        elif Menu == 'inBox':
            self.click(*inBox)
        else:
            raise ValueError('''
            菜单选择错误!
            homePage->首页
            mailList->通讯录
            applicationCenter->应用中心
            inBox->收件箱''')

if __name__=='__main__':
    from selenium import webdriver
    from Page.PageObject.LoginPage import LoginPage
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login('账号', 'xiaochao11520')

    home = HomePage(driver)
    home.selectMenu()
