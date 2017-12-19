# 数据是16*8的矩阵
def read_data():
    reader = open("./letter.data")
    i = 0
    letterData = {'data': [], 'target': []}
    for line in reader:
        i += 1
        lineList = line.split()
        letterData['target'].append(lineList[1])
        tmp = []
        for item in lineList[6:]:
            tmp.append(int(item))
        letterData['data'].append(tmp)
    reader.close()
    return letterData
