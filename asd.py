import pandas as pd
from io import StringIO

df = pd.DataFrame(index=list(range(1,3)))

print(df)

asd = df.to_csv()
#asd = df.to_string()

print(asd)

print(type(asd))


df = pd.read_csv(StringIO(asd), sep='\s+')

print(df)