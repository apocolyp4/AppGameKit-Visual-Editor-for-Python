import appgamekit as agk
from VisualEditor_properties import Resolution, Image


def get_id(self, entity_name, scene_id):
    if scene_id < 0 or scene_id > len(self.scenes) - 1:
        agk.message("The scene index passed into get_entity_id is out of bounds. This scene does not exist.")
        return -1

    for scene_entity in self.scenes[scene_id].entities:
        entity = self.VisualEditor_Entities[scene_entity.index]
        if entity.sName == entity_name:
            return scene_entity.id

    agk.message("The entity " + entity_name + " does not exist. Please note the scene index begins at 0.")
    return -1


def get_kind(self, entity_name, scene_id):
    if scene_id < 0 or scene_id > len(self.scenes) - 1:
        agk.message("The scene index passed into get_entity_kind is out of bounds. This scene does not exist.")
        return "NULL"

    for scene_entity in self.scenes[scene_id].entities:
        entity = self.VisualEditor_Entities[scene_entity.index]
        if entity.sName == entity_name:
            return scene_entity.kind

    agk.message("The entity " + entity_name + " does not exist. Please note the scene index begins at 0.")
    return "NULL"

def add_resolution(self, width, height):
    new_resolution = Resolution()
    new_resolution.width = width
    new_resolution.height = height
    self.VisualEditor_Resolutions.append(new_resolution)

def update_custom_resolutions(self):
    resize_list(self.VisualEditor_Resolutions, len(self.VisualEditor_Resolutions) - 1, Resolution())

    if len(self.VisualEditor_CustomResolutions) == 0:
        return

    count = agk.count_string_tokens(self.VisualEditor_CustomResolutions, " ")

    if count % 2 == 0:
        index = 1
        halfCount = int(count / 2)
        for i in range(halfCount):
            width = agk.get_string_token(self.VisualEditor_CustomResolutions, " ", index + 0)
            height = agk.get_string_token(self.VisualEditor_CustomResolutions, " ", index + 1)
            index = index + 2
            add_resolution(self, int(width), int(height))

    resize_list(self.Resolutions, len(self.Resolutions) - 1, Resolution())


def find_closest_resolution(self):

    deviceWidth = self.VisualEditor_BaseWidth
    deviceHeight = self.VisualEditor_BaseHeight

    closestWidth = 0
    closestHeight = 0

    if agk.get_device_base_name().lower() != "windows":
        deviceWidth = agk.get_device_width()
        deviceHeight = agk.get_device_height()

    for i in range(len(self.VisualEditor_Resolutions)):
        set = 0
        if self.VisualEditor_Resolutions[i].width <= deviceWidth and self.VisualEditor_Resolutions[i].height <= deviceHeight:
            set = 1

        if set == 1 and self.VisualEditor_Resolutions[i].width >= closestWidth and self.VisualEditor_Resolutions[i].height >= closestHeight:
            closestWidth = self.VisualEditor_Resolutions[i].width
            closestHeight = self. VisualEditor_Resolutions[i].height

    if closestWidth == 0 or closestHeight == 0:
        closestWidth = agk.get_device_width()
        closestHeight = agk.get_device_height()

    self.VisualEditor_Width = closestWidth
    self.VisualEditor_Height = closestHeight


def get_new_resolution(self, newWidth, newHeight):
    self.VisualEditor_OriginalWidth = self.VisualEditor_BaseWidth
    self.VisualEditor_OriginalHeight = self.VisualEditor_BaseHeight

    self.VisualEditor_TargetWidth = 0.0
    self.VisualEditor_TargetHeight = 0.0

    width = self.VisualEditor_OriginalWidth
    height = self.VisualEditor_OriginalHeight

    size = newWidth / self.VisualEditor_OriginalWidth
    sizeX = width * size
    sizeY = height * size

    if sizeY > newHeight:
        size = newHeight / self.VisualEditor_OriginalHeight
        sizeX = width * size
        sizeY = height * size

    self.VisualEditor_TargetWidth = sizeX
    self.VisualEditor_TargetHeight = sizeY

    canvasX = newWidth
    canvasY = newHeight

    aspect = newHeight / self.VisualEditor_TargetWidth
    sizeY = canvasY / aspect
    height = sizeY
    offset = (canvasX - sizeY) / 2.0
    pixelSize = height / self.VisualEditor_TargetWidth
    totalHeightInPixels = canvasX / pixelSize
    self.VisualEditor_BorderInPixels = offset / pixelSize

    aspect = newWidth / self.VisualEditor_TargetHeight
    sizeY = canvasX / aspect
    height = sizeY
    offset = (canvasY - sizeY) / 2.0
    pixelSize = height / self.VisualEditor_TargetHeight
    totalHeightInPixels = canvasY / pixelSize
    self.VisualEditor_BorderInPixelsY = offset / pixelSize


