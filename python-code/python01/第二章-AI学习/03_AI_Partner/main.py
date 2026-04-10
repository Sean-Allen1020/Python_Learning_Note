import os
from datetime import datetime
import streamlit as st
from chat_operation import init_chat, start_new_session, save_session, get_session_list, load_session, delete_session
from chat_service import build_memory, build_user_message, parse_llm_reply

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
    # 新しい会話
    st.subheader("会話操作")
    if st.button("新しい会話", icon="✏️", width="stretch"):
        if st.session_state.current_session:
            # 1. 現在の会話を保存
            if len(st.session_state.messages) > 2:
                save_session(st.session_state.current_session)
            else:
                pass
            # 2. 新しい会話を開始
            name, personality = "", ""
            new_session_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            start_new_session(new_session_name, name or "智能AI聊天伙伴Jack", personality or "阳光开朗，说话风格简练")

    # 会話履歴
    st.text("会話履歴")
    session_list = get_session_list()
    for session in session_list:
        session_bu, delete_bu = st.columns([4, 1])
        with session_bu:
            # 過去会話をロード
            if st.button(session, icon="📝", width="stretch"):
                save_session(session)
                load_session(session)
        with delete_bu:
            if st.button("", icon="❌", key=f"delete_{session}", width="stretch"):
                delete_session( session)
                st.rerun()

    # パートナー設定
    st.subheader("パートナー設定")
    name = st.text_input("パートナーニックネーム", placeholder="パートナーのニックネームを設定してください", key="name")
    personality = st.text_area("パートナー性格", placeholder="パートナーの性格を設定してください", key="personality")

# 初期化chat + チャット表示
init_chat(name or "智能AI聊天伴侣Jack", personality or "阳光开朗，说话风格简练")

# チャット処理
prompt = st.chat_input("メッセージを入力してください")
if prompt:
    # ユーザー入力 + ユーザーメッセージ保存
    user = build_user_message(prompt)
    st.session_state.messages.append(user)

    # LLM返事取得
    response = build_memory()

    # LLM返事解析 + LLM返事保存
    reply = parse_llm_reply(response)
    st.session_state.messages.append(reply)
