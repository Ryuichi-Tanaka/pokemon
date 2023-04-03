import requests
from bs4 import BeautifulSoup
import streamlit as st
st.write("カード検索")
def search(query):
    url = f"https://jp.mercari.com/search?keyword={query}"
    response = requests.get(url)
    if response.status_code == 200:
        st.write("検索結果ページに飛びます。")
        st.write(response.url)
        st.write("")

p = st.text_input("")
bu = st.button("検索")
if bu:
    search(p)



# スクレイピング対象のURLを指定
url = "https://altema.jp/pokemoncard/pricedown"

# GETリクエストを送信してHTMLを取得
response = requests.get(url)

# HTMLをパースしてBeautifulSoupオブジェクトを作成
soup = BeautifulSoup(response.text, "html.parser")
"""
## 値下がりカード一覧
"""
# スクレイピング対象の要素を取得
tables = soup.find_all("table")
for table in tables:
    if "値下がりカード" in table.text:
        # tableの中のspan要素を取得
        spans = table.find_all("span")
        for span in spans:
            st.write(span.text)
            st.write(f"https://jp.mercari.com/search?keyword={span.text}")
