# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activ.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_2.addWidget(self.calendarWidget)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.b_selectExcel = QtWidgets.QPushButton(self.groupBox_2)
        self.b_selectExcel.setMaximumSize(QtCore.QSize(110, 16777215))
        self.b_selectExcel.setObjectName("b_selectExcel")
        self.horizontalLayout_4.addWidget(self.b_selectExcel)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.l_ename = QtWidgets.QLineEdit(self.groupBox_2)
        self.l_ename.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.l_ename.setObjectName("l_ename")
        self.horizontalLayout_4.addWidget(self.l_ename)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, 0, 100, -1)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.b_selectItem = QtWidgets.QPushButton(self.groupBox_2)
        self.b_selectItem.setObjectName("b_selectItem")
        self.horizontalLayout_6.addWidget(self.b_selectItem)
        self.b_selectCard = QtWidgets.QPushButton(self.groupBox_2)
        self.b_selectCard.setObjectName("b_selectCard")
        self.horizontalLayout_6.addWidget(self.b_selectCard)
        self.line_5 = QtWidgets.QFrame(self.groupBox_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_6.addWidget(self.line_5)
        self.b_load = QtWidgets.QPushButton(self.groupBox_2)
        self.b_load.setObjectName("b_load")
        self.horizontalLayout_6.addWidget(self.b_load)
        self.b_compare = QtWidgets.QPushButton(self.groupBox_2)
        self.b_compare.setObjectName("b_compare")
        self.horizontalLayout_6.addWidget(self.b_compare)
        self.b_value = QtWidgets.QPushButton(self.groupBox_2)
        self.b_value.setObjectName("b_value")
        self.horizontalLayout_6.addWidget(self.b_value)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(100)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_8.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_8.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_8.addWidget(self.checkBox_3)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(30)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.c_xiangxi = QtWidgets.QCheckBox(self.groupBox_3)
        self.c_xiangxi.setChecked(True)
        self.c_xiangxi.setTristate(False)
        self.c_xiangxi.setObjectName("c_xiangxi")
        self.horizontalLayout_9.addWidget(self.c_xiangxi)
        self.c_suonlue = QtWidgets.QCheckBox(self.groupBox_3)
        self.c_suonlue.setObjectName("c_suonlue")
        self.horizontalLayout_9.addWidget(self.c_suonlue)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName("tabWidget")
        self.t_1 = QtWidgets.QWidget()
        self.t_1.setObjectName("t_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.t_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.t_1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.t_1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.excel_1 = QtWidgets.QTableView(self.t_1)
        self.excel_1.setObjectName("excel_1")
        self.horizontalLayout_13.addWidget(self.excel_1)
        self.excel_2 = QtWidgets.QTableView(self.t_1)
        self.excel_2.setObjectName("excel_2")
        self.horizontalLayout_13.addWidget(self.excel_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.t_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView_3 = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_3.setMinimumSize(QtCore.QSize(0, 30))
        self.tableView_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tableView_3.setObjectName("tableView_3")
        self.verticalLayout_4.addWidget(self.tableView_3)
        self.tableView_4 = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_4.setMinimumSize(QtCore.QSize(0, 30))
        self.tableView_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tableView_4.setObjectName("tableView_4")
        self.verticalLayout_4.addWidget(self.tableView_4)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.groupBox_4)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout_4.addWidget(self.horizontalScrollBar)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.verticalLayout_5.setStretch(0, 10)
        self.verticalLayout_5.setStretch(1, 40)
        self.verticalLayout_5.setStretch(2, 5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "选择服务器："))
        self.comboBox.setItemText(0, _translate("MainWindow", "对外安卓测试服"))
        self.comboBox.setItemText(1, _translate("MainWindow", "对外IOS测试"))
        self.pushButton_4.setText(_translate("MainWindow", "OK"))
        self.pushButton_3.setText(_translate("MainWindow", "连接检查"))
        self.label.setText(_translate("MainWindow", "服务器时间："))
        self.pushButton.setText(_translate("MainWindow", "2020/01/25 15:25:50"))
        self.b_selectExcel.setText(_translate("MainWindow", "选择活动表"))
        self.label_6.setText(_translate("MainWindow", "输入活动表分页名称："))
        self.l_ename.setPlaceholderText(_translate("MainWindow", "不填默认Sheet1"))
        self.b_selectItem.setText(_translate("MainWindow", "选择道具配置表"))
        self.b_selectCard.setText(_translate("MainWindow", "选择究极卡配置表"))
        self.b_load.setText(_translate("MainWindow", "加载"))
        self.b_compare.setText(_translate("MainWindow", "比对"))
        self.b_value.setText(_translate("MainWindow", "价值验证"))
        self.groupBox_3.setTitle(_translate("MainWindow", "对比结果"))
        self.checkBox.setText(_translate("MainWindow", "*"))
        self.checkBox_2.setText(_translate("MainWindow", "="))
        self.checkBox_3.setText(_translate("MainWindow", "≠"))
        self.c_xiangxi.setText(_translate("MainWindow", "详细"))
        self.c_suonlue.setText(_translate("MainWindow", "缩略"))
        self.label_7.setText(_translate("MainWindow", "服务器："))
        self.label_8.setText(_translate("MainWindow", "活动表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_1), _translate("MainWindow", "对比结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "历史对比结果"))
        self.groupBox_4.setTitle(_translate("MainWindow", "单行比对"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())