'''
Use Module:PIL
PIL可以帮助编辑图片
PIL导入只使用from PIL import XXX 模式
'''

from PIL import Image, ImageFont, ImageDraw

MyFontPath = "//Library/Fonts/Papyrus.ttc"
font = ImageFont.truetype(MyFontPath, 50) #50 means fontsize

MyPicPath = "IMG_1.JPG"
MyPic = Image.open(MyPicPath)

draw = ImageDraw.Draw(MyPic)
draw.ellipse([40,60,210,120], fill = None, outline = (255,255,255), width = 2) #画椭圆
draw.text((50,60), "Love You", fill = (0,0,0), font = font)

MyPic.show()
