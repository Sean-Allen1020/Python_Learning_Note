import streamlit as st
from openai import OpenAI

class ChatLogic:
    # api-key
    client = OpenAI(
        api_key='sk-api-1BwkK9M4g4qTozbBdmaRMmapJfSdTSqkJmuUkids86_wdVpMvWH5mnowgbdBtztlKV67pecqNPQaLpDv7enJoAhkjQe6m2Y4SSPu0_Cub0-rrpDt6TQjAQ4',
        base_url="https://api.minimaxi.com/v1"
    )
    def __init__(self, prompt):
        self.prompt = prompt

    # ユーザー入力
    def user_input(self):
        st.chat_message("user").write(self.prompt)
        print(f"----> 调用LLM，prompt：{self.prompt}")
        # ユーザーメッセージ保存
        user = {'role': 'user', 'content': self.prompt}
        return user

    # LLM呼び出し
    def call_llm(self):
        response = self.client.chat.completions.create(
            model="MiniMax-M2.7",
            messages=st.session_state.messages,
            stream=True,
            extra_body={"reasoning_split": True}
        )
        return response

    # LLM返事 (流式输出的解析方式)
    def llm_reply(self, response):
        with st.chat_message("assistant"):  # 创建一个消息框，用于显示LLM的回复，消息框内部程序执行完毕，消息框会自动关闭
            placeholder = st.empty()        # 创建一个占位符，用于显示实时的LLM回复
            reply = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    reply += chunk.choices[0].delta.content
                    placeholder.write(reply)
        print(f"----> LLM回复，reply：{reply}")

        # # LLM返事 (非流式输出的解析方式)
        # reply = response.choices[0].message.content
        # st.chat_message("assistant").write(reply)
        # print(f"----> LLM回复，reply：{reply}")

        # LLM返事保存
        assistant = {'role': 'assistant', 'content': reply}
        return assistant