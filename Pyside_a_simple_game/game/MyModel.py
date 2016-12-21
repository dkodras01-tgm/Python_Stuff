class MyModel(object):
    """
    Eine Klasse, die das Model fuer das Spiel darstellt. Sie enthaelt alle wichtigen Spieldaten.
    """
    def __init__(self):
        """
        Diese Methode setzt alle Defaultwerte fuer die Spielestatistik
        """
        self.groesse = 15
        self.offen = 15
        self.korrekt = 0
        self.inkorrekt = 0
        self.gesamt = 0
        self.spiele = 0

    def neuesSpiel(self):
        """
        Diese Methode setzt alle Werte, wenn weitere Spielrunden gespielt werden
        """
        self.offen = self.groesse
        self.korrekt = 0
        self.inkorrekt = 0
        self.gesamt = 0
        self.spiele += 1

    def richtig(self):
        """
        Diese Methode setzt alle Werte, wenn ein korrekter Button gedrueckt wurde
        """
        self.offen -= 1
        self.korrekt += 1
        self.gesamt += 1

    def falsch(self):
        """
        Diese Methode setzt alle Werte, wenn ein invalider Button gedrueckt wurde
        """
        self.inkorrekt += 1
        self.gesamt += 1

    def offenstring(self):
        """
        Diese Methode gibt den Wert der offenen Buttons zurueck
        :return String: offen
        """
        return str(self.offen)

    def korrektstring(self):
        """
        Diese Methode gibt die Anzahl der korrekt gedrueckten Buttons zurueck
        :return String: korrekt
        """
        return str(self.korrekt)

    def inkorrektstring(self):
        """
        Diese Methode gibt die Anzahl der inkorrekt gedrueckten Buttons zurueck
        :return String: inkorrekt
        """
        return str(self.inkorrekt)

    def gesamtstring(self):
        """
        Diese Methode gibt die Anzahl der gesamt gedrueckten Buttons zurueck
        :return String: gesamt
        """
        return str(self.gesamt)

    def spielestring(self):
        """
        Diese Methode gibt die Anzahl der gespielten Spiele zurueck
        :return String: spiele
        """
        return str(self.spiele)
