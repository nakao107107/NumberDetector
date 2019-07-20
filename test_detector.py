#coding: utf-8

from number_detector import NumberDetector

number_detector = NumberDetector('search_image.png')
num_coord = number_detector.detect()
print(num_coord)

#結果を画像として出力させたい場合、以下
#num_coord = number_detector.detect(True)
