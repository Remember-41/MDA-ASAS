# README

本项目是对于论文《Multiple Data Augmentation Strategies for Improving Performance on Automatic Short Answer Scoring》的工具复现。

## 1 论文理解

论文的主要内容是通过多种数据扩增的策略来提升自动简答题评分表现（MDA-ASAS）。目前，ASAS主要有两种方法，即传统方法和神经网络方法。由于ASAS的表现过于依赖于训练数据，因此，解决问题的关键在于提升训练数据的数据量。

论文中一共提出了三种数据扩增的策略：

- Back-translation
- Correct Answer as Reference Answer
- Swap Content

Back-translation，即双向翻译。原文中利用百度翻译，将英文翻译成日文，再将日文翻译为英文，将源数据扩增，并将扩增得到的数据称为源数据的孪生数据。（由于百度翻译需要注册开发人员，且API使用产生部分问题，故本项目中采用了有道翻译，且进行的是中英文双向翻译）

Correct Answer as Reference Answer，即正确答案视为参考答案。将学生的正确答案也视为一种参考答案，则可以将源数据集中的参考答案进行替换，得到新的扩增数据。

Swap Content，即交换内容。将源数据和其孪生数据的相关内容进行交换，从而得到新的数据集。

论文借助了BERT模型，进行了微调，测试了扩增数据的评分效果，发现使用策略3进行交换数据得到的扩增数据集测试效果最好。

最后论文还进行了广泛的消融研究，并为ASAS的实际使用提出了参数建议。

## 2 项目运行

#### 2.1 目录结构

```
│  README.md
│  strategy1.py
│  strategy2.py
│  strategy3.py
│  test.py
│          
├─dataset1
│      question
│      reference answer
│      student answer
│      
└─dataset2
        question
        reference answer
        student answer
```

其中，dataset1和dataset2为原始的两个数据集合，strategy分别对应论文中提到的三种数据扩增方法。

#### 2.2 数据扩增

1. 运行strategy1.py，会使用back-translation策略生成扩充数据datasetByS1。
2. 运行strategy2.py，会使用correct answer as reference answer策略生成扩充数据datasetByS2。
3. 运行strategy3.py，会使用swap content策略生成扩充数据datasetByS3_1和datasetByS3_2。

注意，strategy3应在strategy1后运行（strategy3交换的数据是基于strategy1的运行结果的）。

#### 2.3 测试数据

未能完成对BERT工具的微调，因此简单做了一个利用difflib库计算文本相似度的测试test.py。

BERT工具的GitHub地址：https://github.com/huggingface/pytorch-pretrained-BERT

由于未能找到作者所使用的数据集，因此未能完成脚本测试。

#### 2.4 演示视频

链接：https://pan.baidu.com/s/1qP8plodxokE6MqcyijqRxg

提取码：tw96