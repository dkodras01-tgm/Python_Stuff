import sys
import datetime
import math
import pygame


class MyClock:
    """
    Eine Klasse, die eine Uhr darstellt.
    """

    def __init__(self):
        """
        Setzt alle Attribute fuer das Fenster und die Uhr
        """
        self.analog = False  # True  - Ticken, False - Gleiten
        self.ad = True  # True - analog Uhr, False - digital Uhr
        self.windowMargin = 30
        self.windowWidth = 600
        self.windowHeight = 600
        self.windowCenter = 600/2, 600/2
        self.clockMarginWidth = 20
        self.secondColor = (255, 0, 0)
        self.minuteColor = (100, 200, 0)
        self.hourColor = (100, 200, 0)
        self.clockMarginColor = (130, 130, 0)
        self.clockBackgroundColor = (20, 40, 30)
        self.backgroundColor = (255, 255, 255)
        self.ticksColor = (255, 255, 0)
        self.radius = self.windowWidth / 2.0 - self.windowMargin
        self.hourCursorLength = self.radius - 140
        self.minuteCursorLength = self.radius - 40
        self.secondCursorLength = self.radius - 10
        self.quatorTicks = self.radius * 0.75
        self.fiveMinuteTicks = self.quatorTicks * 1.2
        self.oneMinuteTicks = self.secondCursorLength
        self.virtualSpeed = 1
        self.useVirtualTimer = True

        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Analog Clock")

        # Endlosschleife, damit die Uhr endlos laeuft, bis sie beendet wird
        while True:
            self.handleEvents()
            self.screen.fill(self.backgroundColor)
            self.drawBackground()
            self.drawCurrentTime()
            self.drawForeground()
            pygame.display.flip()
            pygame.time.delay(10)  # Updateintervall der Uhr (besonders sichtbar, bei analog kontinurierlich

    def handleEvents(self):
        """
        Kuemmert sich um die gedrueckten Keys
        A - Analog Uhr
        D - Digital Uhr
        P - Sekundenzeiger ticken/kontinuierlich

        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                print("A")
                self.ad = True
                pygame.init()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                print("D")
                self.ad = False
                pygame.init()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                if self.analog:
                    self.analog = False
                else:
                    self.analog = True
                pygame.init()

    def drawBackground(self):
        """
        Zeichnet das Ziffernblatt der Uhr

        :return:
        """
        self.screen.fill(self.backgroundColor)
        pygame.draw.ellipse(self.screen, self.clockMarginColor, (self.windowMargin, self.windowMargin,
                                                                 self.windowWidth-2*self.windowMargin,
                                                                 self.windowWidth-2*self.windowMargin))
        pygame.draw.ellipse(self.screen, self.clockBackgroundColor, (self.windowMargin+self.clockMarginWidth/2,
                                                                     self.windowMargin+self.clockMarginWidth/2,
                                                                     self.windowWidth-(self.windowMargin+self.clockMarginWidth/2)*2,
                                                                     self.windowWidth-(self.windowMargin+self.clockMarginWidth/2)*2))

        for i in range(0, 60, 1):
            start = self.getCirclePoint(i, 60, self.radius)
            length = self.oneMinuteTicks
            if i % 15 == 0:
                length = self.fiveMinuteTicks

            self.drawCursor(self.ticksColor, 5, length, i, 60, start)

    def getCirclePoint(self, position, scale, cursorLength):
        """
        Errechnet den Rotationspunkt (Mittelpunkt der Uhr)

        :param position:
        :param scale:
        :param cursorLength:
        :return: x und y Koordinaten
        """
        degrees = 360 / scale * position - 90
        bogenmass = math.radians(degrees)
        xPos = round(math.cos(bogenmass) * cursorLength + self.windowCenter[0])
        yPos = round(math.cos(bogenmass) * cursorLength + self.windowCenter[1])
        return (xPos, yPos)

    def drawCursor(self, color, width, length, position, scale, start=0):
        """
        Zeichnet einen Zeiger mit den angegebenen Parametern

        :param color:
        :param width:
        :param length:
        :param position:
        :param scale:
        :param start:
        :return:
        """
        start = (start if start != 0 else self.windowCenter)
        end = self.getCirclePoint(position, scale, length)
        pygame.draw.line(self.screen, color, start, end, width)

    def drawCurrentTime(self):
        """
        Zeichnet die Zeiger der Uhr (gemaess der aktuellen Zeit)

        :return:
        """
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        micro = now.microsecond

        self.drawCursor(self.hourColor, 15, self.hourCursorLength, hour + minute / 60.0, 12)
        self.drawCursor(self.minuteColor, 8, self.minuteCursorLength, minute + second / 60.0, 60)
        showSecond = (second + micro / 1000000.0 if self.analog else second)
        self.drawCursor(self.secondColor, 3, self.secondCursorLength, showSecond, 60)

    def drawForeground(self):
        """
        Zeichnet den Rotationspunkt

        :return:
        """
        pygame.draw.ellipse(self.screen, self.clockMarginColor, (self.windowWidth/2.0-9, self.windowHeight/2.0-9, 18, 18))

# Main Funktion
if __name__ == '__main__':
    MyClock()
