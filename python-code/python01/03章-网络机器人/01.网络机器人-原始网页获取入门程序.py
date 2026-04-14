import requests
"""
爬取：tiobe编程语言榜单 --> 入门程序只需要做到获取到页面的html文本内容
页面：https://www.tiobe.com/tiobe-index/

机器人协议：
    User-agent: *
    Disallow: /wp-admin/
    Allow: /wp-admin/admin-ajax.php
    Sitemap: https://www.tiobe.com/sitemap_index.xml
"""
# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 通过requests库，发送请求，获取响应数据对象
response = requests.get(target_url)

# 输出数据的文本到控制台
print(response.text)    # 输出页面的html文本内容