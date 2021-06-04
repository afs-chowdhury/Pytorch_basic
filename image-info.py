import cv2
 
# read image

class Image_info():
    def __init__(self, path):
        
        self.path = path
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        # get dimensions of image
        dimensions = img.shape

        # height, width, number of channels in image
        height = img.shape[0]
        width = img.shape[1]
        channels = img.shape[2]

        print('Image Dimension    : ',dimensions)
        print('Image Height       : ',height)
        print('Image Width        : ',width)
        print('Number of Channels : ',channels)