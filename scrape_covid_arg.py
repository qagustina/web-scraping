import pandas as pd
from pandas.io.html import read_html


def get_url():
    return 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases_in_2020'


table = read_html(get_url(), index_col=0, attrs={"class": "wikitable"}, flavor='html5lib')
pd.set_option('display.max_columns', None, 'display.max_rows', None, 'display.max_colwidth', 15,
                  'display.width', None)
table_clean = table[0].iloc[:-4, :] 
table_clean = table_clean.drop_duplicates()\
              .replace(r'—', 0, regex=True)\
              .replace(r'N/A', 0, regex=True)


def extract_cases_table(table_clean):
    cases_table = table_clean.replace({"\[[0-9a-z]*\]": ""}, regex=True)\
                  .replace({"\((\d+)\)": ""}, regex=True)
    return cases_table


def extract_deaths_table(table_clean):
    deaths_table = table_clean.replace({"^(\d*)": ""}, regex=True)\
                  .replace(r'^\s*$', 0, regex=True)\
                  .replace({"\[[0-9a-z]*\]": ""}, regex=True)
    return deaths_table


def main():
    cases_table = extract_cases_table(table_clean)
    deaths_table = extract_deaths_table(table_clean)
    #print(cases_table)
    #print(deaths_table)

    
if __name__ == '__main__':
     main()
