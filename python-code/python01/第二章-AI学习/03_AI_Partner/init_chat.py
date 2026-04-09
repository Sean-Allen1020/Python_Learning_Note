import streamlit as st

def init_chat(system_prompt: str):
    # 初期化chat
    partner = {'role': 'system', 'content': system_prompt}
    if "messages" not in st.session_state:
        st.session_state.messages = [partner]
    else:
        # 昵称，性格更新后，实时更新 system_prompt
        st.session_state.messages[0] = partner

    # チャット表示
    for message in st.session_state.messages:
        if message["role"] == "user" or message["role"] == "assistant":
            st.chat_message(message["role"]).write(message["content"])
        else:  # do nothing
            pass