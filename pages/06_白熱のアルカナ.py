import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

st.write("白熱のアルカナ買取")

if st.checkbox("相場の確認"):
    # スクレイピング対象のURLを指定
    url = "https://pokemon-infomation.com/market-price-incandescentarcana/"

    # GETリクエストを送信してHTMLを取得
    response = requests.get(url)

    # HTMLをパースしてBeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.text, "html.parser")

    # スクレイピング対象の要素を取得
    target_element = soup.find("table")
    # pandasのread_htmlメソッドでHTMLのテーブルをDataFrameに変換
    df = pd.read_html(str(target_element))[0]
    st.write(df)
