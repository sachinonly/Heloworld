import openpyxl
import xlrd
wb = openpyxl.load_workbook('Sample.xlsx')
type(wb)
sheet = wb.get_sheet_by_name('Sheet1')
tuple(sheet['A1':'C3'])
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        if cellObj.value == 'Mango':
            print('Matches ')
            print(cellObj.coordinate, cellObj.value)
        else:
            print('No Match')
            print(cellObj.coordinate, cellObj.value)
 
            
             