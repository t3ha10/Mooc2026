# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents
         
    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"
    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents
    def __ne__(self, another):
        return self._euros != another._euros or self._cents != another._cents
    def __lt__(self, another):
        return self._euros < another._euros or self._euros == another._euros and self._cents < another._cents
    def __gt__(self, another):
        return self._euros > another._euros or self._euros == another._euros and self._cents > another._cents

    def __add__(self, another):
        cent = self._cents + another._cents
        if cent >= 100:
            cent -= 100
            euro =  self._euros + 1 + another._euros
        else:
            euro = self._euros + another._euros
        return Money(euro, cent)

    def __sub__(self, another):
        if self._euros < another._euros or self._euros == another._euros and self._cents < another._cents:
            raise ValueError(f"a negative result is not allowed")
        if self._cents < another._cents:
            cent = self._cents + 100 - another._cents
            euro = self._euros - another._euros - 1
        else:
            euro = self._euros - another._euros
            cent = self._cents - another._cents
        return Money(euro, cent)

if __name__ == "__main__":
    e1 = Money(1, 0)
    e2 = Money(1, 0)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)


    print(e1)
    e1.euros = 1000
    print(e1)