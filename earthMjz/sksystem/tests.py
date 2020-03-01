import re
def data_replace(self, data):
    data = {'username': 'dsx', 'password': '${password}', 'age': '18'}
    for k, v in data.items():
        keys = re.findall(r'\$\{(.*?)\}', str(v))
        print(keys)

if __name__ == '__main__':
    data_replace(11,11)