# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
import lxml
# from sqlite3 import connect
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()

# MySQL Connector using pymysql
engine = create_engine("mysql+mysqldb://root:"+"1q2w3e4r" +
                       "@localhost/mywork", encoding="utf-8")

conn = engine.connect()

URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Korea"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'lxml')

outer_container = soup.find("div", {"class": "barbox tright"})
trs = outer_container.find_all("tr")[27:787]


def filter_td_from_tr(trs):
    td_lst = []
    for tr in trs:
        td_dict = dict()
        for idx, td in enumerate(tr):
            if idx == 1:
                td_dict['Date'] = td.get_text().strip()
            if idx == 5:
                td_dict['Cases'] = td.get_text().strip()
            if idx == 7:
                td_dict['Death'] = td.get_text().strip()
        td_lst.append(td_dict)
    return td_lst


print(filter_td_from_tr(trs))

covid_df = pd.DataFrame(filter_td_from_tr(trs))
print(covid_df)
