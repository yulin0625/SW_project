import easyocr
import cv2
import argparse

# img_path = "score.jpg"



def main():
    parser = argparse.ArgumentParser(description='text OCR.')
    parser.add_argument('--img_path', required=True, help='image path to recongnize')
    opt = parser.parse_args()
    img_path = opt.img_path
    img = cv2.imread(img_path)

    reader = easyocr.Reader(['en'], gpu = True) # this needs to run only once to load the model into memory
    result = reader.readtext(img)

    for i in range(len(result)):
            print(result[i])

    for i in result:
        cv2.rectangle(img, (int(i[0][0][0]), int(i[0][0][1])), (int(i[0][2][0]), int(i[0][2][1])), (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(img, i[1], (int(i[0][0][0]), int(i[0][0][1]) - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

    # cv2.imwrite(img_path.split(".")[0] + "_label." + img_path.split(".")[1], img)  # save result image
    cv2.imshow("result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()