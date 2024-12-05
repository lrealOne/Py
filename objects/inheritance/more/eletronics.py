from log import LogFileMixin, LogPrintMixin
class Eletronic:
    def __init__(self, name):
        self._name = name
        self._on = False
    
    def turnOn(self):
        if not self._on:
            self._on = True

    def turnOff(self):
        if self._on:
            self._on = False

class Smartphone(Eletronic, LogFileMixin):
    def turnOn(self):
        super().turnOn()
    
        if self._on:
            message = f"{self._name} está ligado."
            self.log_success(message)

    def turnOff(self):
        super().turnOff()

        if not self._on:
            message = f"{self._name} está desligado."
            self.log_error(message)