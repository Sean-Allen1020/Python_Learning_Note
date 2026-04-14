from lxml import html
import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"
# 发送请求，获取原始网页对象
response = requests.get(target_url)
# 将原始网页文本封装为html对象
doc = html.fromstring(response.text)

# 解析原始网页
# 获取表头
headers = doc.xpath("//*[@id='top20']/thead/tr/th/text()")
print(headers)

# 获取表体
rows = doc.xpath("//*[@id='top20']/tbody/tr")
for row in rows:
    cells = row.xpath("./td/text()")
    print(cells)

