from datetime import date, time
from decimal import Decimal


def dataParser(line):
    data = {
        "type": line[0],
        "date": date(int(line[1:5]), int(line[5:7]), int(line[7:9])),
        "value": Decimal(f"{int(line[9:19]) / 100.00}"),
        "cpf": line[19:30],
        "card": line[30:42],
        "hour": time(int(line[42:44]), int(line[44:46]), int(line[46:48])),
        "shop_owner": line[48:62].strip(),
        "shop_name": line[62:81].strip(),
    }

    return data
