import os
import streamlit as st
from session_manager import init_chat, render_chat, create_session, save_session, get_session_list, load_session, delete_session
from chat_service import build_memory, build_user_message, parse_llm_reply
from partner_settings import partner_setting, sync_partner_setting_from_current_session

# Latyout
# ページコンフィグ
st.set_page_config(
    page_title="AIパートナー",
    page_icon="👼",
    layout="wide",
    initial_sidebar_state="expanded",
)
# 初期化chat + チャット表示
init_chat()

# タイトル
st.title("AIパートナー")
st.text(st.session_state.current_session)
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
            if st.session_state.is_dirty:
                save_session(st.session_state.current_session)
                st.session_state.is_dirty = False

            # 2. 新しい会話を開始
            name, personality = "", ""
            create_session(name or "智能AI聊天伙伴Jack", personality or "阳光开朗，说话风格简练")
            # 同期化パートナー設定
            sync_partner_setting_from_current_session()
            st.rerun()

    # 会話履歴
    st.text("会話履歴")
    session_list = get_session_list()
    for session in session_list:
        session_bu, delete_bu = st.columns([4, 1])
        with session_bu:
            # 会話をロード
            if st.button(session, icon="📝", width="stretch", type="primary" if session ==st.session_state.current_session else "secondary"):
                # 現在の会話を保存
                if st.session_state.is_dirty:
                    save_session(st.session_state.current_session)
                    st.session_state.is_dirty = False
                # 過去会話をロード
                load_session(session)
                # 同期化パートナー設定
                sync_partner_setting_from_current_session()
                st.rerun()
        with delete_bu:
            if st.button("", icon="❌", key=f"delete_{session}", width="stretch"):
                delete_session( session)
                st.rerun()

    st.divider()

    # パートナー設定初期化
    st.subheader("パートナー設定")
    name = st.text_input("パートナーニックネーム", placeholder="パートナーのニックネームを設定してください", key="name")
    personality = st.text_area("パートナー性格", placeholder="パートナーの性格を設定してください", key="personality")
    # パートナー設定
    if st.button("設定応用"):
        is_applied = partner_setting(name, personality)
        if is_applied:
            save_session(st.session_state.current_session)
            st.success("設定を適用しました", icon="✅")
        else:
            st.warning("ニックネームまたは性格は設定されていません")

render_chat()

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

    # 一回目の会話で保存
    if not st.session_state.is_dirty:
        save_session(st.session_state.current_session)

    # 会話状態更新フラグ
    st.session_state.is_dirty = True
    st.rerun()
