# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticketsupport.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Support(object):
    def setupUi(self, Support):
        Support.setObjectName("Support")
        Support.resize(838, 846)
        self.erstelleSupportticket = QtWidgets.QPushButton(Support)
        self.erstelleSupportticket.setGeometry(QtCore.QRect(610, 760, 171, 61))
        self.erstelleSupportticket.setObjectName("erstelleSupportticket")
        self.TicketNummer = QtWidgets.QLCDNumber(Support)
        self.TicketNummer.setGeometry(QtCore.QRect(760, 10, 64, 23))
        self.TicketNummer.setFrameShape(QtWidgets.QFrame.Panel)
        self.TicketNummer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TicketNummer.setProperty("value", 1.0)
        self.TicketNummer.setObjectName("TicketNummer")
        self.groupBoxKontakt = QtWidgets.QGroupBox(Support)
        self.groupBoxKontakt.setGeometry(QtCore.QRect(540, 50, 291, 321))
        self.groupBoxKontakt.setObjectName("groupBoxKontakt")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxKontakt)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Vorname = QtWidgets.QLabel(self.groupBoxKontakt)
        self.label_Vorname.setObjectName("label_Vorname")
        self.verticalLayout.addWidget(self.label_Vorname)
        self.lineEdit_Vorname = QtWidgets.QLineEdit(self.groupBoxKontakt)
        self.lineEdit_Vorname.setObjectName("lineEdit_Vorname")
        self.verticalLayout.addWidget(self.lineEdit_Vorname)
        self.label_Name = QtWidgets.QLabel(self.groupBoxKontakt)
        self.label_Name.setObjectName("label_Name")
        self.verticalLayout.addWidget(self.label_Name)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.groupBoxKontakt)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.verticalLayout.addWidget(self.lineEdit_Name)
        self.label_Baustelle = QtWidgets.QLabel(self.groupBoxKontakt)
        self.label_Baustelle.setObjectName("label_Baustelle")
        self.verticalLayout.addWidget(self.label_Baustelle)
        self.lineEdit_Baustelle = QtWidgets.QLineEdit(self.groupBoxKontakt)
        self.lineEdit_Baustelle.setObjectName("lineEdit_Baustelle")
        self.verticalLayout.addWidget(self.lineEdit_Baustelle)
        self.label_Bauprojekt = QtWidgets.QLabel(self.groupBoxKontakt)
        self.label_Bauprojekt.setObjectName("label_Bauprojekt")
        self.verticalLayout.addWidget(self.label_Bauprojekt)
        self.lineEdit_Bauprojekt = QtWidgets.QLineEdit(self.groupBoxKontakt)
        self.lineEdit_Bauprojekt.setObjectName("lineEdit_Bauprojekt")
        self.verticalLayout.addWidget(self.lineEdit_Bauprojekt)
        self.label_Telefonnummer = QtWidgets.QLabel(self.groupBoxKontakt)
        self.label_Telefonnummer.setObjectName("label_Telefonnummer")
        self.verticalLayout.addWidget(self.label_Telefonnummer)
        self.lineEdit_Telefonnummer = QtWidgets.QLineEdit(self.groupBoxKontakt)
        self.lineEdit_Telefonnummer.setObjectName("lineEdit_Telefonnummer")
        self.verticalLayout.addWidget(self.lineEdit_Telefonnummer)
        self.radioButtonWachmann = QtWidgets.QRadioButton(self.groupBoxKontakt)
        self.radioButtonWachmann.setObjectName("radioButtonWachmann")
        self.verticalLayout.addWidget(self.radioButtonWachmann)
        self.radioButtonLogistiker = QtWidgets.QRadioButton(
            self.groupBoxKontakt)
        self.radioButtonLogistiker.setObjectName("radioButtonLogistiker")
        self.verticalLayout.addWidget(self.radioButtonLogistiker)
        self.radioButton_Projektmanager = QtWidgets.QRadioButton(
            self.groupBoxKontakt)
        self.radioButton_Projektmanager.setObjectName(
            "radioButton_Projektmanager")
        self.verticalLayout.addWidget(self.radioButton_Projektmanager)
        self.groupBoxBestellungen = QtWidgets.QGroupBox(Support)
        self.groupBoxBestellungen.setGeometry(QtCore.QRect(0, 520, 361, 289))
        self.groupBoxBestellungen.setObjectName("groupBoxBestellungen")
        self.label_BestellungenDrodown = QtWidgets.QLabel(
            self.groupBoxBestellungen)
        self.label_BestellungenDrodown.setGeometry(
            QtCore.QRect(10, 23, 202, 16))
        self.label_BestellungenDrodown.setObjectName(
            "label_BestellungenDrodown")
        self.textfreieBeschreibungBestellungen = QtWidgets.QTextEdit(
            self.groupBoxBestellungen)
        self.textfreieBeschreibungBestellungen.setGeometry(
            QtCore.QRect(10, 87, 256, 192))
        self.textfreieBeschreibungBestellungen.setObjectName(
            "textfreieBeschreibungBestellungen")
        self.dropDownBestellungen = QtWidgets.QComboBox(
            self.groupBoxBestellungen)
        self.dropDownBestellungen.setGeometry(QtCore.QRect(10, 42, 251, 20))
        self.dropDownBestellungen.setObjectName("dropDownBestellungen")
        self.label_freieBeschreibungBestellungen = QtWidgets.QLabel(
            self.groupBoxBestellungen)
        self.label_freieBeschreibungBestellungen.setGeometry(
            QtCore.QRect(10, 68, 181, 16))
        self.label_freieBeschreibungBestellungen.setObjectName(
            "label_freieBeschreibungBestellungen")
        self.radioBBestellungen = QtWidgets.QRadioButton(
            self.groupBoxBestellungen)
        self.radioBBestellungen.setGeometry(QtCore.QRect(80, 0, 16, 16))
        self.radioBBestellungen.setText("")
        self.radioBBestellungen.setObjectName("radioBBestellungen")
        self.label_freieBeschreibungBestellungen_2 = QtWidgets.QLabel(
            self.groupBoxBestellungen)
        self.label_freieBeschreibungBestellungen_2.setGeometry(
            QtCore.QRect(270, 10, 84, 26))
        self.label_freieBeschreibungBestellungen_2.setAlignment(
            QtCore.Qt.AlignCenter)
        self.label_freieBeschreibungBestellungen_2.setObjectName(
            "label_freieBeschreibungBestellungen_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBoxBestellungen)
        self.spinBox.setGeometry(QtCore.QRect(290, 40, 39, 20))
        self.spinBox.setObjectName("spinBox")
        self.groupBox_4 = QtWidgets.QGroupBox(Support)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 331, 491))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioBProblemeFehler = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioBProblemeFehler.setGeometry(QtCore.QRect(90, 0, 82, 17))
        self.radioBProblemeFehler.setText("")
        self.radioBProblemeFehler.setObjectName("radioBProblemeFehler")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 278, 453))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioBAlgo = QtWidgets.QRadioButton(self.frame)
        self.radioBAlgo.setObjectName("radioBAlgo")
        self.verticalLayout_3.addWidget(self.radioBAlgo)
        self.radioBOAS = QtWidgets.QRadioButton(self.frame)
        self.radioBOAS.setObjectName("radioBOAS")
        self.verticalLayout_3.addWidget(self.radioBOAS)
        self.radioBwederOASnochAlgo = QtWidgets.QRadioButton(self.frame)
        self.radioBwederOASnochAlgo.setObjectName("radioBwederOASnochAlgo")
        self.verticalLayout_3.addWidget(self.radioBwederOASnochAlgo)
        self.verticalLayout_4.addWidget(self.frame)
        self.groupBoxProblemeMit = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxProblemeMit.setObjectName("groupBoxProblemeMit")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxProblemeMit)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dropDownProbleme = QtWidgets.QComboBox(self.groupBoxProblemeMit)
        self.dropDownProbleme.setObjectName("dropDownProbleme")
        self.verticalLayout_2.addWidget(self.dropDownProbleme)
        self.radioButtonEinloggenImSystem = QtWidgets.QRadioButton(
            self.groupBoxProblemeMit)
        self.radioButtonEinloggenImSystem.setObjectName(
            "radioButtonEinloggenImSystem")
        self.verticalLayout_2.addWidget(self.radioButtonEinloggenImSystem)
        self.radioButtonRegistrierenImSystem = QtWidgets.QRadioButton(
            self.groupBoxProblemeMit)
        self.radioButtonRegistrierenImSystem.setObjectName(
            "radioButtonRegistrierenImSystem")
        self.verticalLayout_2.addWidget(self.radioButtonRegistrierenImSystem)
        self.radioButtonMAanmelden = QtWidgets.QRadioButton(
            self.groupBoxProblemeMit)
        self.radioButtonMAanmelden.setObjectName("radioButtonMAanmelden")
        self.verticalLayout_2.addWidget(self.radioButtonMAanmelden)
        self.radioButtonFirmaErstellen = QtWidgets.QRadioButton(
            self.groupBoxProblemeMit)
        self.radioButtonFirmaErstellen.setObjectName(
            "radioButtonFirmaErstellen")
        self.verticalLayout_2.addWidget(self.radioButtonFirmaErstellen)
        self.label_6 = QtWidgets.QLabel(self.groupBoxProblemeMit)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.textfreieBeschreibungdesProblems = QtWidgets.QTextEdit(
            self.groupBoxProblemeMit)
        self.textfreieBeschreibungdesProblems.setObjectName(
            "textfreieBeschreibungdesProblems")
        self.verticalLayout_2.addWidget(self.textfreieBeschreibungdesProblems)
        self.verticalLayout_4.addWidget(self.groupBoxProblemeMit)
        self.frame_2 = QtWidgets.QFrame(Support)
        self.frame_2.setGeometry(QtCore.QRect(540, 670, 291, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dateTimeEditZeitpunkFehler = QtWidgets.QDateTimeEdit(self.frame_2)
        self.dateTimeEditZeitpunkFehler.setGeometry(
            QtCore.QRect(60, 40, 194, 22))
        self.dateTimeEditZeitpunkFehler.setObjectName(
            "dateTimeEditZeitpunkFehler")
        self.label_Datum_Zeit = QtWidgets.QLabel(self.frame_2)
        self.label_Datum_Zeit.setGeometry(QtCore.QRect(0, 0, 291, 31))
        self.label_Datum_Zeit.setAlignment(
            QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_Datum_Zeit.setObjectName("label_Datum_Zeit")

        self.retranslateUi(Support)
        QtCore.QMetaObject.connectSlotsByName(Support)

    def retranslateUi(self, Support):
        _translate = QtCore.QCoreApplication.translate
        Support.setWindowTitle(_translate("Support", "Dialog"))
        self.erstelleSupportticket.setText(
            _translate("Support", "Erstelle Supportticket"))
        self.groupBoxKontakt.setTitle(_translate(
            "Support", "Wie können wir den Supportanfragenden kontaktieren?"))
        self.label_Vorname.setText(_translate("Support", "Vorname"))
        self.label_Name.setText(_translate("Support", "Name"))
        self.label_Baustelle.setText(_translate("Support", "Baustelle"))
        self.label_Bauprojekt.setText(_translate("Support", "Bauprojekt"))
        self.label_Telefonnummer.setText(
            _translate("Support", "Telefonnummer"))
        self.radioButtonWachmann.setText(_translate("Support", "Wachmann"))
        self.radioButtonLogistiker.setText(_translate("Support", "Logistiker"))
        self.radioButton_Projektmanager.setText(
            _translate("Support", "Projektmanager"))
        self.groupBoxBestellungen.setTitle(
            _translate("Support", "Bestellungen"))
        self.label_BestellungenDrodown.setText(_translate(
            "Support", "Auf der Baustelle wird folgendes benötigt:"))
        self.label_freieBeschreibungBestellungen.setText(
            _translate("Support", "freie Beschreibung was wird benötigt:"))
        self.label_freieBeschreibungBestellungen_2.setText(_translate("Support", "Wieviel Stück \n"
                                                                      "werden benötigt?"))
        self.groupBox_4.setTitle(_translate("Support", "Probleme Fehler"))
        self.radioBAlgo.setText(_translate("Support", "Algo"))
        self.radioBOAS.setText(_translate("Support", "OAS"))
        self.radioBwederOASnochAlgo.setText(_translate(
            "Support", "betrifft weder OAS noch Algo"))
        self.groupBoxProblemeMit.setTitle(_translate(
            "Support", "Ich habe /  hatte ein Problem mit:"))
        self.radioButtonEinloggenImSystem.setText(
            _translate("Support", "Einloggen im System"))
        self.radioButtonRegistrierenImSystem.setText(
            _translate("Support", "Registrieren im System"))
        self.radioButtonMAanmelden.setText(
            _translate("Support", "Mitarbeiter anzumelden"))
        self.radioButtonFirmaErstellen.setText(
            _translate("Support", "eine Firma zu erstellen"))
        self.label_6.setText(_translate(
            "Support", "freie Beschreibung des Problems:"))
        self.label_Datum_Zeit.setText(_translate("Support", "Seit wann besteht der Fehler?\n"
                                                 "(Nur Zeit eintragen bei Systemfehlern, Fehlermeldungen)"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Support = QtWidgets.QDialog()
    ui = Ui_Support()
    ui.setupUi(Support)
    Support.show()
    sys.exit(app.exec_())