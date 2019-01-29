import appgamekit as agk
from VisualEditor_properties import *


def find_image(self, s_image):
    for image in self.images:
        if image.image == s_image:
            return True

    new_image = Image()
    new_image.image = s_image

    self.images.append(new_image)

    return False

def load_image(self, s_image):
    # look for the image in the list
    # if it has no ID then it needs to be loaded
    # if it has already been loaded it will have an ID so return that

    for image in self.images:
        if image.image == s_image:
            if image.id == -1:
                image.id = agk.load_image(s_image)

            return image.id
    return -1
