import cv2

def load_image(path): # This feels like an overkill.
    """ Load an image from a path using opencv"""
    return cv2.imread(path)

def show_image(image):
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

# quick test
path = r"images\scottish-cliffs-3840x2160.jpg"
image = load_image(path)

show_image(image)