def VisualEditor_UpdateForDifferentResolution(self, entity, id, kind):
    size = self.VisualEditor_TargetWidth / self.VisualEditor_OriginalWidth

    if kind == self.constants.VISUAL_EDITOR_TEXT:
        size_x = agk.get_text_total_width(id) * size
        current_size = 0.1

        agk.set_text_size(id, current_size)

        while 1:
            width = agk.get_text_total_width(id)
            agk.set_text_size(id, current_size)

            if width < size_x:
                current_size += 0.1
            else:
                break

        x = agk.get_text_x(id) / self.VisualEditor_BaseWidth
        y = agk.get_text_y(id) / self.VisualEditor_BaseHeight

        new_pos_x = x * self.VisualEditor_TargetWidth
        new_pos_y = y *self. VisualEditor_TargetHeight

        agk.set_text_position(id, self.VisualEditor_BorderInPixels + new_pos_x, self.VisualEditor_BorderInPixelsY + new_pos_y)

    elif kind == self.constants.VISUAL_EDITOR_SPRITE:
        size_x = agk.get_sprite_width(id) * size
        size_y = agk.get_sprite_height(id) * size

        agk.set_sprite_size(id, size_x, size_y)

        x = agk.get_sprite_x(id) / self.VisualEditor_BaseWidth
        y = agk.get_sprite_y(id) / self.VisualEditor_BaseHeight

        new_pos_x = x * self.VisualEditor_TargetWidth
        new_pos_y = y * self.VisualEditor_TargetHeight

        agk.set_sprite_position(id, self.VisualEditor_BorderInPixels + new_pos_x, self.VisualEditor_BorderInPixelsY + new_pos_y)

    elif kind == self.constants.VISUAL_EDITOR_EDIT_BOX:
        size_x = agk.get_edit_box_width(id) * size
        size_y = agk.get_edit_box_height(id) * size

        agk.set_edit_box_size(id, size_x, size_y)
        agk.set_edit_box_text_size(id, size_y - 2)

        x = agk.get_edit_box_X(id) / self.VisualEditor_BaseWidth
        y = agk.get_edit_box_Y(id) / self.VisualEditor_BaseHeight

        new_pos_x = x * self.VisualEditor_TargetWidth
        new_pos_y = y * self.VisualEditor_TargetHeight

        agk.set_edit_box_position(id, self.VisualEditor_BorderInPixels + new_pos_x, self.VisualEditor_BorderInPixelsY + new_pos_y)

    elif kind == self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON:
        size_x = entity.sizeX * size
        size_y = entity.sizeY * size

        agk.set_virtual_button_size(id, size_x, size_y)

        x = entity.x / self.VisualEditor_BaseWidth
        y = entity.y / self.VisualEditor_BaseHeight

        new_pos_x = x * self.VisualEditor_TargetWidth
        new_pos_y = y * self.VisualEditor_TargetHeight

        off_set_x = size_x / 2.0
        off_set_y = size_y / 2.0

        agk.set_virtual_button_position(id, self.VisualEditor_BorderInPixels + new_pos_x + off_set_x, self.VisualEditor_BorderInPixelsY + new_pos_y + off_set_y)

    elif kind == self.constants.VISUAL_EDITOR_PARTICLES:
        size_x = entity.particleSize * size

        agk.set_particles_size(id, size_x)

        x = entity.x / self.VisualEditor_BaseWidth
        y = entity.y / self.VisualEditor_BaseHeight

        new_pos_x = x * self.VisualEditor_TargetWidth
        new_pos_y = y * self.VisualEditor_TargetHeight

        agk.set_particles_position(id, self.VisualEditor_BorderInPixels + new_pos_x, self.VisualEditor_BorderInPixelsY + new_pos_y)


def resize_list(list, new_size, list_type):
    if new_size < len(list):
        list = list[:new_size]
    elif new_size > len(list):
        for i in range(new_size - len(list)):
            list.append(list_type)

    return list


def setup_animation(self, enity, id):
    # load all the frames of animation, play  the default anim
    agk.clear_sprite_animation_frames(id)

    frame = 1
    count = 1

    for animation_set in enity.animationSet:
        animation_set.startFrame = frame
        animation_set.endFrame = frame + len(animation_set.frames)
        frame = frame + len(animation_set.frames)

        for animation_set.frame in animation_set.frames:
            # check for subimage and load from that instead
            if len(enity.sSubImage) > 0:
                image = load_sub_image(self, enity.sImage, animation_set.frame.sImage)
            else:
                image = agk.load_image(enity.sImage)

            agk.add_sprite_animation_frame(id, image)

        if count == 1:
            agk.set_sprite_active(id, 1)

            start_frame = animation_set.startFrame
            end_frame = animation_set.endFrame

            agk.play_sprite(id, animation_set.speed, animation_set.loopMode, start_frame, end_frame)

            count += 1


def load_sub_image(self, s_image, sub_image):
    # look for the image in the list
    # if it has no ID then it needs to be loaded
    # if it has already been loaded it will have an ID so return that

    i_main_image = 0

    for image in self.VisualEditor_Images:
        if image.sImage == s_image:
            if image.id == -1:
                image.id = agk.load_image(s_image)

            i_main_image = self.VisualEditor_Images[i].id
            break


    # need to switch to sharing all images
    self.VisualEditor_SubImages.append(Image())

    self.VisualEditor_SubImages[-1].sImage = sub_image
    self.VisualEditor_SubImages[-1].id = agk.load_sub_image(i_main_image, sub_image)

    return self.VisualEditor_SubImages[-1].id