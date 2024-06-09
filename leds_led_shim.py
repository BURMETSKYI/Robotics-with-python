import ledshim

class Leds:
    @property
    def count(self):
        return ledshim.width