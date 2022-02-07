from openpyxl import load_workbook
from openpyxl.chart import BarChart, PieChart, Series, Reference

wb = load_workbook('crime_report.xlsx')
ws = wb.active

# Initialize Bar chart
chart = BarChart()

# Reference A8 to M13
data = Reference(ws, min_col=1, min_row=10, max_row=13, max_col=13)
labels = Reference(ws, min_col=2, min_row=8, max_col=13, max_row=8)

# Add data to the chart and add chart to cell B14
chart.add_data(data, from_rows=True, titles_from_data=True)
chart.set_categories(labels)
chart.title = 'Counterfeit Crimes by District'
chart.height, chart.width = 4.75, 20.3
ws.add_chart(chart, 'B14')

# Add Pie chart from O14 to Q22

wb.save('lines.xlsx')
