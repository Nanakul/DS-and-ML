from openpyxl import load_workbook
from openpyxl.chart import BarChart, PieChart, Series, Reference

wb = load_workbook('crime_report.xlsx')
ws = wb.active

# Initialize Bar chart
chart = BarChart()

# Reference A8 to M13
data = Reference(ws, min_col=1, min_row=8, max_row=13, max_col=13)

# Add data to the chart and add chart to cell B14
chart.add_data(data, titles_from_data=True)
ws.add_chart(chart, 'B14')
wb.save('lines.xlsx')
