import pyqrcode
import png

from pyqrcode import QRCode

QrString = 'https://www.instagram.com/therealslimmad/'

url = pyqrcode.create(QrString)

url.png(r'qr.png', scale=8)