import appgamekit as agk
from VisualEditor_properties import *
from VisualEditor_Scene_Entities import *
from VisualEditor_utilities import resize_list

def setup_scenes(self):
    # go through all the entities and assign them to scenes
    count = 0

    for entity in self.VisualEditor_Entities:
        scene = entity.scene

        if scene > len(self.scenes) - 1:
            self.scenes.append(Scene())

        index = len(self.scenes[scene].entities) - 1

        if entity.sType == "sprite":
            self.scenes[scene].entities[index].kind = self.constants.VISUAL_EDITOR_SPRITE
        elif entity.sType == "text":
            self.scenes[scene].entities[index].kind = self.constants.VISUAL_EDITOR_TEXT
        elif entity.sType == "editbox":
            self.scenes[scene].entities[index].kind = self.constants.VISUAL_EDITOR_EDIT_BOX
        elif entity.sType == "button":
            self.scenes[scene].entities[index].kind = self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON
        elif entity.sType == "particles":
            self.scenes[scene].entities[index].kind = self.constants.VISUAL_EDITOR_PARTICLES

        # store the index into the main entities array so we can access it later
        self.scenes[scene].entities[index].index = count
        self.scenes[scene].entities.append(SceneEntity())

        count += 1

    for i in range(1, len(self.scenes)):
        self.scenes[i].clear_colour_red = 255
        self.scenes[i].clear_colour_green = 255
        self.scenes[i].clear_colour_blue = 255

    count = agk.count_string_tokens(self.VisualEditor_SceneColours, " ")

    if count % 3 == 0:
        index = 1
        scene = 0
        for i in range(0, int(count / 3)):
            self.scenes[scene].clear_colour_red = int(agk.get_string_token(self.VisualEditor_SceneColours, " ", index + 0))
            self.scenes[scene].clear_colour_green = int(agk.get_string_token(self.VisualEditor_SceneColours, " ", index + 1))
            self.scenes[scene].clear_colour_blue = int(agk.get_string_token(self.VisualEditor_SceneColours, " ", index + 2))
            index = index + 3
            scene = scene + 1

    # sort out any dynamic resolution information here
    for entity in self.VisualEditor_Entities:
        count = agk.count_string_tokens(entity.dynamicRes, " ")

        # stick this into an array for each entity
        # if this array length is greater than 0 then we look through it
        # width, height, x, y, size x, size y
        if count % 6 == 0:
            index = 1
            for j in range(1, int(count / 6)):
                entity.overrides.append(Override())

                array_pos = len(entity.overrides) - 1
                entity.overrides[array_pos].width = int(agk.get_string_token(entity.dynamicRes, " ", index + 0))
                entity.overrides[array_pos].height = int(agk.get_string_token(entity.dynamicRes, " ", index + 1))
                entity.overrides[array_pos].x = int(agk.get_string_token(entity.dynamicRes, " ", index + 2))
                entity.overrides[array_pos].y = int(agk.get_string_token(entity.dynamicRes, " ", index + 3))
                entity.overrides[array_pos].sizeX = int(agk.get_string_token(entity.dynamicRes, " ", index + 4))
                entity.overrides[array_pos].sizeY = int(agk.get_string_token(entity.dynamicRes, " ", index + 5))
                index = index + 6

    # run through all the entities and add their images to the image list
    for entity in self.VisualEditor_Entities:
        find_image(self, entity.sImage)
        find_font(self, entity.sFont)

    if len(self.images) > 0:
        new_length = len(self.images)
        self.images = resize_list(self.images, new_length, Image())

    self.manager.currentScene = 0
    set_scene(self, 0)


def set_scene(self, scene_id):
    # find active scene, delete its contents, then load everything for the selected scene
    if scene_id < 0 or scene_id > len(self.scenes) - 1:
        agk.message("The scene index passed into VisualEditor_SetScenes is out of bounds. This scene does not exist.")
        return

    delete_scene(self)

    self.manager.currentScene = scene_id
    agk.set_clear_color(self.scenes[scene_id].clear_colour_red, self.scenes[scene_id].clear_colour_green, self.scenes[scene_id].clear_colour_blue)

    for scene_entity in self.scenes[scene_id].entities:

        entity = self.VisualEditor_Entities[scene_entity.index]
        self.overrideIndex = 0

        for j in range(0, len(entity.overrides)):
            if self.VisualEditor_Width == entity.overrides[j].width and self.VisualEditor_Height == entity.overrides[j].height:
                self.overrideIndex = j
                break

        kind = scene_entity.kind

        if kind == self.constants.VISUAL_EDITOR_SPRITE:
            set_scene_sprite(self, scene_entity)

        elif kind == self.constants.VISUAL_EDITOR_TEXT:
            set_scene_text(self, scene_entity)

        elif kind == self.constants.VISUAL_EDITOR_EDIT_BOX:
            set_scene_text_box(self, scene_entity)

        elif kind == self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON:
            set_scene_virtual_button(self, scene_entity)

        elif kind == self.constants.VISUAL_EDITOR_PARTICLES:
            set_scene_virtual_particles(self, scene_entity)


def find_font(self, s_font):

    if s_font == "":
        return 0

    for i in range(0, len(self.fonts)):
        if self.VisualEditor_Fonts.sFile == s_font:
            return 1

    new_font = self.font()
    new_font.sImage = s_font
    new_font.ID = -1

    self.VisualEditor_Fonts.append(new_font)

    return 0


def delete_scene(self):
    scene = self.manager.currentScene

    for entity in self.scenes[scene].entities:

        kind = entity.kind

        if kind == self.constants.VISUAL_EDITOR_SPRITE:
            if self.load_all_media == 0:
                agk.delete_sprite(entity.id)
            else:
                agk.set_sprite_visible(entity.id, 0)

        elif kind == self.constants.VISUAL_EDITOR_TEXT:
            if self.load_all_media == 0:
                agk.delete_text(entity.id)
            else:
                agk.set_text_visible(entity.id, 0)

        elif kind == self.constants.VISUAL_EDITOR_EDIT_BOX:
            if self.load_all_media == 0:
                agk.delete_edit_box(entity.id)
            else:
                agk.set_edit_box_visible(entity.id, 0)

        elif kind == self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON:
            if self.load_all_media == 0:
                agk.delete_virtual_button(entity.id  + 1)
            else:
                agk.set_virtual_button_visible(entity.id + 1, 0)

        elif kind == self.constants.VISUAL_EDITOR_PARTICLES:
            if self.load_all_media == 0:
                agk.delete_particles(entity.id)
            else:
                agk.set_particles_visible(entity.id, 0)

    if self.load_all_media == 0:
        for image in self.images:
            if image.id == -1:
                agk.delete_image(image.id)
                image.id = -1

        for sub_image in self.VisualEditor_SubImages:
            if sub_image.id == -1:
                agk.delete_image(sub_image.id)
                sub_image.id = -1
