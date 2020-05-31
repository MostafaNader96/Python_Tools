# -*- coding: utf-8 -*-

#################################################################################
## Form generated from reading UI file 'Print.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#################################################################################
## DIO_Configuration tool generates a _confih.h file including the configurations
## of the 32 pins included in the atmega32 microcontroller according to the users
## choice between the configuration parameters and saved this file in a path 
## chosen by the user.
## All the configurations are choses through a simple GUI
#################################################################################



from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt,SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import sys
        
textA0='#define DIO_PORTA_u8PIN0_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA1='#define DIO_PORTA_u8PIN1_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA2='#define DIO_PORTA_u8PIN2_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA3='#define DIO_PORTA_u8PIN3_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA4='#define DIO_PORTA_u8PIN4_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA5='#define DIO_PORTA_u8PIN5_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA6='#define DIO_PORTA_u8PIN6_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textA7='#define DIO_PORTA_u8PIN7_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'

textB0='#define DIO_PORTB_u8PIN0_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB1='#define DIO_PORTB_u8PIN1_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB2='#define DIO_PORTB_u8PIN2_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB3='#define DIO_PORTB_u8PIN3_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB4='#define DIO_PORTB_u8PIN4_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB5='#define DIO_PORTB_u8PIN5_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB6='#define DIO_PORTB_u8PIN6_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textB7='#define DIO_PORTB_u8PIN7_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'

textC0='#define DIO_PORTC_u8PIN0_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC1='#define DIO_PORTC_u8PIN1_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC2='#define DIO_PORTC_u8PIN2_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC3='#define DIO_PORTC_u8PIN3_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC4='#define DIO_PORTC_u8PIN4_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC5='#define DIO_PORTC_u8PIN5_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC6='#define DIO_PORTC_u8PIN6_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textC7='#define DIO_PORTC_u8PIN7_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'

textD0='#define DIO_PORTD_u8PIN0_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD1='#define DIO_PORTD_u8PIN1_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD2='#define DIO_PORTD_u8PIN2_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD3='#define DIO_PORTD_u8PIN3_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD4='#define DIO_PORTD_u8PIN4_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD5='#define DIO_PORTD_u8PIN5_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD6='#define DIO_PORTD_u8PIN6_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
textD7='#define DIO_PORTD_u8PIN7_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
        
