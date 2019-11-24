import jsonpath
import os
import xlrd

from config.setting import  log


def get_value(dic, key):
    '''
    这个函数是从一个字典里面，根据key获取vlaue
    :param dic:传一个字典
    :param key:传一个
    :return:如果有，返回key取到value，如果key没有，返回空字符串
    '''
    result = jsonpath.jsonpath(dic, '$..%s' % key)
    if result:
        return result[0]
    return ''


class GetTestData:

    @staticmethod
    def data_for_txt(file_name):
        log.debug('开始读取参数化文件%s' % file_name)
        if os.path.exists(file_name):
            with open(file_name, encoding='utf-8') as fr:
                data = []
                for line in fr:
                    if line.strip():
                        line_data = line.strip().split(',')
                        data.append(line_data)
            return data
        log.error('%s参数化文件不存在' % file_name)
        raise Exception('%s参数化文件不存在' % file_name)

    @staticmethod
    def data_for_excel(file_name, sheet_name=None):
        log.debug('开始读取参数化文件%s' % file_name)
        if os.path.exists(file_name):
            data = []
            book = xlrd.open_workbook(file_name)
            if sheet_name:
                sheet = book.sheet_by_name(sheet_name)
            else:
                sheet = book.sheet_by_index(0)
            for row_num in range(1, sheet.nrows):
                row_data = sheet.row_values(row_num)
                data.append(row_data)
            return data
        log.error('%s参数化文件不存在' % file_name)
        raise Exception('%s参数化文件不存在' % file_name)

    @staticmethod
    def data_for_mysql(sql):
        pass


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        cls.instance = super().__new__(cls)  #
        return cls.instance
