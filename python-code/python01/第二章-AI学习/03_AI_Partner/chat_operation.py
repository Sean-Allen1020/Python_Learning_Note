import os
import json
import streamlit as st
from datetime import datetime
from system_prompt_settings import build_partner_prompt

# 初期化chat + チャット表示
def init_chat(name: str, personality: str):
    # 初期化パートナープロンプト
    system_prompt = build_partner_prompt(name, personality)
    partner = {'role': 'system', 'content': system_prompt}
    if "messages" not in st.session_state:
        st.session_state.messages = [partner]
    else:
        st.session_state.messages[0] = partner  # 昵称，性格更新后，实时更新 system_prompt

    # 初期化会話タイトル
    if "current_session" not in st.session_state:
        st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # チャット表示
    for message in st.session_state.messages:
        if message["role"] == "user" or message["role"] == "assistant":
            st.chat_message(message["role"]).write(message["content"])
        else:  # do nothing
            pass

# 新しい会話を初期化
def start_new_session(session_name: str, new_partner_name: str, new_partner_personality: str):
    # 新しい会話を初期化
    new_system_prompt = build_partner_prompt(new_partner_name, new_partner_personality)
    partner = {'role': 'system', 'content': new_system_prompt}
    st.session_state.messages = [partner]
    st.session_state.current_session = session_name

# 会話保存
def save_session(current_session: str):
    if not os.path.exists("./session_data"):
        os.mkdir("./session_data")
    with open(f"./session_data/{current_session}.json", "w", encoding="utf-8") as f:
        session_data = {
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        json.dump(session_data, f, ensure_ascii=False, indent=4)

# 会話履歴リスト取得
def get_session_list():
    session_list = []
    if os.path.exists("./session_data"):
        for filename in os.listdir("./session_data"):
            if filename.endswith(".json"):
                session_list.append(filename.split(".")[0])

    return session_list

#　会話履歴ロード
def load_session(session):
    if os.path.exists(f"./session_data/{session}.json"):
        with open(f"./session_data/{session}.json", "r", encoding="utf-8") as f:
            session_data = json.load(f)
            st.session_state.current_session = session_data["current_session"]
            st.session_state.messages = session_data["messages"]
    else:
        st.error("会話履歴が見つかりません")

# 会話履歴削除
def delete_session(session):
    if os.path.exists(f"./session_data/{session}.json"):
        os.remove(f"./session_data/{session}.json")
    else:
        st.error("会話履歴が見つかりません")
