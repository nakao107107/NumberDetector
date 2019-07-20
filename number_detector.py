#coding: utf-8

import cv2
import numpy as np

class NumberDetector:

    def __init__(self, path):
        self.src_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        
    def detect(self, image_create= False):

        num_coord = []

        height, width = self.src_img.shape[:2]

        
        for i in range(width - 29):

            for j in range(height - 29):

                #画像から28×28pixcel分の領域を抜き出す
                detect_area = self.src_img[j:j+28, i:i+28]

                #抜き出した範囲が全て0なら、そこに数字はないのでcontinue
                if not (np.any(detect_area)):
                    continue
                
                #要素をスライシング
                detect_area_top = detect_area[0:2,0:28].flatten()
                detect_area_botton = detect_area[26:28,0:28].flatten()
                detect_area_left = detect_area[0:28,0:2].flatten()
                detect_area_right = detect_area[0:28,26:28].flatten()

                #足し合わせを周辺行列として定義
                detect_area_surround = np.concatenate([detect_area_top, detect_area_botton, detect_area_left, detect_area_right])

                #周辺行列に0以外の数字が含まれる（探索領域の周辺2pxに0以外数字が含まれる）場合、
                #数字の領域を部分的に抜き出しているとみなしcontinue

                if (np.any(detect_area_surround)):
                    continue
                
                num_coord.append((j, i))
        
        print("detect completed!")

        #step3(test) 抽出した座標に対して四角形を描画　ちゃんと抽出できているかを確認(画像出力洗濯時のみ)
        
        if (image_create):
            for height, width in num_coord:
                cv2.rectangle(self.src_img, (width, height), (width+28, height+28), (255, 255, 0))
            cv2.imwrite("detect_num_img.png",self.src_img)
        return num_coord


