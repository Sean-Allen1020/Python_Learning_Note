import os
import streamlit as st
from InitPrompt import InitPrompt
from ChatLogic import ChatLogic
import system_prompt_settings

# Latyout
# ページコンフィグ
st.set_page_config(
    page_title="AIパートナー",
    page_icon="👼",
    layout="wide",
    initial_sidebar_state="expanded",
)
# タイトル
st.title("AIパートナー")
# logo
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "../resources", "logo.png")
st.logo(logo_path)
# サイドバー
with st.sidebar:
    st.subheader("設定")
    name = st.text_input("パートナーニックネーム", placeholder="パートナーのニックネームを設定してください")
    personality = st.text_area("パートナー性格", placeholder="パートナーの性格を設定してください")

# 初期化chat + チャット表示
system_prompt = SYSTEM_PROMPT
ip = InitPrompt(system_prompt)
ip.init_chat()

# チャット処理
prompt = st.chat_input("メッセージを入力してください")
if prompt:
    cl = ChatLogic(prompt)
    # ユーザー入力 + ユーザーメッセージ保存
    user = cl.user_input()
    st.session_state.messages.append(user)

    # LLM呼び出し
    response = cl.call_llm()

    # LLM返事 + LLM返事保存
    reply = cl.llm_reply(response)
    st.session_state.messages.append(reply)

