# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool:
        ...


class EmailNotification(Notification):
    def send(self):
        print("Email: Sending.. - ",  self.message)
        return True


class SMSNotification(Notification):
    def send(self):
        print("SMS: Sending.. - ",  self.message)
        return True


def notify(notification:Notification):
    sendedNotification =  notification.send()    
    print("Notification was sended" if sendedNotification else "Not sended")

notify(EmailNotification("Success"))