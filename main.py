import pandas as pd
import matplotlib.pyplot as plt

df_can = pd.read_excel(
    "Canada.xlsx",
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print(df_can.head()) # Вивід перших 5 рядків
print(df_can.tail()) # Вивід останнійх 5 рядків
print(df_can.info()) # Вивід загальної інформації про data frame
print(df_can.columns) # Вивід назв стовпців
print(df_can.index) # Вивід інформації про ідексацію data frame
print(df_can.shape) # Вивід розміру data frame (рядки, стовпці)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True) #Видалення стовпців

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True) #зміна назв деяких стовпців

df_can['Total'] = df_can[[1980,       1981,       1982,
             1983,       1984,       1985,       1986,       1987,       1988,
             1989,       1990,       1991,       1992,       1993,       1994,
             1995,       1996,       1997,       1998,       1999,       2000,
             2001,       2002,       2003,       2004,       2005,       2006,
             2007,       2008,       2009,       2010,       2011,       2012]].sum(axis=1) # Додаваннянового стовпця для підсумку загальної кількість іммігрантів за країнами за весь період 1980-2013 років

print(df_can.isnull().sum()) # Підрахвання та вивід кількості NULL об'єктів

print(df_can.describe()) # Короткий опис кожного стовпця тип даних якого не string (основні статистичні метрики)

print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

df_can.set_index('Country', inplace=True) # Встановлення індексом Country

df_can.columns = list(map(str, df_can.columns)) # Перетворення назв стовпців у з int у string

years = list(map(str, range(1980, 2014))) # Створення змінної для доступу до стовпців

# Вивід графіку еміграції з України до Канади
Ukraine = df_can.loc['Ukraine', years]
print(Ukraine.head())

Ukraine.index = Ukraine.index.map(int)
Ukraine.plot(kind='line')

plt.title('Immigration from Ukraine')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

# plt.savefig('1.png')
plt.show()


# Вивід графіку еміграції з 5 країн з найбільшою кількістю емігрантів до Канади
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

df_top5 = df_can.head(5)

df_top5 = df_top5[years].transpose()

print(df_top5)

df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='line', figsize=(14, 8))

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
# plt.savefig('2.png')
plt.show()