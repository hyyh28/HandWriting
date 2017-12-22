import os
from PIL import Image
import numpy as np


def splitimage(src, rownum, colnum, dstpath):
    result = []
    img = Image.open(src)
    img = img.convert('L')
    img = img.convert('1')
    w, h = img.size
    #print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
    #print('开始处理图片切割, 请稍候...')

    s = os.path.split(src)
    if dstpath == '':
         dstpath = s[0]
    fn = s[1].split('.')
    basename = fn[0]
    ext = fn[-1]

    num = 0
    rowheight = h // rownum
    colwidth = w // colnum
    for r in range(rownum):
        for c in range(colnum):
            box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
            Img = img.crop(box)
            tmpdepth = './TempData'
            img.crop(box).save(os.path.join(tmpdepth, basename + '_' + str(num) + '.' + ext), ext)
            data = Img.getdata()
            data = np.matrix(data, dtype='int')/255
            data1= -data + 1
            new_data = np.reshape(data1, (1, 128)).tolist()
            result.append(new_data[0])
           # print(new_data[0])
            num = num + 1
            #Img.show()
    #print('图片切割完毕，共生成 %s 张小图片。' % num)
    return result


def test(src):
    if os.path.isfile(src):
        dstpath = './TempData/'
        if (dstpath == '') or os.path.exists(dstpath):
            result = splitimage(src, 1, 4, dstpath)
            return result
