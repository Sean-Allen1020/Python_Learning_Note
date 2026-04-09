import streamlit as st

class InitPrompt:

    def __init__(self, system_prompt):
        self.system_prompt = system_prompt

    def init_chat(self):
        # 初期化chat
        partner = {'role': 'system', 'content': self.system_prompt}
        if "messages" not in st.session_state:
            st.session_state.messages = [partner]

        # チャット表示
        for message in st.session_state.messages:
            if message["role"] == "user" or message["role"] == "assistant":
                st.chat_message(message["role"]).write(message["content"])
            else:  # do nothing
                pass