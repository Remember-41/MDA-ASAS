# 未能完成对BERT的微调进行结果测试
# 这里使用了difflib库，通过比较参考答案和学生答案的文本相似度大致为简答题打分
# 但基于简答题的打分原则上不应基于文本相似度，这里的结果不具有说服力
import difflib


# 判断相似度的方法，用到了diff库
def get_equal_rate_1(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


# 执行方法进行验证
# 简单计算了dataset1的参考答案和学生答案的文本相似度，为0.6608695652173913，但结果不应具有说服力
if __name__ == '__main__':
    with open("dataset1/reference answer", 'r') as f:
        a = f.read()
        f.close()
    with open("dataset1/student answer", 'r') as f:
        b = f.read()
        f.close()
    print(get_equal_rate_1(a, b))
