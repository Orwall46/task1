"""
Нашел красивый метод .gt() на просторах stackoverflow...
"""

import pandas as pd


data_base = {
    'customer_id': [1, 2, 1, 1, 2, 1, 1, 2, 1],
    'product_id': [999, 998, 997, 996, 995, 994, 993, 992, 991],
    'timestamp': [
        '2022.11.17 03:00:00', '2022.11.17 03:00:00', '2022.11.17 03:01:00',
        '2022.11.17 03:06:00', '2022.11.17 03:03:05', '2022.11.17 03:07:00',
        '2022.11.17 03:11:00', '2022.11.17 03:04:00', '2022.11.17 03:22:00'
    ]
}

df = pd.DataFrame(data_base)

# Переводим в формат datetime, чтобы могли дальше использовать метод diff
# df['timestamp'] =  pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')

### Оборачиваем в groupby потому что мы хотим видеть по конкретному пользователю,
## применяем метод transform, которая принимает неименованную функцию,
# которая возвращает уникальный int id
# df['session0'] = df.groupby('customer_id')['timestamp'].transform(
#                     lambda x: x.diff().gt('3Min').cumsum()
#                     )

# Таже самая логика, только реализована без помощи transfrom. Делали две группировки,
## при помощи cumsum() + 1 - возвращает int id, которая начинается с 1.
# df['session'] = df.assign(session=(df.groupby('customer_id')['timestamp'].diff() > '00:03:00')
#                     .astype(int)).groupby('customer_id')['session'].cumsum() + 1


def add_sessions(data: pd.DataFrame) -> pd.DataFrame:
    '''Получаем DataFrame, проверяем и добавляем новую колонку'''
    if not isinstance(data, pd.DataFrame):
        return print('data will be pandas DataFrame')
    if len(data.axes[1]) != 3:
        return print('data will have 3 columns')

    data['timestamp'] =  pd.to_datetime(data['timestamp'], format='%Y-%m-%d %H:%M:%S')

    data['session'] = data.groupby('customer_id')['timestamp'].transform(
                    lambda x: x.diff().gt('3Min').cumsum()
                    )
    return data


add_sessions(df)
