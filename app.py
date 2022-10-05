from typing import List, Dict
from model.Route import Route


def create_list_routes() -> List[Route]:
    # Creará una lista de objetos de rutas
    data_routes: List[Dict[str, str]] = [
        {
            "code": "LIM-AYA",
            "name": "LIMA-AYACUCHO",
            "base_price": 55.19,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 120,
            "max_sales_economics": 130,
            "min_sales_premium": 10,
            "max_sales_premium": 20
        },
        {
            "code": "LIM-CUS",
            "name": "LIMA-CUSCO",
            "base_price": 136.51,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 130,
            "max_sales_economics": 144,
            "min_sales_premium": 15,
            "max_sales_premium": 24
        },
        {
            "code": "LIM-ARE",
            "name": "LIMA-AREQUIPA",
            "base_price": 90.59,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 115,
            "max_sales_economics": 138,
            "min_sales_premium": 16,
            "max_sales_premium": 22
        },
        {
            "code": "LIM-TAR",
            "name": "LIMA-TARAPOTO",
            "base_price": 79.89,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 100,
            "max_sales_economics": 120,
            "min_sales_premium": 12,
            "max_sales_premium": 18
        },
        {
            "code": "AYA-LIMA",
            "name": "AYACUCHO-LIMA",
            "base_price": 40.42,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 100,
            "max_sales_economics": 115,
            "min_sales_premium": 10,
            "max_sales_premium": 15
        },
        {
            "code": "CUS-LIM",
            "name": "CUSCO-LIMA",
            "base_price": 124.32,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 105,
            "max_sales_economics": 120,
            "min_sales_premium": 14,
            "max_sales_premium": 20
        },
        {
            "code": "ARE-LIM",
            "name": "AREQUIPA-LIMA",
            "base_price": 86.59,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 100,
            "max_sales_economics": 110,
            "min_sales_premium": 13,
            "max_sales_premium": 18
        },
        {
            "code": "TAR-LIMA",
            "name": "TARAPOTO-LIMA",
            "base_price": 68.42,
            "economy_seat": 8.00,
            "premium_seat": 16.00,
            "min_sales_economics": 90,
            "max_sales_economics": 105,
            "min_sales_premium": 10,
            "max_sales_premium": 20
        }
    ]

    routes: List[Route] = []

    # Iteramos sobre la lista de rutas
    for key, route in enumerate(data_routes):
        # Creamos objeto de rutas
        obj_route = Route(str(route['code']), str(route['name']), float(route['base_price']), float(
            route['economy_seat']), float(route['premium_seat']), int(route['min_sales_economics']), int(route['max_sales_economics']), int(route['min_sales_premium']), int(route['max_sales_premium']))
        routes.append(obj_route)

    return routes

def create_sales_and_incomes_tickets(route: Route):
  # Número de asientos económicos vendidos
  sales_economics = route.get_rand_sales_economy()
  # Número de asientos premium vendidos  
  sales_premium = route.get_rand_sales_premium()
  # Número de total de asientos vendidos
  sales = sales_economics + sales_premium
  # Ingreso por venta de pasajes económicos por vuelo
  income_economics_sales: float = round(sales_economics * route.price_economic, 2)
  # ingreso por venta de pasajes premium por vuelo
  income_premium_sales: float = round(sales_premium * route.price_premium, 2)
  # Ingreso total por vuelo
  income_total = round(income_economics_sales + income_premium_sales, 2)
  IGV_total = round(route.price_economic_IGV * sales_economics + route.price_premium_IGV * sales_premium, 2)


 # Diccionario de tickets vendidos
  sales_and_incomes = {
    "sales_economics": sales_economics,
    "sales_premium": sales_premium,
    "sales_total": sales,
    "income_economics_sales": income_economics_sales,
    "income_premium_sales": income_premium_sales,
    "income_total": income_total,
    "IGV_total": IGV_total
  }
  
  return sales_and_incomes

def main():
    # Función principal del modulo
    total_sales_tickets = 0
    total_income_sales_economics: float = 0
    total_income_sales_premium: float = 0
    IGV_total: float = 0
    route_with_seats_sales: List = []
    seats_by_routes: List = []
    first_three_incomes: List = []

    routes: List[Route] = create_list_routes()
    for k, route in enumerate(routes):
        sales_tickets: List = create_sales_and_incomes_tickets(route)
        # Número de tickets vendidos por vuelo
        sales_tickets_by_route = sales_tickets["sales_total"]
        # Número total de tickets vendidos en todos los vuelos
        total_sales_tickets += sales_tickets["sales_total"]
        # Ingresos totales por venta de asientos económicos
        total_income_sales_economics += float(round(sales_tickets["income_economics_sales"],2))
        # Ingresos totales por venta de asientos premium
        total_income_sales_premium += sales_tickets["income_premium_sales"]
        # Ingresos totales por vuelo
        total_income = total_income_sales_economics +  total_income_sales_premium
        # Costo del IGV total
        IGV_total += sales_tickets["IGV_total"]
        # Precio promedio de los asientos económicos en todos los vuelos
        avg_economic_price:float = round((total_income_sales_economics / sales_tickets["sales_economics"]) / len(routes),2)  
        # Precio promedio de los asientos premium en todos los vuelos
        avg_premium_price: float = round((total_income_sales_premium / sales_tickets["sales_premium"]) / len(routes), 2)

        # Lista de objetos de asientos e ingresos
        seats_by_routes.append({
            "route": route,
            "total_sales_tickets": sales_tickets_by_route,
            "total_income": total_income
        })

        max_sales_tickets: Dict[str, Route] = max(seats_by_routes, key=lambda x: x["total_sales_tickets"])

        min_sales_tickets: Dict[str, Route] = min(seats_by_routes, key=lambda x: x["total_sales_tickets"])

        # Tres primeros vuelos con mayores ingresos
        sorted_income_sales: Dict[str, Route] = sorted(seats_by_routes, key=lambda x: x['total_income'], reverse=True)



    print('-'*20)
    # ¿Cuál es el total de pasajes vendidos entre todos los vuelos?
    print('Total de pasajes vendidos entre todos los vuelos: ', total_sales_tickets)
    # ¿Cuál es el total de ingresos por la venta de pasajes económicos?
    print('Total de ingresos por venta de pasajes económicos: ', total_income_sales_economics)
    # ¿Cuál es el total de ingresos por la venta de pasajes premium?
    print('Total de ingresos por venta de pasajes premium: ', total_income_sales_premium)
    # ¿Cuál es el importe total de IGV cobrado?
    print('El costo total de IGV cobrado: ', IGV_total)
    # ¿Cuál es el valor promedio de un pasaje económico?
    print('Valor promedio de pasaje economico: ', avg_economic_price)
    # ¿Cuál es el valor promedio de un pasaje premium?
    print("Valor promedio de pasaje premium: ", avg_premium_price)
    # ¿Cuál fue el vuelo con la mayor cantidad de pasajeros?
    print("Vuelo con mayor cantidad de pasasjeros:", route_with_seats_sales[-1])
    # ¿Cuál fue el vuelo con la menor cantidad de pasajeros?
    print("Vuelo con menor cantidad de pasajeros", route_with_seats_sales[0])
    # ¿Cuáles son los tres primeros vuelos que obtuvieron los mayores ingresos por la venta de asientos?
    
    # ¿Cuál fue el avión que transportó la mayor cantidad de pasajeros?
        


if __name__ == "__main__":
    main()
