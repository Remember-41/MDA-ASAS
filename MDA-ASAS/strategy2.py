# Strategy2: Correct Answer as Reference Answer
# 假设学生的正确答案可以作为参考答案来扩充数据
# 在这里，我们假设dataset1中student1的答案是正确答案，并由此构造datasetByS2
import os


# 创建路径datasetByS2
def creatPath(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        os.mkdir(path)
        return True
    else:
        return False


# 判断学生答案是否能作为参考答案,这里默认为正确答案
def isCorrect(file):
    if file == "student answer":
        return True


myPath = "datasetByS2"
creatPath(myPath)

# 判断学生答案是否正确
with open("dataset1/student answer", 'r' ):
    if isCorrect("student answer"):
        flag = 1

# 答案正确，则将该答案作为正确答案，并构建dataset3
# 同时，将dataset2的学生答案作为dataset3的学生答案
with open('dataset1/question', 'r') as f1:
    with open("datasetByS2/question", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()
with open("dataset1/student answer", 'r') as f1:
    with open("datasetByS2/reference answer", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()
with open("dataset2/student answer", 'r') as f1:
    with open("datasetByS2/student answer", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()


