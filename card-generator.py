from gimei import Gimei
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
import random
import sys

try:
    count = int(sys.argv[1])
    # Create a black image
    front_image = cv2.imread('front.jpg')
    back_image = cv2.imread('back.jpg')

    # Write some Text
    font_large        = ImageFont.truetype('MSMINCHO.TTF', 38)
    font_medium        = ImageFont.truetype('MSMINCHO.TTF', 32)
    font_small        = ImageFont.truetype('MSMINCHO.TTF', 24)
    fontColor              = (0,0,0)
    thickness              = 2
    lineType               = 2

    # Text positions
    name_pos = (100,50)
    address_pos = (100,110)
    birth_pos = (420,200)
    sex_pos = (1000, 150)
    num_pos = (300, 600)
    back_num_pos = (550, 180)
    back_name_pos = (580, 240)
    back_birth_pos = (750, 280)

    for i in range(1, count + 1):
        # Draw
        name = Gimei().name
        address = Gimei().address
        img_front = Image.fromarray(front_image)
        fdraw = ImageDraw.Draw(img_front)
        fdraw.text(name_pos, name.kanji, font = font_medium , fill=fontColor)
        address_str = address.kanji + str(random.choice(range(1,99))) + '-' + str(random.choice(range(1,3000)))
        fdraw.text(address_pos, address_str, font = font_small , fill=fontColor)
        year_word = random.choice(['令和', '昭和', '平成'])
        birth_str = year_word + str(random.choice(range(1,99))) + '年 ' + str(random.choice(range(1,12))) + '月 ' + str(random.choice(range(1,31))) + '日生'
        date_str =  str(random.choice(range(2025,2050))) + '年 ' + str(random.choice(range(1,12))) + '月 ' + str(random.choice(range(1,31))) + '日'
        fdraw.text(birth_pos, birth_str + '   ' + date_str, font = font_small , fill=fontColor)
        fdraw.text(sex_pos, random.choice(['男', '女']), font = font_medium , fill=fontColor)
        fdraw.text(num_pos, str(random.choice(range(1000, 9999))), font = font_medium , fill=fontColor)
        res_front = np.array(img_front)

        img_back = Image.fromarray(back_image)
        bdraw = ImageDraw.Draw(img_back)
        bdraw.text(back_num_pos, str(random.choice(range(1000, 9999))) + '     ' + str(random.choice(range(1000, 9999))) + '     ' + str(random.choice(range(1000, 9999))), font = font_large , fill=fontColor)
        bdraw.text(back_name_pos, name.kanji, font = font_small , fill=fontColor)
        bdraw.text(back_birth_pos, birth_str, font = font_small , fill=fontColor)
        res_back = np.array(img_back)

        #Save image
        cv2.imwrite(str(i) + "_front.jpg", res_front)
        cv2.imwrite(str(i) + "_back.jpg", res_back)
except:
    print('insert count of card')