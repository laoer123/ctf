from PIL import Image
import re
if __name__ == '__main__':
    x = 887 //将像素点个数进行分解，可以确定图片的长宽
    y = 111
    i = 0
    j = 0
     
    c = Image.new("RGB", (x,y))
    file_object = open('ce.txt') //ce.txt中保存着像素点的坐标
     
    for i in range(0,  x): 
        for j in range(0,  y):
            line = file_object.next() //每次读取一个像素点
            lst = line.split(",") //lst生成一个元组
            c.putpixel((i, j), (int(lst[0]), int(lst[1]), int(lst[2])))
     
    c.show()
    c.save("c.png")