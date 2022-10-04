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
