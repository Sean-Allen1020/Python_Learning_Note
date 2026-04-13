def triangle(base, height):
    """
    计算三角形面积

    :param base: 底
    :param height: 高
    :return: 面积
    """
    if height < 0 and base < 0:
        return 0
    else:
        return height * base / 2


def score_report(score_list):
    """
    统计出成绩单的相关数据
    :param score_list: 成绩单
    :return: 最低分，最高分，平均分
    """
    avg = round(sum(score_list) / len(score_list), 1)

    return min(score_list), max(score_list), avg


area = triangle(4, 6)
min_score, max_score, avg = score_report([89, 70, 98, 82])
print(f"三角形面积：{area}")
print(f"最低分：{min_score}，最高分：{max_score}，平均分：{avg}")
