import sys
import rpy2.robjects as robjects
from PyQt4 import QtGui, QtCore
from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.setGeometry(230,130,900,500)
window.show()

dialog = QtGui.QDialog()
ui2 = Ui_Dialog2()
ui2.setupUi(dialog)

dialog2 = QtGui.QDialog()
ui3 = Ui_Dialog2()
ui3.setupUi(dialog2)

dialog3 = QtGui.QDialog()
ui4 = Ui_Dialog2()
ui4.setupUi(dialog3)

def help():
    help = QtGui.QPixmap("help.png")
    scene = QtGui.QGraphicsScene(dialog)
    ui2.graphicsView.setScene(scene)
    scene.addPixmap(help)
    dialog.setGeometry(0,0,1200,680)
    dialog.setWindowTitle(_translate("Dialog", "Helper", None))
    dialog.show()

def show():
    pixmap = QtGui.QPixmap(ui.comboBox.currentText()+".png")
    scene = QtGui.QGraphicsScene(dialog2)
    ui3.graphicsView.setScene(scene)
    scene.addPixmap(pixmap)
    dialog2.setGeometry(200,115,1000,600)
    dialog2.setWindowTitle(_translate("Dialog", "OutPut", None))
    dialog2.show()

def fix():
    r = robjects.r

    r('sp = c()')
    r('po = c()')

    r('for(i in 1:100){ sp[i] = i}')
    tag = 0
    c1b = ui.lineEdit.text()
    if c1b.isdigit(): c1b = int(c1b)
    elif c1b != "": tag = 1
    robjects.globalenv['c1b'] = c1b
    c1k1 = ui.lineEdit_2.text()
    if c1k1.isdigit(): c1k1 = int(c1k1)
    elif c1k1 != "": tag = 1
    robjects.globalenv['c1k1'] = c1k1
    c2b = ui.lineEdit_3.text()
    if c2b.isdigit(): c2b = int(c2b)
    elif c2b != "": tag = 1
    robjects.globalenv['c2b'] = c2b
    c2k2 = ui.lineEdit_4.text()
    if c2k2.isdigit(): c2k2 = int(c2k2)
    elif c2k2 != "": tag = 1
    robjects.globalenv['c2k2'] = c2k2

    c1s = ui.lineEdit_5.text()
    if c1s.isdigit(): c1s = int(c1s)
    elif c1s != "": tag = 1
    robjects.globalenv['c1s'] = c1s
    ck1 = ui.lineEdit_6.text() 
    if ck1.isdigit(): ck1 = int(ck1)
    elif ck1 != "": tag = 1
    robjects.globalenv['ck1'] = ck1
    c2s = ui.lineEdit_7.text() 
    if c2s.isdigit(): c2s = int(c2s)
    elif c2s != "": tag = 1
    robjects.globalenv['c2s'] = c2s
    ck2 = ui.lineEdit_8.text() 
    if ck2.isdigit(): ck2 = int(ck2)
    elif ck2 != "": tag = 1
    robjects.globalenv['ck2'] = ck2

    p1b = ui.lineEdit_9.text()
    if p1b.isdigit(): p1b = int(p1b)
    elif p1b != "": tag = 1
    robjects.globalenv['p1b'] = p1b
    p1k1 = ui.lineEdit_10.text()
    if p1k1.isdigit(): p1k1 = int(p1k1)
    elif p1k1 != "": tag = 1
    robjects.globalenv['p1k1'] = p1k1
    p2b = ui.lineEdit_11.text()
    if p2b.isdigit(): p2b = int(p2b)
    elif p2b != "": tag = 1
    robjects.globalenv['p2b'] = p2b
    p2k2 = ui.lineEdit_12.text()
    if p2k2.isdigit(): p2k2 = int(p2k2)
    elif p2k2 != "": tag = 1
    robjects.globalenv['p2k2'] = p2k2
    
    p1s = ui.lineEdit_13.text()
    if p1s.isdigit(): p1s = int(p1s)
    elif p1s != "": tag = 1
    robjects.globalenv['p1s'] = p1s
    pk1 = ui.lineEdit_14.text() 
    if pk1.isdigit(): pk1 = int(pk1)
    elif pk1 != "": tag = 1
    robjects.globalenv['pk1'] = pk1
    p2s = ui.lineEdit_15.text() 
    if p2s.isdigit(): p2s = int(p2s)
    elif p2s != "": tag = 1
    robjects.globalenv['p2s'] = p2s
    pk2 = ui.lineEdit_16.text()  
    if pk2.isdigit(): pk2 = int(pk2)
    elif pk2 != "": tag = 1
    robjects.globalenv['pk2'] = pk2

    if(tag):
     msgBox = QtGui.QMessageBox()
     msgBox.setText("Only Integer Input is allowed");
     msgBox.setWindowTitle("WARNING !")
     msgBox.exec();   
 
    if(ui.comboBox.currentText() == "Bull Spread"):
     r('for(i in 1:c1k1){ po[i] = 0}')
     r('for(i in c1k1:ck1){ po[i] = sp[i] - c1k1}')
     r('for(i in ck1:100){ po[i] = ck1 - c1k1}')
     r('po = po - (c1b - c1s)')
     r('png("Bull Spread.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Bull Spread", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Bear Spread"):
     r('for(i in 1:ck1){ po[i] = c1k1 - ck1}')
     r('for(i in ck1:c1k1){ po[i] = c1k1 - sp[i]}')
     r('for(i in c1k1:100){ po[i] = 0}')
     r('po = po - (c1b - c1s)')
     r('png("Bear Spread.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Bear Spread", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Box Spread"):
     r('for(i in 1:c1k1){ po[i] = 0}')
     r('for(i in c1k1:ck1){ po[i] = sp[i] - c1k1}')
     r('for(i in ck1:100){ po[i] = ck1 - c1k1}')
     r('po = po - (c1b - c1s)')

     r('for(i in 1:pk1){ po[i] = po[i] + p1k1 - pk1}')
     r('for(i in pk1:p1k1){ po[i] = po[i] + p1k1 - sp[i]}')

     r('po = po - (p1b - p1s)')
     r('png("Box Spread.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Box Spread", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Butterfly Spread"):
     r('for(i in 1:c1k1){ po[i] = 0}')
     r('for(i in c1k1:ck1){ po[i] = sp[i] - c1k1}')
     r('for(i in ck1:100){ po[i] = ck1 - c1k1}')
     r('po = po - (c1b - c1s)')

     r('for(i in 1:ck1){ po[i] = po[i] + c2k2 - ck1}')
     r('for(i in ck1:c2k2){ po[i] = po[i] + c2k2 - sp[i]}')

     r('po = po - (c2b - c1s)')
     r('png("Butterfly Spread.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Butterfly Spread", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Straddle"):
     r('for(i in 1:c1k1){ po[i] = c1k1 - sp[i]}')
     r('for(i in c1k1:100){ po[i] = sp[i] - c1k1}')
     r('po = po - (c1b + p1b)')
     r('png("Straddle.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Straddle", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Strips"):
     r('for(i in 1:c1k1){ po[i] = 2*(c1k1 - sp[i])}')
     r('for(i in c1k1:100){ po[i] = sp[i] - c1k1}')
     r('po = po - (c1b + 2*p1b)')
     r('png("Strips.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Strips", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Straps"):
     r('for(i in 1:c1k1){ po[i] = c1k1 - sp[i]}')
     r('for(i in c1k1:100){ po[i] = 2*(sp[i] - c1k1)}')
     r('po = po - (2*c1b + p1b)') 
     r('png("Straps.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Straps", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

    elif(ui.comboBox.currentText() == "Strangle"):
     r('for(i in 1:p1k1){ po[i] = p1k1 - sp[i]}')
     r('for(i in p1k1:c1k1){ po[i] = 0}')
     r('for(i in c1k1:100){ po[i] = sp[i] - c1k1}')
     r('po = po - (c1b + p1b)')
     r('png("Strangle.png")')
     r('plot(sp, po, type="o", col="blue", lty=2, ann=FALSE)')
     r('box()')
     r('title(main = "Strangle", col.main = "green", font.main = 4)')
     r('title(xlab = "Stock Price", col.lab = "red", font.lab = 3.5)')
     r('title(ylab = "Pay Off", col.lab = "red", font.lab = 3.5)')
     r('dev.off()')

def tooltip():
#    if(ui.comboBox.currentText() == "Bull Spread"):
    msgBox = QtGui.QMessageBox()
    msgBox.setText(ui.comboBox.currentText());
    msgBox.setWindowTitle("What is"+ui.comboBox.currentText()+"!")
    msgBox.exec();

window.connect(ui.actionHelp, QtCore.SIGNAL("triggered()"),
                     help)

window.connect(ui.pushButton_2, QtCore.SIGNAL("clicked()"),
                     show)

window.connect(ui.pushButton, QtCore.SIGNAL("clicked()"),
                     fix)

window.connect(ui.toolButton, QtCore.SIGNAL("clicked()"),
                     tooltip)

sys.exit(app.exec_())
