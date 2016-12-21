# -*- coding: utf-8 -*-

from PySide.QtGui import *
import sys

import google_directions.model.MyModel
import google_directions.view.MyView


class MyController(QMainWindow):
    """
    Diese Klasse kuemmert sich um die Verarbeitung der Events (Button geklickt,..)
    """
    def __init__(self, parent=None):
        """
        Diese Methode erzeugt mit Hilfe des MVC Patterns einen neuen Controller mit einem MyViev und einem MyModel Objekt

        :param parent:
        """
        super().__init__(parent)
        self.form = google_directions.view.MyView.Ui_MainWindow()
        self.form.setupUi(self)
        self.model = google_directions.model.MyModel.MyModel
        self.form.pushButton_submit.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """
        Diese Methode ueberprueft, ob Adressen eingegeben wurden und ob diese gueltig sind und
        gibt dann eine entsprechende Rueckmeldung in der Statusbar zurueck

        :return:
        """
        if self.form.lineEdit_start.text() == "" or self.form.lineEdit_ziel.text() == "":
            self.form.statusbar.showMessage("Es muessen zuerst zwei Orte angegeben werden, bevor eine Route berechnet werden kann!")
        else:
            buffer = self.model.get_request(self.form.lineEdit_start.text(), self.form.lineEdit_ziel.text())
            if buffer == "False":
                self.form.statusbar.showMessage("Die angegebene Adresse konnte nicht gefunden werden :(")
                self.form.textEdit_output.setText("Adresse nicht gefunden! Bitte geben Sie eine gueltige Adresse ein!")
            else:
                self.form.statusbar.showMessage("Ihre Route wird berechet.")
                self.form.textEdit_output.setText(buffer[0])
                self.form.lineEdit_start.setText(buffer[1])
                self.form.lineEdit_ziel.setText(buffer[2])
                self.form.statusbar.showMessage("Die Route wurde erfolgreich berechnet :)")

# Main-Funktion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
