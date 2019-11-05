import pandas as pd

df = pd.read_csv('convertcsv.csv')

wien = df[df['plz_name'] == "Wien"]
#print(wien.info())
print(wien[['plz', 'price_per_m2']])

#print(df[wien])

# 19.Bezirk filtern
bezirk19 = df['plz'] == 1190
print("19 Bezirk %s" % df[bezirk19])
