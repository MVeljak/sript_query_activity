import random
import uuid
from constant import FILE_NAME
from datetime import datetime, timedelta


def getDate(gap=0, datonly=False):
    now = datetime.now()
    if gap == 0:
        return now.date() if datonly else now
    elif gap > 0:
        result = now + timedelta(hours=gap)
        return result.date() if datonly else result
    else:
        result = now - timedelta(hours=gap)
        return result.date() if datonly else result


def getUUID():
    return uuid.uuid4()


def randomChoice(lista):
    return random.choice(lista)


def get_azienda_sanitaria(ambulatorio):
    return "{}".format(ambulatorio.split("-")[0].strip())


def createValueJava(value):
    return value if value == 'null' else 'UUID.fromString("{}")'.format(value)


def pritInFile(insertQuery):
    with open(FILE_NAME, "a") as file:
        file.write(insertQuery + "\n")


def set_value(value):
    # value = str(value)
    if not value:
        return 'null'
    if str(value).isnumeric():
        return f"{value}"
    if value in ['true', 'false']:
        return f"{value}"
    return f"'{value}'"
