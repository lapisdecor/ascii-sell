import qrcode_terminal
import sys

text = sys.argv[1]

qrcode_terminal.draw(text)
