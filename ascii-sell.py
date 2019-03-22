import sys
from PIL import Image
import numpy as np

white_block = '\033[0;37;47m  '
black_block = '\033[0;37;40m  '
new_line = '\033[0m\n'
                                                                              
#chars = np.concatenate(([white_block], np.asarray(list('.,:;irsXA253hMHGS#9B&')), [black_block]))
chars = np.concatenate(([white_block], np.asarray(list([black_block]*21)), [black_block]))

f, SC, GCF, WCF = "tmp.png", float(0.40), float(10), 1

img = Image.open(f)
S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
img = np.sum( np.asarray( img.resize(S) ), axis=2)
img -= img.min()
img = (1.0 - img/img.max())**GCF*(chars.size-1)

print( new_line.join( ("".join(r) for r in chars[img.astype(int)]) ) )
print( new_line )
