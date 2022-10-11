#-*- coding: utf-8 -*-
import os
import shutil

from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


img_ext = ['.jpg','.jpeg','.JPG','.png','.bmp']     # 이미지 확장지
video_ext = ['.mp4','.avi','.mts','.m2ts','.MTS']   # 비디디 확장자
DEBUG = False
img_list = []
video_list = []
etc_list =[]

cur_dir =  os.getcwd()
if DEBUG :
    print('img_list length : ',len(img_list))
    print(f'current_dir : {cur_dir}')

def getImageDate(image,DEBUG=False):
    '''
    이미지 EXIF 정보를 읽어, 이미지 생성 년,월 return
    :param image(str)
    :return img_date(list)
    '''
    img = Image.open(image)
    img_date = []

    if DEBUG : print(img.filename)

    # exif 정보로 이미지 촬영일 체크
    img_info = img.getexif()
    if img_info is not None:                        # exif 존재하면
        for tag_id in img_info:                     # exif TAG 정보에서 촬영일 체크
            tag = TAGS.get(tag_id, tag_id)
            data = img_info.get(tag_id)
            if tag == 'DateTime':                   # 촬영일 존재하면 년,월 세팅
                data = data.replace('-',':')         # '-' 일자 구분자를 :로 변환
                data = data.split()[0]              # data = 년:월:일
                date = data.split(':')  # date = [년, 월, 일]
                try:
                    img_date.append(date[0])
                    img_date.append(date[1])
                except:
                    print('!!!!!! ERRROR !!!!!!!!!')
                    print(f'img name : ', image)
                    print(f'data : {data}')
                    print(f'date : {date}')
                    img_date[0] = 'error'           # 강제 error 세팅
                    img_date.append('00')           # 두번째 값 '00' 추가
                    print(f'img_date : {img_date}')
            if DEBUG:
                print(f'{tag:25}: {data}')

    # EXIF 값이 없으면, 파일 생성일 세팅
    if len(img_date) == 0 :
        date = datetime.fromtimestamp(os.path.getctime(image)).strftime('%Y:%m:%d').split(':')
        img_date.append(date[0])
        img_date.append(date[1])

    if(DEBUG):
        print(f'date : {date}')
        print(f'img_date : {img_date}')
    return img_date

def moveImageFiles(img_list, DEBUG=False):
    count =0
    for img in img_list:
        img_date = getImageDate(img)
        if DEBUG : print(img_date[0], img_date[1], img)

        dir_path = os.path.join(cur_dir, img_date[0], img_date[1])
        s_path = os.path.join(cur_dir, img)
        t_path = os.path.join(dir_path, img)
        if DEBUG:
            print(f'dir_path : {dir_path}')
            print(f'Source_path : {s_path}')
            print(f'Target_path : {t_path}')

        # 이미지 년\월 디렉토리 존재하면, 파일을 이동하고 없으면 생성 후 이동
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        shutil.move(s_path, t_path)
        count = count+1

    print(f'{count} files moved!')

'''
현제 디렉토리의 이미지,비디오,기타 파일 목록 확인
'''
for file in os.listdir(cur_dir):
    if os.path.isfile(file):
        name,ext = os.path.splitext(file)
        if ext in img_ext:
            img_list.append(file)
        elif ext in video_ext:
            video_list.append(file)
        else:
            etc_list.append(file)
    else:
        print(f'[{file}] is not File')

if DEBUG:
    print(f'img_list : {img_list}')
    print(f'video_list : {video_list}')
    print(f'etc_list : {etc_list}')

moveImageFiles(img_list)