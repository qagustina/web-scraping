import pandas as pd
from pandas.io.html import read_html
import re


def get_url():
    return 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases'


def extract_cases_table():
    pd.set_option('display.max_columns', None, 'display.max_rows', None, 'display.max_colwidth', 15,
                  'display.width', None)
    cases_table = read_html(get_url(), index_col=0, attrs={"class": "wikitable"})
    cases_table[0] = cases_table[0].iloc[:-4, :]
    cases_table[0] = cases_table[0].drop_duplicates()
    cases_table[0] = cases_table[0].replace(r'—', 0, regex=True)
    cases_table[0] = cases_table[0].replace(r'N/A', 0, regex=True)
    cases_table[0] = cases_table[0].replace({"\[[0-9a-z]*\]": ""}, regex=True)
    cases_table[0] = cases_table[0].replace({"\((\d+)\)": ""}, regex=True)
    print(cases_table)
    print("\n")
    return cases_table


def extract_deaths_table():
    pd.set_option('display.max_columns', None, 'display.max_rows', None, 'display.max_colwidth', 15,
                  'display.width', None)
    deaths_table = read_html(get_url(), index_col=0, attrs={"class": "wikitable"})
    deaths_table[0] = deaths_table[0].iloc[:-4, :]
    deaths_table[0] = deaths_table[0].drop_duplicates()
    deaths_table[0] = deaths_table[0].replace(r'—', 0, regex=True)
    deaths_table[0] = deaths_table[0].replace(r'N/A', 0, regex=True)
    deaths_table[0] = deaths_table[0].replace({"^(\d*)": ""}, regex=True)
    deaths_table[0] = deaths_table[0].replace(r'^\s*$', 0, regex=True)
    deaths_table[0] = deaths_table[0].replace({"\[[0-9a-z]*\]": ""}, regex=True)
    print(deaths_table)
    return deaths_table


def main():
    cases_table = extract_cases_table()
    deaths_table = extract_deaths_table()


if __name__ == '__main__':
    main()

