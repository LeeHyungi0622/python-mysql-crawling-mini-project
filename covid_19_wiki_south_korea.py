# -*- coding: utf-8 -*-
import enum
import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Korea"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'lxml')

outer_container = soup.find("div", {"class": "barbox tright"})
trs = outer_container.find_all("tr")


def filter_td_from_tr(trs):
    td_lst = []
    for tr in trs:
        td_dict = dict()
        for idx, td in enumerate(tr):
            if idx == 1:
                td_dict['Date'] = td.get_text()
            if idx == 5:
                td_dict['Cases'] = td.get_text()
            if idx == 7:
                td_dict['Death'] = td.get_text()
        td_lst.append(td_dict)
    return td_lst


print(len(filter_td_from_tr(trs)))
