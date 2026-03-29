#和文件相关的类
#定义一个抽象类，做顶层设计，确定有哪些功能需要实现
from data_define import Record
import json
class FileReader:
    def read_data(self)->list[Record]:
        """读取文件数据，将读取的数据都转化为Record对象,将他们封装到List列表中返回  """
        pass

#读取的是2011年1月分销售数据
class TextFileReader(FileReader):
    #获取文件路径
    def __init__(self,path):
        self.path=path #定义类内部的成员变量=外部传入的Path，类里面的成员变量就有值了
    
    #实现抽象方法
    def read_data(self)->list[Record]:
        f= open(self.path,'r',encoding='UTF-8')
        recode_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            recode_list.append(record)

        f.close()
        return recode_list
    

#读取2011年2月份销售数据JSON

class JsonFileReader(FileReader):#子类继承父类
    #获取文件路径
    def __init__(self,path):
        self.path = path#外部传入的path到类的成员方法里

    #读取文件，然后返回呗
    def read_data(self) ->Record:
        f = open(self.path,'r',encoding='UTF-8')
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

        

if __name__ == '__main__':

    text_file_reader = TextFileReader('D:/2011年1月销售数据.txt')
    json_file_reader = JsonFileReader('D:/2011年2月销售数据JSON.txt')
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)
    for l in list2:
        print(l)

