from numpy import random
# 数据是16*8的矩阵
import numpy as np


class LetterData:
    data = []
    target = []

    def __init__(self):
        reader = open("./letter.data")
        i = 0
        for line in reader:
            i += 1
            lineList = line.split()
            symbol = np.zeros(26)
            info = ord(lineList[1]) - ord('a')
            symbol[info] = 1
            self.target.append(symbol)
            tmp = []
            for item in lineList[6:]:
                tmp.append(int(item))
            self.data.append(tmp)
        reader.close()


def take_test_set(k, letterdata):
    n = len(letterdata.data)
    indexlist = random.randint(0, n, size=k)
    result = {'data': [], 'target': []}
    for i in indexlist:
        result['data'].append(letterdata.data[i])
        result['target'].append(letterdata.target[i])
    return result