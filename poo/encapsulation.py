

class Pepe:
    __bank_account_number = "123456789"
    name = "pepe"


class Juan:
    bank_account_number = "123456789"
    name = "juan"


pepe = Pepe()
if hasattr(pepe, '__bank_account_number'):
    print(pepe.__bank_account_number, "but u shouldn't has this access!!")
else:
    print("u can't access this info")
print("")


juan = Juan()
if hasattr(juan, 'bank_account_number'):
    print(juan.bank_account_number, "but u shouldn't has this access!!")
else:
    print("u can't access this info")

