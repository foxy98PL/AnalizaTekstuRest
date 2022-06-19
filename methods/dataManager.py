import glob
import os
import openpyxl


def Files():
    os.chdir("resources")
    return [file for file in glob.glob("*.txt")]


def Data(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    result = []
    for i in range(2, sheet.max_row + 1):
        result += [sheet["B" + str(i)].value]
    return result


def DataTxt(file):
    with open(file, encoding="UTF-8") as f:
        temp = f.readlines()
    return temp
