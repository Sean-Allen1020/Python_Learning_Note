from lxml import html

with open("resource/Xpath演示.html", "r", encoding="utf-8") as f:
    content = f.read()
    doc = html.fromstring(content)

    # / 根元素节点开始，获取内容
    title = doc.xpath("/html/body/div/h1/text()")
    print(title)

    # // 任意元素节点考试，获取内容
    title = doc.xpath("//h1/text()")
    print(title)

    # . 当前元素节点开始，获取内容
    title = doc.xpath("//h1")  # 获取h1元素对象列表 (一个元素也是列表)
    text = title[0].xpath("./text()")  # 从当前元素节点开始获取文本内容
    print(text)

    # [n] 获取第n个元素
    student001 = doc.xpath("//ul/li[1]/text()")  # 获取第一个li元素的文本内容
    print(student001)

    # [last()] 获取最后一个元素节点
    student003 = doc.xpath("//ul/li[last()]/text()")  # 获取最后一个li元素的文本内容
    print(student003)

    # [@attr] 获取有该属性的元素
    p_list = doc.xpath("//p[@style]/text()")
    print(p_list)

    # [@attr="value"] 获取属性值为value的元素
    p_red = doc.xpath("//p[@style='color: #FF0000;']/text()")
    print(p_red)

    # 通配符
    # * 获取所有元素
    div1 = doc.xpath("//div[@class='section'][1]/*/text()")
    print(div1)

    # @* 获取指定元素内所有属性的值
    li1_attrs = doc.xpath("//li[1]/@*")
    print(li1_attrs)

    # @attr 获取指定元素内指定属性的值
    li1_style = doc.xpath("//li[1]/@class")
    print(li1_style)
