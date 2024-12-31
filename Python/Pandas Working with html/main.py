import pandas as pd

html = pd.read_html('https://en.wikipedia.org/wiki/Mobile_country_code')

print(html)
print(type(html)) # <class 'list'>

print(html[1]) 

html=pd.read_html("https://en.wikipedia.org/wiki/Economy_of_the_United_States",match="Government debt")

print(html[0])

html=pd.read_html("https://en.wikipedia.org/wiki/Minnesota",match="Average daily maximum and minimum temperatures for selected cities in Minnesota")

print(html[0])
print(type(html[0])) # <class 'pandas.core.frame.DataFrame'>

html[0].to_html('demo.html')

