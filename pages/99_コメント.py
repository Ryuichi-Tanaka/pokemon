import streamlit as st
from datetime import datetime

# 初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# メッセージを追加
message = st.text_input("メッセージを入力してください")
if st.button("投稿"):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.session_state.messages.append({"message": message, "date": now})

# メッセージを表示
if len(st.session_state.messages) > 0:
    st.write("投稿されたメッセージ:")
    for idx, msg in enumerate(st.session_state.messages):
        st.write(f"{idx+1}. {msg['message']} ({msg['date']})")
        if st.button(f"削除 {idx+1}"):
            st.session_state.messages.pop(idx)
else:
    st.write("まだ投稿されたメッセージはありません。")
