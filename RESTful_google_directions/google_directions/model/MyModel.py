# -*- coding: utf-8 -*-

import requests
from xml.etree import ElementTree


class MyModel(object):
    """
    Eine Klasse, die das Model fuer die Anwendung darstellt. Sie kuemmert sich um die Abfrage der Daten.
    """
    def get_request(location, destination):
        """
        Diese Methode erzeugt einen HTTP-request und liefert das Ergebnis zurueck
        Wenn die Abfrage aus irgend einem Gruznd fehl schlaegt, liefert die Methode "False" zurueck

        :param location: Startort
        :param destination: Zielort
        :return: string / string-array["directions", "startpoint", "endpoint"]
        """
        url = "http://maps.googleapis.com/maps/api/directions/xml"
        params = {"origin": location,
                  "destination": destination,
                  "sensor": False,
                  "language": "de"}
        ret = ElementTree.fromstring(requests.get(url, params).text)
        if ret.find('status').text == 'OK':
            route = ret.find('route')
            output = ["", route.find('./leg/start_address').text, route.find('./leg/end_address').text]
            output[0] += "Die Gesamtdauer beträgt: <b>" + route.find("./leg/duration/text")\
                .text + " </b>; Die Gesamtentfernung beträgt: <b>" + route.find("./leg/distance/text").text + "</b><p><p>"
            for i in route.iter('step'):
                output[0] += i.find("./html_instructions").text + \
                             "; Entfernung: " + i.find("./distance/text").text + \
                             "; Dauer: " + i.find("./duration/text").text + "<p>"
            return output
        else:
            return "False"
