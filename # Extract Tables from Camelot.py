# Extract Tables from Camelot
# pip install camelot-py
import camelot
table = camelot.read_pdf('test.pdf', pages='1-2')
# get total number of tables
print("Total tables: ", table.n) # 2
# print table by num
print(table[0].df)
print(table[1].df)
# Export Table to CSV
table[0].to_csv('table1.csv')
table[1].to_csv('table2.csv')
# Export Table to Excel
table[0].to_excel('table1.xlsx')
# Export Table to HTML
table[0].to_html('table1.html')
# Extract and Export Table At Once
table.export('tables.csv', f='csv', compress=True)
# Parse Table Report
table[0].parse(['Date', 'Description', 'Amount'])