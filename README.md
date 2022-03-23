# SW_project

## create conda env
conda create --name sw python=3.8

## activate conda env
conda activate sw

## install EasyOCR
pip install git+git://github.com/jaidedai/easyocr.git

## install requirements
pip install -r requirements.txt

## usage
### demo.py
python demo.py --img_path score.jpg

### recongnize.py
python recongnize.py --img_path score.jpg