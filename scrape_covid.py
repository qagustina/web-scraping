import pandas as pd
from pandas.io.html import read_html


def get_url():
    return 'https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2020_en_Argentina'
    

def extract_pandas_table():
    pd.set_option('display.max_columns',None, 'display.max_rows', None, 'display.max_colwidth', 10, 'display.width', None)
    table = read_html(get_url(), index_col=0, attrs={"class":"wikitable"})
    print(table[0])
    return table[0]


def write_csv(table):
    table.to_csv('casos_covid.csv')

    
def main():
    table = extract_pandas_table()
    write_csv(table)


if __name__ == '__main__': 
    main()