# Strategy3: Swap Content
# 通过交换源数据和孪生数据（即经过双向翻译的数据）的数据项扩充数据

# 设dataset1的数据为(q,r,s)，孪生数据datasetByS1为(q',r',s')
# 交换二者的question，得到新的数据集datasetByS3[(q',r,s),(q,r',s')]

import os

# 创建目录
if not os.path.exists("datasetByS3_1"):
    os.mkdir("datasetByS3_1")
if not os.path.exists("datasetByS3_2"):
    os.mkdir("datasetByS3_2")
with open('datasetByS1/question', 'r') as f1:
    with open("datasetByS3_1/question", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()
with open("dataset1/reference answer", 'r') as f1:
    with open("datasetByS3_1/reference answer", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()
with open("dataset1/student answer", 'r') as f1:
    with open("datasetByS3_1/student answer", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()

with open('dataset1/question', 'r') as f1:
    with open("datasetByS3_2/question", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()
with open("datasetByS1/reference answer", 'r') as f1:
    with open("datasetByS3_2/reference answer", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()
with open("datasetByS1/student answer", 'r') as f1:
    with open("datasetByS3_2/student answer", 'w') as f2:
        f2.write(f1.read())
        f1.close()
        f2.close()