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
chart2 = PieChart()
data = Reference(ws, min_col=15, min_row=8, max_col=16, max_row=8)
labels = Reference(ws, min_col=15, min_row=7, max_col=16, max_row=7)
chart2.add_data(data, from_rows=True)
chart2.set_categories(labels)
chart2.title = '% Counterfeit Crimes'
chart2.height, chart2.width = 4.75, 6.75
ws.add_chart(chart2, 'O14')

wb.save('lines.xlsx')
