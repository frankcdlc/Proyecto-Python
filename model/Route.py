import random
from config import IGV

class Route(object):

    def __init__(self, code: str, name: str, base_price: float, economy_seat: float, premium_seat: float, min_sales_economics: int, max_sales_economics: int, min_sales_premium: int, max_sales_premium: int) -> None:
        self.code = code
        self.name = name
        self.base_price: float = base_price
        self.economy_seat: float = economy_seat
        self.premium_seat: float = premium_seat
        self.min_sales_economics = min_sales_economics
        self.max_sales_economics = max_sales_economics
        self.min_sales_premium = min_sales_premium
        self.max_sales_premium = max_sales_premium

        # Costo de pasaje económico + precio base
        self.price_economic: float = round(self.base_price + self.economy_seat, 2)
        # Costo de pasaje económico + precio base
        self.price_premium: float = round(self.base_price + self.premium_seat, 2)
        # Costo de IGV por pasaje economico
        self.price_economic_IGV = round(self.price_economic*IGV, 2)
        # Costo de IGV por pasaje premium
        self.price_premium_IGV = round(self.price_premium*IGV, 2)


    # Representación de objeto de la clase como string
    def __repr__(self) -> str:
        return self.name

    # Devuelve un número aleatorio de ventas de asientos economicos
    def get_rand_sales_economy(self) -> int:
        return random.randint(self.min_sales_economics, self.max_sales_economics)
    
    # Devuelve un número aleatorio de ventas de asientos premium
    def get_rand_sales_premium(self) -> int:
      return random.randint(self.min_sales_premium, self.max_sales_premium)