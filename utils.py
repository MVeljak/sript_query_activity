
import re

from constant import FILE_NAME


def createParentUUID(ACTIVITY_UUID_PARENT):
    return ACTIVITY_UUID_PARENT if ACTIVITY_UUID_PARENT == 'null' else "'{}'".format(ACTIVITY_UUID_PARENT)


def getAziendaSanitaria(ambulatoi):
    return "'{}'".format(ambulatoi.split("-")[0].strip())


def createValueJava(value):
    return value if value == 'null' else 'UUID.fromString("{}")'.format(value)


def pritInFile(insertQuery):
    with open(FILE_NAME, "a") as file:
        file.write(insertQuery + "\n")


def set_value(value):
    if not value:
        return 'null'
    if str(value).isnumeric():
        return f"{value}"
    if value in ['true', 'false']:
        return f"{value}"
    return f"'{value}'"
