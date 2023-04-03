import streamlit as st
import requests
from bs4 import BeautifulSoup

# スクレイピング対象のURLを指定
url = "https://altema.jp/pokemoncard/pricedown"

# GETリクエストを送信してHTMLを取得
response = requests.get(url)

# HTMLをパースしてBeautifulSoupオブジェクトを作成
soup = BeautifulSoup(response.text, "html.parser")

# スクレイピング対象の要素を取得
tables = soup.find_all("table")
for table in tables:
    if "値下がりカード" in table.text:
            st.write(table.text)
