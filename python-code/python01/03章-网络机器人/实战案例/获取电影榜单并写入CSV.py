import requests  # 网页请求
import csv  # csv操作
from lxml import html  # 原始网页解析
from pathlib import Path  # 文件io路径操作
import re

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
# 网页链接
TMDB_BASE_URL = "https://www.themoviedb.org"  # 基础网址
TMDB_TOP_URL_P1 = TMDB_BASE_URL + "/movie/top-rated"  # 高分电影榜单(第一页)
TMDB_TOP_URL_PREST = TMDB_BASE_URL + "/discover/movie/items"  # 高分电影榜单(剩余页)


# 对未知数据进行统一处理
def get_text(doc, xpath_expr: str, default_value: str = "-") -> str:
    result = doc.xpath(xpath_expr)
    if result:
        if len(result) == 1:
            return result[0].strip()
        else:
            return ", ".join(result)
    return default_value


# 对 年份，上映时间，时长 三个数据进行格式化处理
def format_value(doc, xpath_expr: str) -> str:
    time_str = get_text(doc, xpath_expr)
    if time_str == "-":
        return time_str

    # 年份: (1994) -> 1994
    match = re.fullmatch(r"\((\d{4})\)", time_str)
    if match:
        # return time_str.replace("(", "").replace(")", "")
        # return time_str.strip("()")
        return match.group(1)

    # 上映时间: 1995-06-03 (JP) -> 1995-06-03
    match = re.fullmatch(r"(\d{4}-\d{2}-\d{2})\s+\([A-Z]+\)", time_str)
    if match:
        # return time_str.split(" ")[0]
        return match.group(1)

    # 时长: 2h 22m / 49m / 1h -> 统一换算成分钟
    match = re.fullmatch(r"(?:(\d+)h)?\s*(?:(\d+)m)?", time_str)
    if match:
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        return str(hours * 60 + minutes)

    return time_str


# 获取电影详细信息
def get_movie_info(movie_url: str) -> dict:
    # 1. 获取电影详情原始网页
    print(f"发送请求，获取电影详情原始网页：{movie_url} ...")
    response = requests.get(movie_url, headers=HEADERS)
    # 2. 解析，获取详情数据
    doc = html.fromstring(response.text)
    movie_info = {
        "电影名": get_text(doc, "//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()"),
        "年份": format_value(doc, "//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()"),
        "上映时间": format_value(doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()"),
        "类型": get_text(doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()"),
        "时长(m)": format_value(doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()"),
        "评分": get_text(doc, "//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent"),
        "语言": get_text(doc, "//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()"),
        "导演": get_text(doc, "//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()"),
        "作者": get_text(doc, "//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()"),
        "主演": get_text(doc, "//*[@id='cast_scroller']/ol/li/p[2]/text()"),
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
        writer = csv.DictWriter(f, fieldnames=["电影名", "年份", "上映时间", "类型", "时长(m)", "评分", "语言", "导演",
                                               "作者", "主演", "Slogan", "简介"])
        # 写入表头
        writer.writeheader()
        # 写入数据
        writer.writerows(all_movies)


def main():
    all_movies = []
    for page_num in range(1, 6):
        # 1. 获取原始网页对象
        print(f"发送请求，获取高分电影榜单原始网页, 第{page_num}页 ...")
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_P1, headers=HEADERS)
        else:
            response = requests.post(TMDB_TOP_URL_PREST,
                                     data=f"air_date.gte=&air_date.lte=&certification=&certification_country=JP&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-10-14&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=JP&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                     headers=HEADERS)

        # 2. 解析原始网页，获取电影链接列表
        doc = html.fromstring(response.text)
        movie_href = doc.xpath("//div[@class='media-card-list contents w-full']//a[@class='flex w-full']/@href")

        # 3. 遍历电影链接列表，获取电影详情
        if movie_href:
            for m in movie_href:
                movie_info = get_movie_info(TMDB_BASE_URL + m)
                all_movies.append(movie_info)

    # 4. 保存数据为csv文件
    print("开始保存数据为csv文件 ...")
    save_movies(all_movies)
    print("数据保存完成")


if __name__ == '__main__':
    main()
