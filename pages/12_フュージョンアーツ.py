import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


st.write("フュージョンアーツ買取")


# スクレイピング対象のURLを指定
url = "https://osomatsusan.hatenablog.com/entry/pokeca_FUSION_SR_SA"

# GETリクエストを送信してHTMLを取得
response = requests.get(url)

# HTMLをパースしてBeautifulSoupオブジェクトを作成
soup = BeautifulSoup(response.text, "html.parser")

# スクin targett:レイピング対象の要素を取得
target = soup.find("ol")
for i in soup.find("ol"):
    st.write(i.text)