import requests             # 网页请求
import csv                  # csv操作
from lxml import html       # 原始网页解析
from pathlib import Path    # 文件io路径操作

"""
案例：获取高分电影榜单（Top100）数据，并保存在CSV文件中
     数据包括： 电影名、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、Slogan、简介。

网址：https://www.themoviedb.org/movie/top-rated

机器人协议：只有黑名单，没有全局禁止
"""
# 中文请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

# 对未知数据进行统一处理
def get_text(doc, xpath_expr: str, default_value: str = "未知"):
    result = doc.xpath(xpath_expr)
    if result:
        return result[0].strip()
    return default_value


# 获取电影详细信息
def get_movie_info(movie_url: str)-> dict:
    # 1. 获取电影详情原始网页
    response = requests.get(movie_url, headers=HEADERS)
    # 2. 解析，获取详情数据
    doc = html.fromstring(response.text)
    movie_info = {
        "电影名": get_text(doc, "//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()"),
        "年份": get_text(doc, "//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()"),
        "上映时间": get_text(doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()"),
        "类型": ", ".join(doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")),
        "时长": get_text(doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()"),
        "评分": doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/div/span/@class")[0].strip()[-2:],
        "语言": get_text(doc, "//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()"),
        "导演": get_text(doc, "//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()"),
        "作者": get_text(doc, "//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()"),
        "主演": ", ".join(doc.xpath("//*[@id='cast_scroller']/ol/li/p[2]/text()")),
        "Slogan": get_text(doc, "//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()"),
        "简介": get_text(doc, "//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    }
    # 3. 返回数据
    return movie_info


# 保存数据为csv文件
def save_movies(all_movies: list):
    pass
    # 创建CSV目录
    csv_path = Path(__file__).resolve().parent / "movies_data"
    csv_path.mkdir(parents=True, exist_ok=True)
    # 打开CSV文件
    with open(csv_path / "top_rated_movies.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "作者", "主演", "Slogan", "简介"])
        # 写入表头
        writer.writeheader()
        # 写入数据
        writer.writerows(all_movies)


def main():
    # 网页链接
    TMDB_BASE_URL = "https://www.themoviedb.org"  # 基础网址
    TMDB_TOP_URL = TMDB_BASE_URL + "/movie/top-rated"  # 高分电影榜单

    # 1. 获取原始网页对象
    response = requests.get(TMDB_TOP_URL, headers=HEADERS)

    # 2. 解析原始网页，获取电影链接列表
    doc = html.fromstring(response.text)
    movie_href = doc.xpath("//div[@class='media-card-list contents w-full']//a[@class='flex w-full']/@href")

    # 3. 遍历电影链接列表，获取电影详情
    all_movies = []
    if movie_href:
        for m in movie_href:
            movie_info = get_movie_info(TMDB_BASE_URL + m)
            all_movies.append(movie_info)

    # 4. 保存数据为csv文件
    save_movies(all_movies)


if __name__ == '__main__':
    main()





