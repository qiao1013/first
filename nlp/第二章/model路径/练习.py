


#导包
import jieba
import joblib
from keras.src.legacy.preprocessing.text import Tokenizer
#hot_one
def demo1():
    #1创建数据
    vocabs = ["周杰伦","陈奕迅","王力宏","李宗盛","吴亦凡","鹿晗"]
    #创建sklear模型
    my_tokenizer = Tokenizer()
    #进行训练
    my_tokenizer.fit_on_texts(vocabs)
    #训练好以后，分字典，key value
    word_dict = my_tokenizer.word_index
    #进入循环,目的是得到每个词的one-hot向量
    for word in vocabs:
        #创建0向量张量
        hot_one = [0]*len(vocabs)
        #拿到索引
        index = word_dict[word]-1
        #通过索引设置1
        hot_one[index]=1
        print(f'{word}的词索引为{index},词向量{hot_one}')

    joblib.dump(my_tokenizer,r'nlp\第二章\model路径.pkl')

def demo2():
    #
    word ='李宗盛'
    #加载模型
    my_tokenizer = joblib.load(r'nlp\第二章\model路径.pkl')
    word_dict = my_tokenizer.word_index
    #创建0向量张量
    hot_one = [0]*len(word_dict)
    #拿到索引
    index = word_dict[word]-1
    #通过索引设置1
    hot_one[index]=1
    print(f'{word}的词索引为{index},词向量{hot_one}')

def demo3():
    pass

if __name__ == '__main__':
    demo1()
    demo2()