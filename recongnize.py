import easyocr
import cv2
import argparse
import re

def loadModel():
    """
    Load OCR model to memory.
    Needs to run only once before use recongnize() function.
    """
    return easyocr.Reader(['en'], gpu = True)

def recongnize(reader, img_path):
    img = cv2.imread(img_path)
    result = []
    predict1 = reader.readtext(img, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ') # 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ID_eng = str(predict1[0][1])

    predict2 = reader.readtext(img, allowlist='0123456789') # 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ID_num = str(predict2[1][1])
    ID_num = ID_num.replace(" ", "") # remove space
    ID = ID_eng + ID_num
    score = predict2[2][1]
    result.append(ID)
    result.append(score)

    return result

def main():
    parser = argparse.ArgumentParser(description='Text OCR. Return string.')
    parser.add_argument('--img_path', required=True, help='image path to recongnize')
    opt = parser.parse_args()
    img_path = opt.img_path

    reader = loadModel()
    result = recongnize(reader, img_path)
    print(result)
    
if __name__ == '__main__':
    main()