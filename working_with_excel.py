import xlsxwriter as x

wb = x.Workbook("excel_sheet.xlsx")
ws = wb.add_worksheet()

ws.write("A1", "Block 1")
ws.write("B1", "Block 2")
ws.write(2,2,"yo nu text")
ws.write(1,0, "1,0")
ws.write(3,10, "3,10")

wb.close()

print("Code ran successfully")