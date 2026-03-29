import jieba


# 掌握jieba.lcut(content)



#全词模式：
def demo1():
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    #带lcut
    words = jieba.lcut(content)
    print(words)
    #不带lcut <class 'generator'>generator是生成器
    result = jieba.cut(content)
    print(type(result))

#精确模式：分的更加仔细
def demo2():
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    words = jieba.lcut(content,cut_all = True)
    print(words)
#搜索引擎模式：不带cut_all
def demo3():
    content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    words = jieba.lcut_for_search(content)
    print(words)

if __name__ == '__main__':
    demo1()

    demo2()

    demo3()
