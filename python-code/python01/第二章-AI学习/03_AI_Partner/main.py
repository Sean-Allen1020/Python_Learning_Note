import os
import streamlit as st
from init_chat import init_chat
from chat_service import build_memory, build_user_message, parse_llm_reply
from system_prompt_settings import build_partner_prompt

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
final_name = name or "智能AI聊天伴侣"     # name 为假时，触发默认名
final_personality = personality or "阳光开朗，语句简练"  # personality 为假时，触发默认性格
init_chat(build_partner_prompt(final_name, final_personality))

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
