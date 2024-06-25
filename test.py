import pandas as pd

df_houses = pd.read_excel('data/Рабочая_таблица_Данные_о_ЖК_Владивостока_v4_1_с_новым_атрибутом 09042024.xlsx')
df_houses = df_houses.T

start_col_index = df_houses.columns.get_loc('Общая сумма полученных денег с проданных квартир, руб')
end_col_index = df_houses.columns.get_loc('Количество проданных нежилых помещений')

df_houses = df_houses.drop(df_houses.columns[start_col_index:end_col_index + 1], axis=1)
