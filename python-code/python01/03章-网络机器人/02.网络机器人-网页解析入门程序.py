from lxml import html

# 读取html页面
with open("resource/网页解析演示.html", "r", encoding="utf-8") as f:
    # 获取html文本字符串
    html_content = f.read()

    # 解析html文本字符串，封装为html对象 -- 因为读的是字符串，所以用fromstring方法
    doc = html.fromstring(html_content)

    # 调用 xpath方法，通过xpath表达式，获取到所有精准信息
    # 获取表头
    headers = doc.xpath('//table/thead/tr/th/text()')
    print(headers)
    # 获取表体
    rows = doc.xpath('//table/tbody/tr')  # 如果不指定 text()，则会将元素内容封装成对象列表
    for row in rows:
        cells = row.xpath('./td/text()')
        print(cells)

    # 获取单行表体 -- 在 tr 处添加索引，第一行索引为1，而非0
    row = doc.xpath('//table/tbody/tr[1]/td/text()')
    print(row)