listtt=[textA0,textA1,textA2,textA3,textA4,textA5,textA6,textA7,textB0,textB1,textB2,textB3,textB4,textB5,textB6,textB7,textC0,textC1,textC2,textC3,textC4,textC5,textC6,textC7,textD0,textD1,textD2,textD3,textD4,textD5,textD6,textD7]

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 439)
        self.pin0_groupbox = QGroupBox(Form)
        self.pin0_groupbox.setObjectName(u"pin0_groupbox")
        self.pin0_groupbox.setGeometry(QRect(30, 10, 441, 211))
        self.outputinput_groupBox = QGroupBox(self.pin0_groupbox)
        self.outputinput_groupBox.setObjectName(u"outputinput_groupBox")
        self.outputinput_groupBox.setGeometry(QRect(10, 20, 120, 80))
        self.output_radioButton = QRadioButton(self.outputinput_groupBox)
        self.output_radioButton.setObjectName(u"output_radioButton")
        self.output_radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.input_radioButton = QRadioButton(self.outputinput_groupBox)
        self.input_radioButton.setObjectName(u"input_radioButton")
        self.input_radioButton.setGeometry(QRect(20, 50, 83, 18))
        self.input_radioButton.setChecked(True)
        self.opconfiguration_groupBox = QGroupBox(self.pin0_groupbox)
        self.opconfiguration_groupBox.setObjectName(u"opconfiguration_groupBox")
        self.opconfiguration_groupBox.setEnabled(False)
        self.opconfiguration_groupBox.setGeometry(QRect(180, 20, 120, 80))
        self.high_radiobutton = QRadioButton(self.opconfiguration_groupBox)
        self.high_radiobutton.setObjectName(u"high_radiobutton")
        self.high_radiobutton.setGeometry(QRect(20, 20, 83, 18))
        self.low_radioButton = QRadioButton(self.opconfiguration_groupBox)
        self.low_radioButton.setObjectName(u"low_radioButton")
        self.low_radioButton.setGeometry(QRect(20, 50, 83, 18))
        self.low_radioButton.setChecked(True)
        self.ipconfiguration_groupBox = QGroupBox(self.pin0_groupbox)
        self.ipconfiguration_groupBox.setObjectName(u"ipconfiguration_groupBox")
        self.ipconfiguration_groupBox.setGeometry(QRect(180, 120, 120, 80))
        self.pur_radioButton = QRadioButton(self.ipconfiguration_groupBox)
        self.pur_radioButton.setObjectName(u"pur_radioButton")
        self.pur_radioButton.setGeometry(QRect(10, 20, 83, 18))
        self.highimpedance_radioButton = QRadioButton(self.ipconfiguration_groupBox)
        self.highimpedance_radioButton.setObjectName(u"highimpedance_radioButton")
        self.highimpedance_radioButton.setGeometry(QRect(10, 50, 111, 18))
        self.highimpedance_radioButton.setChecked(True)
        self.pinname_lineedit = QLineEdit(self.pin0_groupbox)
        self.pinname_lineedit.setObjectName(u"pinname_lineedit")
        self.pinname_lineedit.setEnabled(False)
        self.pinname_lineedit.setGeometry(QRect(10, 140, 113, 20))
        self.defaultname_checkBox = QCheckBox(self.pin0_groupbox)
        self.defaultname_checkBox.setObjectName(u"defaultname_checkBox")
        self.defaultname_checkBox.setGeometry(QRect(10, 170, 121, 18))
        self.defaultname_checkBox.setChecked(True)
        self.PORT_comboBox = QComboBox(self.pin0_groupbox)
        self.PORT_comboBox.setObjectName(u"PORT_comboBox")
        self.PORT_comboBox.setGeometry(QRect(310, 50, 62, 22))
        self.PIN_comboBox = QComboBox(self.pin0_groupbox)
        self.PIN_comboBox.setObjectName(u"PIN_comboBox")
        self.PIN_comboBox.setGeometry(QRect(310, 120, 62, 22))
        self.lineEdit = QLineEdit(self.pin0_groupbox)
        self.PIN_comboBox.addItem("0")
        self.PIN_comboBox.addItem("1")
        self.PIN_comboBox.addItem("2")
        self.PIN_comboBox.addItem("3")
        self.PIN_comboBox.addItem("4")
        self.PIN_comboBox.addItem("5")
        self.PIN_comboBox.addItem("6")
        self.PIN_comboBox.addItem("7")
        
        self.PORT_comboBox.addItem("PORTA")
        self.PORT_comboBox.addItem("PORTB")
        self.PORT_comboBox.addItem("PORTC")
        self.PORT_comboBox.addItem("PORTD")

        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 20, 111, 20))
        self.lineEdit_2 = QLineEdit(self.pin0_groupbox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 80, 111, 20))
        self.path_lineEdit = QLineEdit(Form)
        self.path_lineEdit.setObjectName(u"path_lineEdit")
        self.path_lineEdit.setGeometry(QRect(500, 60, 281, 20))
        self.generate_pushButton = QPushButton(Form)
        self.generate_pushButton.setObjectName(u"generate_pushButton")
        self.generate_pushButton.setGeometry(QRect(520, 90, 241, 121))

        self.retranslateUi(Form)
        QObject.connect(self.output_radioButton,SIGNAL("clicked(bool)"),self.opconfiguration_groupBox.setEnabled)
        QObject.connect(self.output_radioButton,SIGNAL("clicked(bool)"),self.ipconfiguration_groupBox.setDisabled)
        QObject.connect(self.input_radioButton,SIGNAL("clicked(bool)"),self.opconfiguration_groupBox.setDisabled)
        QObject.connect(self.input_radioButton,SIGNAL("clicked(bool)"),self.ipconfiguration_groupBox.setEnabled)
        QObject.connect(self.defaultname_checkBox,SIGNAL("clicked(bool)"),self.pinname_lineedit.setDisabled)
        self.PIN_comboBox.activated.connect(self.pinn1)
        self.generate_pushButton.clicked.connect(self.GenerateFunction)


        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    def pinn1(self):
      if self.PORT_comboBox.currentText()=='PORTA': 
        if self.PIN_comboBox.currentText()=='0':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA0='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA0='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA0='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA0='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[0]=textA0
      
        if self.PIN_comboBox.currentText()=='1':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA1='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA1='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA1='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA1='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[1]=textA1
      
        if self.PIN_comboBox.currentText()=='2':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA2='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA2='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA2='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA2='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[2]=textA2
  
  
        if self.PIN_comboBox.currentText()=='3':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA3='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA3='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA3='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA3='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[3]=textA3
  
  
        if self.PIN_comboBox.currentText()=='4':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA4='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA4='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA4='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA4='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[4]=textA4
  
  
        if self.PIN_comboBox.currentText()=='5':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA5='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA5='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA5='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA5='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[5]=textA5
  
  
        if self.PIN_comboBox.currentText()=='6':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA6='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA6='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA6='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA6='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[6]=textA6
  
  
        if self.PIN_comboBox.currentText()=='7':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textA7='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textA7='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA7='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textA7='#define DIO_PORTA_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[7]=textA7


      if self.PORT_comboBox.currentText()=='PORTB': 
        if self.PIN_comboBox.currentText()=='0':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB0='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB0='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB0='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB0='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[8]=textB0
      
        if self.PIN_comboBox.currentText()=='1':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB1='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB1='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textA1='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB1='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[9]=textB1
      
        if self.PIN_comboBox.currentText()=='2':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB2='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB2='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB2='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB2='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[10]=textB2
  
  
        if self.PIN_comboBox.currentText()=='3':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB3='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB3='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB3='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB3='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[11]=textB3
  
  
        if self.PIN_comboBox.currentText()=='4':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB4='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB4='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB4='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB4='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[12]=textB4
  
  
        if self.PIN_comboBox.currentText()=='5':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB5='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB5='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB5='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB5='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[13]=textB5
  
  
        if self.PIN_comboBox.currentText()=='6':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB6='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB6='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB6='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB6='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[14]=textB6
  
  
        if self.PIN_comboBox.currentText()=='7':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textB7='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textB7='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textB7='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textB7='#define DIO_PORTB_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[15]=textB7
          
        
      if self.PORT_comboBox.currentText()=='PORTC': 
        if self.PIN_comboBox.currentText()=='0':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC0='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC0='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC0='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC0='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[16]=textC0
      
        if self.PIN_comboBox.currentText()=='1':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC1='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC1='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC1='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC1='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[17]=textC1
      
        if self.PIN_comboBox.currentText()=='2':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC2='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC2='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC2='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC2='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[18]=textC2
  
  
        if self.PIN_comboBox.currentText()=='3':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC3='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC3='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC3='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC3='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[19]=textC3
  
  
        if self.PIN_comboBox.currentText()=='4':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC4='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC4='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC4='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC4='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[20]=textC4
  
  
        if self.PIN_comboBox.currentText()=='5':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC5='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC5='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC5='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC5='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[21]=textC5
  
  
        if self.PIN_comboBox.currentText()=='6':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC6='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC6='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC6='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC6='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[22]=textC6
  
  
        if self.PIN_comboBox.currentText()=='7':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textC7='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textC7='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textC7='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textC7='#define DIO_PORTC_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[23]=textC7

      if self.PORT_comboBox.currentText()=='PORTD': 
        if self.PIN_comboBox.currentText()=='0':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD0='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD0='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD0='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD0='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(0)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[24]=textD0
      
        if self.PIN_comboBox.currentText()=='1':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD1='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD1='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD1='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD1='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(1)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[25]=textD1
      
        if self.PIN_comboBox.currentText()=='2':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD2='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD2='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD2='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD2='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(2)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[26]=textD2
  
  
        if self.PIN_comboBox.currentText()=='3':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD3='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD3='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD3='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD3='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(3)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[27]=textD3
  
  
        if self.PIN_comboBox.currentText()=='4':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD4='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD4='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD4='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD4='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[28]=textD4
  
  
        if self.PIN_comboBox.currentText()=='5':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD5='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD5='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD5='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD5='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(5)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[29]=textD5
  
  
        if self.PIN_comboBox.currentText()=='6':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD6='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD6='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD6='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD6='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(6)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[30]=textD6
  
  
        if self.PIN_comboBox.currentText()=='7':
          if self.output_radioButton.isChecked():
            if self.high_radiobutton.isChecked():
              textD7='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_HIGH'
            else:
              textD7='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8OUTPUT_LOW'
          else:
            if self.pur_radioButton.isChecked():
              textD7='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_PULLUP'
            else:
              textD7='#define DIO_PORTD_u8PIN'+self.PIN_comboBox.itemText(7)+'_MODE  DIO_u8INPUT_HIGH_IMPEDANCE'
          listtt[31]=textD7
          
    
    
    def GenerateFunction(self):
       # MFIC_Handler=open(self.path_lineEdit.text()+ r'\MFIC.h','r+')
        DIO_Handler=open(self.path_lineEdit.text()+ r'\DIO_config.h','w')
        
        #print(listtt[0])
        #print(listtt[1])
        #print(listtt[2])
        
        DIO_Handler.write(listtt[0]+"\n"+listtt[1]+"\n"+listtt[2]+"\n"+listtt[3]+"\n"+listtt[4]+"\n"+listtt[5]+"\n"+listtt[6]+"\n"+listtt[7]+"\n"+"\n"+
        listtt[8]+"\n"+listtt[9]+"\n"+listtt[10]+"\n"+listtt[11]+"\n"+listtt[12]+"\n"+listtt[13]+"\n"+listtt[14]+"\n"+listtt[15]+"\n"+"\n"+
        listtt[16]+"\n"+listtt[17]+"\n"+listtt[18]+"\n"+listtt[19]+"\n"+listtt[20]+"\n"+listtt[21]+"\n"+listtt[22]+"\n"+listtt[23]+"\n"+"\n"+
        listtt[24]+"\n"+listtt[25]+"\n"+listtt[26]+"\n"+listtt[27]+"\n"+listtt[28]+"\n"+listtt[29]+"\n"+listtt[30]+"\n"+listtt[31])



        #if self.output_radioButton.isChecked():
       #   if self.high_radiobutton.isChecked():
      #      DIO_Handler.write('#define DIO_u8PIN'+self.PIN_comboBox.itemText(4)+'_MODE  DIO_u8OUTPUT_HIGH')
          #else:
         #   DIO_Handler.write('#define DIO_u8PIN_MODE  DIO_u8OUTPUT_LOW')
        #else:
       #   if self.pur_radioButton.isChecked():
           # DIO_Handler.write('#define DIO_u8PIN0_MODE  DIO_u8INPUT_PULLUP')
          #else:
         #   DIO_Handler.write('#define DIO_u8PIN0_MODE  DIO_u8INPUT_HIGH_IMPEDANCE')
        #
        #if self.defaultname_checkBox.isChecked():
         # MFIC_Handler.write('#define DIO_u8PIN0  0')
        #else:
       #   MFIC_Handler.write('#define  ' + self.pinname_lineedit.text() +  '  0')
            
        #MFIC_Handler.close()
        DIO_Handler.close()
    # GenerateFunction

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simple Tool", None))
        self.pin0_groupbox.setTitle(QCoreApplication.translate("Form", u"Pin Configuration", None))
        self.outputinput_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.output_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.input_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.opconfiguration_groupBox.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.high_radiobutton.setText(QCoreApplication.translate("Form", u"High", None))
        self.low_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.ipconfiguration_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pur_radioButton.setText(QCoreApplication.translate("Form", u"PUR", None))
        self.highimpedance_radioButton.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.pinname_lineedit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.defaultname_checkBox.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.PORT_comboBox.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.PORT_comboBox.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.PORT_comboBox.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.PORT_comboBox.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.lineEdit.setText(QCoreApplication.translate("Form", u"Choose Port Number", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"Choose Pin Number", None))
        self.path_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path", None))
        self.generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
    # retranslateUi

    
    
app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())


