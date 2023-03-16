class Saving:
    pass

class Checking:
    pass

class Bankacc(Saving, Checking):
    pass

class Bond:
    pass

class Stock:
    pass

class Security(Stock, Bond):
    pass

class Real:
    pass

class Ins(Bankacc, Real):
    pass

class Asset(Bankacc, Security, Real):
    pass

class Interest(Bankacc, Security):
    pass