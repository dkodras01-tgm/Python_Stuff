from PySide.QtCore import *
from PySide.QtGui import *
import MyView
import MyModel
import sys
from random import *

class MyController(QDialog):

    """
    MVC pattern: Erzeugt einen Controller - MVC Pattern.
    """
    def __init__(self, parent=None):
        """
        Diese Methode erzeugt mit Hilfe des MVC Patterns einen neuen Controller mit einem MyViev und einem MyModel Objekt

        :param parent:
        """
        super(MyController, self).__init__(parent)
        self.myGame = MyView.Ui_MyGame()
        self.myGame.setupUi(self)
        self.buttons = [self.myGame.pushButton,
                        self.myGame.pushButton_2,
                        self.myGame.pushButton_3,
                        self.myGame.pushButton_4,
                        self.myGame.pushButton_5,
                        self.myGame.pushButton_6,
                        self.myGame.pushButton_7,
                        self.myGame.pushButton_8,
                        self.myGame.pushButton_9,
                        self.myGame.pushButton_10,
                        self.myGame.pushButton_11,
                        self.myGame.pushButton_12,
                        self.myGame.pushButton_13,
                        self.myGame.pushButton_14,
                        self.myGame.pushButton_15]
        self.aktuelleNummer = 0
        self.myModel = MyModel.MyModel()
        # connect the buttons with the clicked signal
        self.connectButtons()
        # start a new game
        self.start()

    def connectButtons(self):
        """
        Diese Methode verbindet die Buttons mit ihren "Listenern"
        Fuer den Neu Button wird die start Methode aufgerufen
        """
        for bPuffer in self.buttons:
            bPuffer.clicked.connect(self.buttonClicked)
        self.myGame.pushButton_neu.clicked.connect(self.start)

    def buttonClicked(self):
        """
        Diese Methode prueft, ob der Button Wert valide ist und auch den korrekten Wert hat.

        :raise TypeError: falscher Wert
        """
        button = self.sender()
        if isinstance(button, QPushButton):
            value = int(button.text())
        else:
            raise TypeError("Falscher Wert: " + type(button))
        if self.aktuelleNummer == int(value):
            button.setEnabled(False)
            self.myModel.richtig()
            self.aktuelleNummer += 1
        else:
            self.myModel.falsch()
        self.updateWerte()

    def start(self):
        """
        Die Methode erzeugt das neue Spiel, mischt die Buttons und weist ihnen dann jeweils ganzzahlige Werte zu.
        Danach werden die Werte fuer das neue Spiel gesetzt und alle Buttons wieder anklickbar gemacht.
        """
        self.myModel.neuesSpiel()
        shuffle(self.buttons)
        i = 0
        for bPuffer in self.buttons:
            bPuffer.setText(str(i))
            i += 1
        self.aktuelleNummer = 0
        self.updateWerte()
        #alle Buttons wieder klickbar
        for bPuffer in self.buttons:
            bPuffer.setEnabled(True)

    def updateWerte(self):
        """
        Eine Methode, die die Werte fuer die Zaehler aktualisiert

        Achtung self.myGame._____ nicht zu verwechseln, mit den Attributen des Models!!!
        -> self.myGame.falsch.setText(self.myModel.inkorrektstring())
        """
        self.myGame.offen.setText(self.myModel.offenstring())
        self.myGame.korrekt.setText(self.myModel.korrektstring())
        self.myGame.falsch.setText(self.myModel.inkorrektstring())
        self.myGame.gesamt.setText(self.myModel.gesamtstring())
        self.myGame.spiele.setText(self.myModel.spielestring())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
