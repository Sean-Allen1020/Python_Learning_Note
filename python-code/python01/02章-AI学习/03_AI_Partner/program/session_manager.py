import os
import json
import streamlit as st
import program_path
from datetime import datetime
from prompt_builder import build_partner_prompt

# 新しい会話を初期化
def create_session(name: str = "智能AI聊天伙伴Jack", personality: str = "阳光开朗，说话风格简练"):
    # 新しい会話を初期化
    new_system_prompt = build_partner_prompt(name, personality)
    partner = {'role': 'system', 'content': new_system_prompt}
    st.session_state.messages = [partner]
    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    st.session_state.is_dirty = False

# 初期化chat + チャット表示
def init_chat(name: str = "智能AI聊天伙伴Jack", personality: str = "阳光开朗，说话风格简练"):
    # 初期化パートナープロンプト
    if "messages" not in st.session_state or "current_session" not in st.session_state or "is_dirty" not in st.session_state:
        create_session(name, personality)

# チャット表示
def render_chat():
    for message in st.session_state.messages:
        if message["role"] == "user" or message["role"] == "assistant":
            st.chat_message(message["role"]).write(message["content"])

# 会話保存
def save_session(current_session: str):
    # やり取り一回以上の場合は保存する
    if len(st.session_state.messages) > 1:
        if not os.path.exists(program_path.SESSION_DIR):
            os.mkdir(program_path.SESSION_DIR)
        with open(f"{program_path.SESSION_DIR}/{current_session}.json", "w", encoding="utf-8") as f:
            session_data = {
                "current_session": st.session_state.current_session,
                "messages": st.session_state.messages
            }
            json.dump(session_data, f, ensure_ascii=False, indent=4)
    else:
        pass

# 会話履歴リスト取得
def get_session_list():
    session_list = []
    if os.path.exists(program_path.SESSION_DIR):
        for filename in os.listdir(program_path.SESSION_DIR):
            if filename.endswith(".json"):
                session_list.append(filename.split(".")[0])

    session_list.reverse()
    return session_list

#　会話履歴ロード
def load_session(session):
    try:
        if os.path.exists(f"{program_path.SESSION_DIR}/{session}.json"):
            with open(f"{program_path.SESSION_DIR}/{session}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.current_session = session
                st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error("会話履歴が見つかりません")

# 会話履歴削除
def delete_session(session):
    try:
        if os.path.exists(f"{program_path.SESSION_DIR}/{session}.json"):
            # 現在の会話を削除する場合は、新規会話を初期化
            if session == st.session_state.current_session:
                st.session_state.name = ""
                st.session_state.personality = ""
                create_session()
            # 他の会話を削除する場合は、そのまま実行
            os.remove(f"{program_path.SESSION_DIR}/{session}.json")
    except Exception as e:
        st.error("会話履歴が見つかりません")
