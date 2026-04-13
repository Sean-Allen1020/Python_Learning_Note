import os
import streamlit as st
import program_path
from dotenv import load_dotenv
from openai import OpenAI

# 環境変数を取得
load_dotenv(program_path.PROJECT_DIR / ".env")
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME", "MiniMax-M2.7")

# api-key
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

# ユーザー入力
def build_user_message(prompt):
    st.chat_message("user").write(prompt)
    print(f"----> 调用LLM，prompt：{prompt}")
    # ユーザーメッセージ保存
    user = {'role': 'user', 'content': prompt}
    return user

# LLM返事取得
def build_memory():
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=st.session_state.messages,
        stream=True,
        extra_body={"reasoning_split": True}
    )
    return response

# LLM返事解析 (流式输出的解析方式)
def parse_llm_reply(response):
    with st.chat_message("assistant"):  # 创建一个消息框，用于显示LLM的回复，消息框内部程序执行完毕，消息框会自动关闭
        placeholder = st.empty()  # 创建一个占位符，用于显示实时的LLM回复
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
