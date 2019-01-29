import appgamekit as agk
from VisualEditor_properties import Resolution, Image


def get_id(self, entity_name, scene_id):
    if scene_id < 0 or scene_id > len(self.scenes) - 1:
        agk.message("The scene index passed into get_entity_id is out of bounds. This scene does not exist.")
        return -1

    for scene_entity in self.scenes[scene_id].entities:
        entity = self.entities[scene_entity.index]
        if entity.name == entity_name:
            return scene_entity.id

    agk.message("The entity " + entity_name + " does not exist. Please note the scene index begins at 0.")
    return -1


def get_kind(self, entity_name, scene_id):
    if scene_id < 0 or scene_id > len(self.scenes) - 1:
        agk.message("The scene index passed into get_entity_kind is out of bounds. This scene does not exist.")
        return "NULL"

    for scene_entity in self.scenes[scene_id].entities:
        entity = self.entities[scene_entity.index]
        if entity.name == entity_name:
            return scene_entity.kind

    agk.message("The entity " + entity_name + " does not exist. Please note the scene index begins at 0.")
    return "NULL"

def add_resolution(self, width, height):
    new_resolution = Resolution()
    new_resolution.width = width
    new_resolution.height = height
    self.resolutions.append(new_resolution)

def update_custom_resolutions(self):
    resize_list(self.resolutions, len(self.resolutions) - 1, Resolution())

    if len(self.custom_resolutions) == 0:
        return

    count = agk.count_string_tokens(self.custom_resolutions, " ")

    if count % 2 == 0:
        index = 1
        halfCount = int(count / 2)
        for i in range(halfCount):
            width = agk.get_string_token(self.custom_resolutions, " ", index + 0)
            height = agk.get_string_token(self.custom_resolutions, " ", index + 1)
            index = index + 2
            add_resolution(self, int(width), int(height))

    resize_list(self.Resolutions, len(self.Resolutions) - 1, Resolution())


def find_closest_resolution(self):

    deviceWidth = self.base_width
    deviceHeight = self.base_height

    closestWidth = 0
    closestHeight = 0

    if agk.get_device_base_name().lower() != "windows":
        deviceWidth = agk.get_device_width()
        deviceHeight = agk.get_device_height()

    for i in range(len(self.resolutions)):
        set = 0
        if self.resolutions[i].width <= deviceWidth and self.resolutions[i].height <= deviceHeight:
            set = 1

        if set == 1 and self.resolutions[i].width >= closestWidth and self.resolutions[i].height >= closestHeight:
            closestWidth = self.resolutions[i].width
            closestHeight = self. resolutions[i].height

    if closestWidth == 0 or closestHeight == 0:
        closestWidth = agk.get_device_width()
        closestHeight = agk.get_device_height()

    self.width = closestWidth
    self.height = closestHeight


def get_new_resolution(self, newWidth, newHeight):
    self.original_width = self.base_width
    self.original_height = self.base_height

    self.target_width = 0.0
    self.target_height = 0.0

    width = self.original_width
    height = self.original_height

    size = newWidth / self.original_width
    size_x = width * size
    size_y = height * size

    if size_y > newHeight:
        size = newHeight / self.original_height
        size_x = width * size
        size_y = height * size

    self.target_width = size_x
    self.target_height = size_y

    canvasX = newWidth
    canvasY = newHeight

    aspect = newHeight / self.target_width
    size_y = canvasY / aspect
    height = size_y
    offset = (canvasX - size_y) / 2.0
    pixelSize = height / self.target_width
    totalHeightInPixels = canvasX / pixelSize
    self.border_in_pixels = offset / pixelSize

    aspect = newWidth / self.target_height
    size_y = canvasX / aspect
    height = size_y
    offset = (canvasY - size_y) / 2.0
    pixelSize = height / self.target_height
    totalHeightInPixels = canvasY / pixelSize
    self.border_in_pixels_y = offset / pixelSize


