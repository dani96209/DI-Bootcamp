# Exercise 2
import openpyxl

# Open the workbook and select the first sheet
wb = openpyxl.load_workbook('C:\\Users\\daniel\\Downloads\\Plants.xlsx')
ws = wb['Sheet1']

# Start from cell A2
cell = ws['A2']

# Loop through the rows until a blank cell is encountered
while cell.value is not None:
    # Check if the plant is not in stock (Column H, which is 7 columns to the right of column A)
    stock_status = cell.offset(row=0, column=7).value
    if stock_status == "No":
        print(cell.value)
    
    # Move to the next row
    cell = cell.offset(row=1, column=0)
