import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Streamlit演示",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config',
        'Report a bug': "https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config",
        'About': "# 这是一个Streamlit演示"
    }
)

# 标题
st.title('Streamlit 入门演示')
st.header('一级标题')
st.subheader('二级标题')

# 段落文字
st.write('法国大革命')
st.write('【历史现场氛围】')
st.write(
    '想象一下革命前夜的法国：宫廷里依旧灯火通明，贵族们穿着华服跳舞、吃宴席，仿佛这个国家永远不会出事；可在宫墙之外，巴黎街头和乡村田地里，空气已经紧得像一根快要崩断的弦。国王犹豫、贵族傲慢、百姓愤怒，面包越来越贵，税却一分不少，连“说句公道话”的路都快被堵死了。最危险的地方就在这里：不是所有人都已经饿到活不下去，而是越来越多人突然意识到——“为什么偏偏是我们在承担一切？”当这种愤怒和“不服”同时点燃，一个时代就真的会被掀翻。')

# 图片，视频，音频
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7BT1otU8-BEyrpbjOWCHg11ONZZm2H84eag&s')
# st.video
# st.audio

# 网页logo -- 会展示在网页左上角
st.logo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5nh-qUMtj1ySxMlbB-ufqm3O-0s9iLlajTQ&s')

# 表格
student_data = {
    '姓名': ['孙中山', '蒋介石', '毛泽东', '华国锋'],
    '成绩': [100, 1000, 6000, 10]
}
st.table(student_data)

# 输入框
name = st.text_input('请输入姓名')
st.write(f'你好，{name}')
# 输入框 -- 密码
password = st.text_input('请输入密码', type='password')
st.write(f'你的密码是：{password}')

# 单选
gender = st.radio('请选择性别', ['男', '女'])
st.write(f'你的性别是：{gender}')
