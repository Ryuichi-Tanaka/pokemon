import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


st.write("バイオレットex買取")

if st.checkbox("相場の確認"):
    # スクレイピング対象のURLを指定
    url = "https://pokemon-infomation.com/market-price-violetex/"

    # GETリクエストを送信してHTMLを取得
    response = requests.get(url)

    # HTMLをパースしてBeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.text, "html.parser")

    # スクレイピング対象の要素を取得
    target_element = soup.find("tr")

    for a in soup.find_all("tr"):
        if "販売価格" in a.text:
            break
        else:
            st.write(a.text)