def update_for_different_resolution(self, entity, id, kind):
    size = self.target_width / self.original_width

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

        x = agk.get_text_x(id) / self.base_width
        y = agk.get_text_y(id) / self.base_height

        new_pos_x = x * self.target_width
        new_pos_y = y *self. target_height

        agk.set_text_position(id, self.border_in_pixels + new_pos_x, self.border_in_pixels_y + new_pos_y)

    elif kind == self.constants.VISUAL_EDITOR_SPRITE:
        size_x = agk.get_sprite_width(id) * size
        size_y = agk.get_sprite_height(id) * size

        agk.set_sprite_size(id, size_x, size_y)

        x = agk.get_sprite_x(id) / self.base_width
        y = agk.get_sprite_y(id) / self.base_height

        new_pos_x = x * self.target_width
        new_pos_y = y * self.target_height

        agk.set_sprite_position(id, self.border_in_pixels + new_pos_x, self.border_in_pixels_y + new_pos_y)

    elif kind == self.constants.VISUAL_EDITOR_EDIT_BOX:
        size_x = agk.get_edit_box_width(id) * size
        size_y = agk.get_edit_box_height(id) * size

        agk.set_edit_box_size(id, size_x, size_y)
        agk.set_edit_box_text_size(id, size_y - 2)

        x = agk.get_edit_box_X(id) / self.base_width
        y = agk.get_edit_box_Y(id) / self.base_height

        new_pos_x = x * self.target_width
        new_pos_y = y * self.target_height

        agk.set_edit_box_position(id, self.border_in_pixels + new_pos_x, self.border_in_pixels_y + new_pos_y)

    elif kind == self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON:
        size_x = entity.size_x * size
        size_y = entity.size_y * size

        agk.set_virtual_button_size(id, size_x, size_y)

        x = entity.x / self.base_width
        y = entity.y / self.base_height

        new_pos_x = x * self.target_width
        new_pos_y = y * self.target_height

        off_set_x = size_x / 2.0
        off_set_y = size_y / 2.0

        agk.set_virtual_button_position(id, self.border_in_pixels + new_pos_x + off_set_x, self.border_in_pixels_y + new_pos_y + off_set_y)

    elif kind == self.constants.VISUAL_EDITOR_PARTICLES:
        size_x = entity.particle_size * size

        agk.set_particles_size(id, size_x)

        x = entity.x / self.base_width
        y = entity.y / self.base_height

        new_pos_x = x * self.target_width
        new_pos_y = y * self.target_height

        agk.set_particles_position(id, self.border_in_pixels + new_pos_x, self.border_in_pixels_y + new_pos_y)


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

    for animation_set in enity.animation_set:
        animation_set.start_frame = frame
        animation_set.end_frame = frame + len(animation_set.frames)
        frame = frame + len(animation_set.frames)

        for animation_set.frame in animation_set.frames:
            # check for subimage and load from that instead
            if len(enity.sub_image) > 0:
                image = load_sub_image(self, enity.image, animation_set.frame.image)
            else:
                image = agk.load_image(enity.image)

            agk.add_sprite_animation_frame(id, image)

        if count == 1:
            agk.set_sprite_active(id, 1)

            start_frame = animation_set.start_frame
            end_frame = animation_set.end_frame

            agk.play_sprite(id, animation_set.speed, animation_set.loop_mode, start_frame, end_frame)

            count += 1


def load_sub_image(self, new_image, sub_image):
    # look for the image in the list
    # if it has no ID then it needs to be loaded
    # if it has already been loaded it will have an ID so return that

    i_main_image = 0

    for image in self.images:
        if image.sImage == new_image:
            if image.id == -1:
                image.id = agk.load_image(new_image)

            i_main_image = image.id
            break

    # need to switch to sharing all images
    self.VisualEditor_SubImages.append(Image())

    self.sub_images[-1].image = sub_image
    self.sub_images[-1].id = agk.load_sub_image(i_main_image, sub_image)

    return self.sub_images[-1].id