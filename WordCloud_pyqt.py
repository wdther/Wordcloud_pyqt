from PyQt5.QtWidgets import *  #必须导入，否则会出错 -1073740791 (0xC0000409)
from Ui_WordCloud_pyqt import Ui_MainWindow # 【UI】指的是UI文件的文件名
#from UI_matpltest import Ui_MainWindow
import os
import sys

class PyQtLogic(QMainWindow, Ui_MainWindow):  #构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic,self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)   # #直接继承界面类，调用类的setupUi方法

    def colorchanged(self):
        self.Templatecolor.setChecked(0)

    def parainit(self):
        #self.para.a=1 错误用法，不存在这样的属性
        #self.a=1 正确用法，动态创建属性
        self.tc = self.Templatecolor.isChecked()
        self.swf= self.StatisWordFreq.isChecked()
        self.pscale = self.scale.value()
        self.number=self.spinBox.value()
        self.pheight=self.height.value()
        self.pwidth =self.width.value()
        self.pstopwords=self.stopwords.toPlainText()
        self.pcontour_width=self.contour_width.value()
        self.prelative_scaling=self.relative_scaling.value()
        self.pcolormap = self.colormap.currentText()
        sfont = self.FoncobotBox.currentText()

        if sfont == "宋体":
            self.font_path = "simsun.ttc"

        elif sfont == "楷体":
            self.font_path = "simkai.ttf"

        elif sfont == "行书":
            self.font_path = "STXINGKA.TTF"
        elif sfont == "Courier New":
            self.font_path = "cour.ttf"

        list = [('tc', self.tc),
                ('scale', self.pscale),
                ('font_path',self.font_path),
                ('number',self.number),
                ('width',self.pwidth),
                ('height',self.pheight),
                ('stopwords',self.pstopwords),
                ('contour_width',self.pcontour_width),
                ('colormap',self.pcolormap),
                ('relative_scaling',self.prelative_scaling),
                ('swf',self.swf)]

        self.para = dict(list) #将列表转化为字典


    def textbutton(self):
        #双引号可以不加转义字符
        #返回两个参数，文件名和文件类型
        self.txtfile,_ = QFileDialog.getOpenFileName(self,
                                                   '打开文件',
                                                   "./text/",
                                                   "txt files (*.txt)")
        print(self.txtfile)
        folder_path, file_name = os.path.split(self.txtfile)
        self.txtlineEdit.setText(file_name)



    def imagebutton(self):

        self.imgfile,_= QFileDialog.getOpenFileName(self,
                                                  '打开文件',
                                                  "./images/",
                                                  "Image files (*.jpg *.png *.gif)")
        folder_path, file_name = os.path.split(self.imgfile)
        self.imglineEdit.setText(file_name)

    def Cloudplot(self):  #调用格式 self.对象.MatplotlibWidget(QWidget)类中定义的方法
        self.parainit()

        if self.swf==1: #如果按照词频来绘制
            self.statistics.mpl.wordfreqplot(self.txtfile)
            self.tabWidget_2.setCurrentIndex(1)


        #self.mpl  是MyMplCanvas() 对象
        print(self.para)

        self.customwidget.mpl.wordcloud_plot(self.txtfile,self.imgfile,self.para)
        self.mytips.setPlainText("正在生成图像，请稍等...")


    def saveimg(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "Image Files (*.png)")
        self.customwidget.mpl.wc.to_file(fileName2)


if __name__ == "__main__":
    app = QApplication(sys.argv)   #pyqt窗口必须在QApplication方法中使用
    window = PyQtLogic() # 实例化类

    window.show()         #windows调用show方法
    sys.exit(app.exec_())  # #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序
