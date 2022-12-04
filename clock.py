import Ui_clock, sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import configparser

color = "black"



app = QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QMainWindow()
ui = Ui_clock.Ui_MainWindow()
ui.setupUi(baseWidget)






# 获取当前时间
def get_gettime():
    time1 = time.strftime("%H:%M:%S", time.localtime())
    # date = time.strftime("%m{}%d{}", time.gmtime()).format("月", "日")
    return time1


def up_time():
    ui.label.setText(get_gettime())


def change_color():
    global color
    if color == "black":
        color = "white"
        ui.label.setStyleSheet("color:white;")
    elif color == "white":
        color = "black"
        ui.label.setStyleSheet("color:black;")


# 定时器
timer = QtCore.QTimer()
timer.timeout.connect(up_time)
timer.start(500)




def change_potision():
    win_settings.show()

def quitApp():
    # 关闭窗体程序
    QCoreApplication.instance().quit()


a0 = QAction("桌面时钟")
a1 = QAction("————")
a2 = QAction("切换颜色", triggered=change_color)
a3 = QAction("退出时钟", triggered=quitApp)

Menu = QMenu()
Menu.addAction(a0)
Menu.addAction(a1)
Menu.addAction(a2)
Menu.addAction(a3)
tp = QSystemTrayIcon(baseWidget)
tp.setContextMenu(Menu)
tp.setIcon(QIcon(":/png/res/clock.png"))

def init_config():
    # 确认配置文件是否存在
    try:
        f = open("setting.ini")
        f.close()
    except IOError:
        # 创建配置
        config = configparser.ConfigParser()
        # 加载配置
        config['setting'] = {'x': '5',
                            'y': '5'
                            }
        # 创建ini文件
        with open('setting.ini', 'w') as configfile:
            # 写入配置
            config.write(configfile)


def read_config():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read("setting.ini", encoding='utf-8')
    dict1 = dict(config.items('setting'))
    # 返回字典
    return dict1




def clock_init():
    # 设置窗口无边框
    baseWidget.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.SplashScreen)
    # 设置窗口透明
    baseWidget.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    # 获取配置
    init_config()
    a = read_config()
    x = int(a['x'])
    y = int(a['y'])
    # 设置窗口位置
    baseWidget.move(x, y)



clock_init()


# 托盘和主窗口放置
tp.show()
baseWidget.show()
sys.exit(app.exec_())
