import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')




data = pd.read_csv('/home/poldi/Matplotlib/MuenchenWetter.csv', sep=';')

temp = data['TMK']
years = [1956,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988.1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]


plt.plot(years,temp,
         label='Tempature in Munich',linestyle='--',
         color='red')

plt.title('Tempature in Munich 1954-2020')

plt.legend()

plt.xlabel('Year')
plt.ylabel('Tempature')

plt.tight_layout()

plt.show()