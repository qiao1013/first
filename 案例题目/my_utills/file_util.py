""" 
文件相关的处理工具
"""
def print_file_info(file_name):  #接收传入路径，打印内容，不存在则捕获异常，输出提示信息，finally关闭
    try:
        f = open(file_name,'r',encoding='UTF-8')
        for line in f:
            print(line)
    except Exception as e:
        print("文件不存在")
        print(f"异常情况时：{e}")
    finally:
        if 'f' in locals() and f:
            f.close()

def append_to_file(file_name,data):           #接收路径，传入数据，追加写入到文件中
    try:
        f = open(file_name,'a',encoding='UTF-8')
        f.write(f"\n{data}\n")
    except Exception as e:
        print(f"写入文件时出错：{e}")
    finally:
        if 'f' in locals() and f:
            f.close()


# append_to_file("D:/bili.txt","乔冠迪买了一辆奥迪A6L")