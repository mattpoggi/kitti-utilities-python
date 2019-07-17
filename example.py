from utils import kitti_colormap, read_16bit_gt
import cv2

src = read_16bit_gt('sample/000000_10.png')
colored = kitti_colormap(src)
cv2.imwrite('sample/000000_10_color.png', colored)
