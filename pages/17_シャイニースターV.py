import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


st.write("白銀のランス買取")


# スクレイピング対象のURLを指定
url = "https://altema.jp/pokemoncard/shinystarv"

# GETリクエストを送信してHTMLを取得
response = requests.get(url)

# HTMLをパースしてBeautifulSoupオブジェクトを作成
soup = BeautifulSoup(response.text, "html.parser")


# スクレイピング対象の要素を取得
tables = soup.find_all("table")

for table in tables:
    if "順位" in table.text:
        print(table.text)