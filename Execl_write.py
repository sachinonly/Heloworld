#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xlwt
import xlsxwriter
workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("Sheet_Excel_Write")


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)


worksheet.write('A1', 'Hello2222')
worksheet.insert_image('B5', 'IMG_2868.jpg')
