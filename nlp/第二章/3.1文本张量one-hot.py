#因为计算机只认张量数字，所以我们要把张量文本转换为张量数字，一般都是2的n次方

#名词是词向量

#one-hot 称为独热编码，只有一个元素是1 ，其他元素是0例如

""" 
["改变","要","如何","起手"]


[1,0,0,0]
[0,1,0,0]
[0,0,1,0]
[0,0,0,1]
 """
# ----------------------------------------------------------------------------------------


""" 
-------------one-hot优缺点:
                    优点：方便简单

                    缺点：词向量是一个稀疏值（0比较多，信息密度低），浪费存储和资源
                         对多义词的处理效果不行，过过过过过过，中的3对过的词向量是同一个

 """
#去掉警告的
import os
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

#导包
import joblib
from keras.src.legacy.preprocessing.text import Tokenizer

def demo1():
    #1准备数据
    vocabs = ["周杰伦","陈奕迅","王力宏","李宗盛","吴亦凡","鹿晗"]
    #2创建模型
    my_tokenizer = Tokenizer()
    #3进行训练
    my_tokenizer.fit_on_texts(vocabs)
    #4得到训练好的词语和映射关系 
    #word_index是字典   key是words，values是index是词索引  索引是从1开始的
    word_dict = my_tokenizer.word_index
    # print(word_dict)
    # print(type(word_dict))

    #5得到每个词的one-hot词向量
    for word in vocabs:
        #5.1初始化全0列表
        one_hot = [0]*len(vocabs)
        #5.2获得词在词汇映射器中的索引位置
        index = word_dict[word]-1
        #5.3指定位置的值设置为1
        one_hot[index]=1
        print(f'{word}--->{one_hot}')
    #6保存
    joblib.dump(my_tokenizer,r"nlp\第二章\model路径.pkl")
    
def demo2():
    word = '李宗盛'
    #1加载训练好的模型
    my_tokenizer = joblib.load(r"nlp\第二章\model路径.pkl")

    #f复制上面的
    #2映射字典
    word_dict = my_tokenizer.word_index
    #2.1初始化全0列表
    one_hot = [0]*len(word_dict)
    #2.2获得词在词汇映射器中的索引位置
    index = word_dict[word]-1
    #2.3指定位置的值设置为1
    one_hot[index]=1
    print(f'{word}--->{one_hot}')

def demo3():#用python源代码实现one-hot词向量，
    #1创建词汇量
    vocabs = ["周杰伦","陈奕迅","王力宏","李宗盛","吴亦凡","鹿晗"]
    #2创建全0列表
    for word in vocabs:
        one_hot = [0]*len(vocabs)
        #3获得索引
        index = vocabs.index(word)
        #词索引的位置改为1
        one_hot[index]=1
        print(f'{word}-->的词索引{index}-->词向量是{one_hot}')

if __name__ == '__main__':
    demo1()
    demo2()
    demo3()