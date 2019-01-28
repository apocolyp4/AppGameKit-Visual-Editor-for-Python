import appgamekit as agk
from VisualEditor_properties import *

def find_image(self, s_image):
    for image in self.images:
        if image.sImage == s_image:
            return True

    newImage = Image()
    newImage.sImage = s_image

    self.images.append(newImage)

    return False

def load_image(self, s_image):
    # look for the image in the list
    # if it has no ID then it needs to be loaded
    # if it has already been loaded it will have an ID so return that
    for image in self.images:
        if image.sImage == s_image:
            if image.id == -1:
                image.id = agk.load_image(s_image)

            return image.id
    return -1
