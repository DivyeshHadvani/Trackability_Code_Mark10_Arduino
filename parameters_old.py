# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameters.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import serial.tools.list_ports

class para(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # QtWidgets.QDialog.__init__(self)                                                            #           added by me for trial
        self.setObjectName("Dialog")
        self.resize(309, 336)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(309, 336))
        self.setMaximumSize(QtCore.QSize(309, 336))
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 100, 251, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.proximal_baude_label = QtWidgets.QLabel(self.groupBox_3)
        self.proximal_baude_label.setGeometry(QtCore.QRect(1, 47, 47, 16))
        self.proximal_baude_label.setObjectName("proximal_baude_label")
        self.proximal_baude = QtWidgets.QLineEdit(self.groupBox_3)
        self.proximal_baude.setGeometry(QtCore.QRect(110, 50, 133, 20))
        self.proximal_baude.setObjectName("proximal_baude")
        self.proximal_com = QtWidgets.QComboBox(self.groupBox_3)
        self.proximal_com.setGeometry(QtCore.QRect(110, 20, 60, 20))
        self.proximal_com.setObjectName("proximal_com")
        self.proximal_com.addItem("")
        self.proximal_com.addItem("")
        self.proximal_com_label = QtWidgets.QLabel(self.groupBox_3)
        self.proximal_com_label.setGeometry(QtCore.QRect(1, 21, 46, 16))
        self.proximal_com_label.setObjectName("proximal_com_label")
        self.roller_dia = QtWidgets.QLineEdit(self)
        self.roller_dia.setGeometry(QtCore.QRect(133, 188, 133, 20))
        self.roller_dia.setObjectName("roller_dia")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 188, 71, 16))
        self.label_7.setObjectName("label_7")
        self.roller_steps = QtWidgets.QLineEdit(self)
        self.roller_steps.setGeometry(QtCore.QRect(133, 214, 133, 20))
        self.roller_steps.setText("")
        self.roller_steps.setObjectName("roller_steps")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(20, 214, 107, 16))
        self.label_8.setObjectName("label_8")
        self.axis_steps = QtWidgets.QLineEdit(self)
        self.axis_steps.setGeometry(QtCore.QRect(133, 266, 133, 20))
        self.axis_steps.setText("")
        self.axis_steps.setObjectName("axis_steps")
        self.axis_pitch = QtWidgets.QLineEdit(self)
        self.axis_pitch.setGeometry(QtCore.QRect(133, 240, 133, 20))
        self.axis_pitch.setObjectName("axis_pitch")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(20, 266, 100, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 73, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 251, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.com_distal_label = QtWidgets.QLabel(self.groupBox_2)
        self.com_distal_label.setGeometry(QtCore.QRect(1, 21, 46, 16))
        self.com_distal_label.setObjectName("com_distal_label")
        self.distal_baude = QtWidgets.QLineEdit(self.groupBox_2)
        self.distal_baude.setGeometry(QtCore.QRect(110, 50, 133, 20))
        self.distal_baude.setObjectName("distal_baude")
        self.distal_baude_label = QtWidgets.QLabel(self.groupBox_2)
        self.distal_baude_label.setGeometry(QtCore.QRect(1, 47, 47, 16))
        self.distal_baude_label.setObjectName("distal_baude_label")
        self.distal_com = QtWidgets.QComboBox(self.groupBox_2)
        self.distal_com.setGeometry(QtCore.QRect(110, 20, 60, 20))
        self.distal_com.setObjectName("distal_com")
        self.distal_com.addItem("")
        self.distal_com.addItem("")
        self.save_parameters = QtWidgets.QPushButton(self)
        self.save_parameters.setGeometry(QtCore.QRect(190, 310, 75, 23))
        self.save_parameters.setObjectName("save_parameters")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.save_parameters.clicked.connect(self.save_all_para)   


    def save_all_para(self):
        self.all_parameters = {
        "distal_port":self.distal_com.currentText(),
        "distal_baude":self.distal_baude.text(),
        "proximal_port":self.proximal_com.currentText(),
        "proximal_baude":self.proximal_baude.text(),
        "roller_dia":self.roller_dia.text(),
        "roller_steps":self.roller_steps.text(),
        "axis_pitch":self.axis_pitch.text(),
        "axis_steps":self.axis_steps.text()
        }
        with open("parameters.pkl",'wb') as para_file:
            pickle.dump(self.all_parameters, para_file, pickle.HIGHEST_PROTOCOL)


    def load_para(self):
        try:
            print("Load para")
            with open("parameters.pkl",'rb') as para_file:
                self.all_parameters = pickle.load(para_file)  
            print(self.all_parameters)
            self.proximal_baude.setText(str(self.all_parameters['proximal_baude']))
            self.distal_baude.setText(str(self.all_parameters['distal_baude']))
            self.roller_dia.setText(self.all_parameters['roller_dia'])
            self.roller_steps.setText(self.all_parameters['roller_steps'])
            self.axis_pitch.setText(self.all_parameters['axis_pitch'])
            self.axis_steps.setText(self.all_parameters['axis_steps'])

        except:
            pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Parameters"))
        self.groupBox_3.setTitle(_translate("self", "Proximal force sensor"))
        self.proximal_baude_label.setText(_translate("self", "Baud rate"))
        self.proximal_com.setItemText(0, _translate("self", "COM11"))                       #   ("self", "COM11")   
        self.proximal_com.setItemText(1, _translate("self", "COM1"))                        #   ("self", "COM1")
        self.proximal_com_label.setText(_translate("self", "COM port"))
        self.label_7.setText(_translate("self", "Roller dia (mm)"))
        self.label_8.setText(_translate("self", "Roller motor steps/rev"))
        self.label_9.setText(_translate("self", "Axis motor steps/rev"))
        self.label_10.setText(_translate("self", "Axis pitch (mm)"))
        self.groupBox_2.setTitle(_translate("self", "Distal force sensor"))
        self.com_distal_label.setText(_translate("self", "COM port"))
        self.distal_baude_label.setText(_translate("self", "Baud rate"))
        self.distal_com.setItemText(0, _translate("self", "COM11"))
        self.distal_com.setItemText(1, _translate("self", "COM1"))
        self.save_parameters.setText(_translate("self", "Save"))

    def closeEvent(self, evnt):
        print("closing event")

    # def para_data(self):
    #     self.all_parameters = {
    #     "distal_port":"COM11",
    #     "distal_baud":9600,
    #     "proximal_port":"COM2",
    #     "proximal_baud":9600,
    #     "roller_dia":25,
    #     "roller_steps":25600,
    #     "axis_pitch":1,
    #     "axis_steps":25600
    #     }

    def find_devices(self):
        self.proximal_com.clear()
        self.distal_com.clear()
        connected = []
        comlist = serial.tools.list_ports.comports()
        for element in comlist:
            connected.append(element.device)
            self.proximal_com.addItem(element.device)
            self.distal_com.addItem(element.device)
        try:
            self.proximal_com.setCurrentIndex(connected.index(self.all_parameters['proximal_port']))
        except:
            pass
        try:
            self.distal_com.setCurrentIndex(connected.index(self.all_parameters['distal_port']))
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = para()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())