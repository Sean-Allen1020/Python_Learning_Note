import streamlit as st
import re
from prompt_builder import build_partner_prompt

# パートナ設定
def partner_setting(name: str, personality: str):
    if name != "" or personality != "":
        system_prompt = build_partner_prompt(name, personality)
        partner = {'role': 'system', 'content': system_prompt}
        st.session_state.messages[0] = partner

        return True
    return False

# パートナ　ニックネーム、性格を取得
def extract_partner_info(system_prompt: str):

    name_match = re.search(
        r"你叫\s*(.*?)\s*，现在是用户的真实(?:伴侣|朋友)",
        system_prompt,
        re.S
    )
    personality_match = re.search(
        r"(?:伴侣|朋友)性格：\s*-\s*(.*?)\s*你必须严格遵守上述规则",
        system_prompt,
        re.S
    )
    name = name_match.group(1).strip() if name_match else ""
    personality = personality_match.group(1).strip() if personality_match else ""

    return name, personality

# パートナ設定を同期化
def sync_partner_setting_from_current_session():
    if "messages" in st.session_state and st.session_state.messages:
        system_prompt = st.session_state.messages[0]["content"]
        name, personality = extract_partner_info(system_prompt)

        if name == "智能AI聊天伙伴Jack":
            name = ""
        if personality == "阳光开朗，说话风格简练":
            personality = ""

        st.session_state.name = name
        st.session_state.personality = personality
