import appgamekit as agk
from VisualEditor_properties import *
from VisualEditor_utilities import resize_list


class FileData:
    tag = ""
    value = ""


def load_project(self, file_name):
    # load a project
    if agk.get_file_exists(file_name) == 0:
        agk.message("Error - project file cannot be opened")

    file = agk.open_to_read(file_name)

    counter = 0

    while agk.file_eof(file) == 0:
        line = agk.read_line(file)
        line = agk.replace_string(line, "</>", "", -1)
        line = agk.get_string_token2(line, "<", 2)

        data = FileData()
        data.tag = agk.get_string_token2(line, ">", 1)
        data.value = agk.get_string_token2(line, ">", 2)
        self.project_data.append(data)

    agk.close_file(file)

    file = agk.open_to_write("entity.txt")
    for data in self.project_data:
        agk.write_line(file, data.tag + " : " + data.value)
    agk.close_file(file)
    
    # parse project data
    self.entities = []
    data_type = "settings"
    for data in self.project_data:
        if data.tag == "settings":
            data_type = "settings"

        elif data.tag == "/settings":
            data_type = ""

        if data.tag == "entity":
            data_type = "entity"
            self.entities.append(FileEntity())

        elif data.tag == "/entity":
            data_type = ""

        elif data_type == "settings":
            parse_settings_data(self, data)

        elif data_type == "entity":
            parse_entity_data(self, self.entities[-1], data)




def parse_entity_data(self, entity, data):
    # we have found an entity, look through all supported data, if we find
    # a then store the data in the entities array

    # need to split this into different kinds of entities so we can parse
    # edit  boxes, text, virtual buttons etc.individually

    # this will change in the future - another approach is needed for it

    tags = ["collision", "type", "name", "scene", "image", "subimage", "animplay", "animset", "animspeed",
                "animloop", "animframe",
                "x", "y", "size x", "size y", "scale x", "custom",
                "scale y", "offset x", "offset y", "angle", "depth", "visible", "red", "green", "blue", "alpha", "text",
                "text size", "alignment",
                "active", "physics", "fliph", "flipv", "alignment", "dynamic res", "font", "fixed",
                "edit size", "edit colour red", "edit colour green", "edit colour blue",
                "edit background red", "edit background green", "edit background blue", "edit background alpha",
                "edit border red", "edit border green", "edit border blue", "edit border alpha", "edit border size",
                "edit max characters", "edit max lines", "edit multi line", "edit password", "edit cursor red",
                "edit cursor green", "edit cursor blue", "edit cursor width", "edit cursor wrap",
                "button down", "button up", "button text", "button goto",
                "particle image", "particle size", "particle life", "particle max", "particle frequency",
                "particle emit angle",
                "particle face dir", "particle transparency", "particle dir x", "particle dir y", "particle rot x",
                "particle rot y",
                "particle x1", "particle y1", "particle x2", "particle y2", "particle vel x", "particle vel y",
                "particle colours",
                "particle scales", "particle forces",
                "angulardamping", "centreofmassx", "centreofmassy", "canrotate", "damping", "friction", "isbullet",
                "issensor", "mass", "restitution"]

    for tag in tags:
        if data.tag == tag:
            if data.tag == "type":
                entity.type = data.value
            elif data.tag == "name":
                entity.name = data.value
            elif data.tag == "font":
                entity.s_font = data.value
            elif data.tag == "scene":
                entity.scene = int(data.value)
            elif data.tag == "visible":
                entity.visible = int(data.value)
            elif data.tag == "fliph":
                entity.flip_h = int(data.value)
            elif data.tag == "flipv":
                entity.flip_v = int(data.value)
            elif data.tag == "x":
                entity.x = int(float(data.value))
            elif data.tag == "y":
                entity.y = int(float(data.value))
            elif data.tag == "custom":
                new_size = len(entity.custom) + 1
                entity.custom = resize_list(entity.custom, new_size, "")
                entity.custom[len(entity.custom) - 1] = data.value
            elif data.tag == "animplay":
                entity.anim_play = int(float(data.value))
            elif data.tag == "animset":
                new_size = len(entity.animation_set) + 1
                entity.animation_set = resize_list(entity.animation_set, new_size, "")
                entity.animation_set.animation_set[len(entity.animation_set) - 1].name = data.value
            elif data.tag == "animspeed":
                entity.animation_set[len(entity.animation_set) - 1].speed = int(float(data.value))
            elif data.tag == "animloop":
                entity.animation_set[len(entity.animation_set) - 1].loop_mode = int(float(data.value))
            elif data.tag == "animframe":
                i = len(entity.animation_set)
                new_size = len(entity.animation_set[i].frames) + 1
                entity.animation_set[i].frames = resize_list(entity.animation_set[i].frames, new_size, AnimationFrame())
                j = len(entity.animation_set[i].frames)
                entity.animation_set[i].frames[j].image = data.value
            elif data.tag == "image":
                entity.image = agk.replace_string(data.value, "media/", "", 1)
            elif data.tag == "subimage":
                entity.sub_image = data.value
            elif data.tag == "size x":
                entity.size_x = int(float(data.value))
            elif data.tag == "size y":
                entity.size_y = int(float(data.value))
            elif data.tag == "scale x":
                entity.scale_x = int(float(data.value))
            elif data.tag == "scale y":
                entity.scale_y = int(float(data.value))
            elif data.tag == "offset x":
                entity.offset_x = int(float(data.value))
            elif data.tag == "offset y":
                entity.offset_y = int(float(data.value))
            elif data.tag == "angle":
                entity.angle = int(float(data.value))
            elif data.tag == "fixed":
                entity.fixed = int(float(data.value))
            elif data.tag == "text":
                entity.text = entity.text + data.value + chr(10)
            elif data.tag == "depth":
                entity.depth = int(float(data.value))
            elif data.tag == "red":
                entity.red = int(float(data.value))
            elif data.tag == "green":
                entity.green = int(float(data.value))
            elif data.tag == "blue":
                entity.blue = int(float(data.value))
            elif data.tag == "alpha":
                entity.alpha = int(float(data.value))
            elif data.tag == "alignment":
                entity.alignment = int(float(data.value))
            elif data.tag == "text size":
                entity.text_size = int(float(data.value))
            elif data.tag == "collision":
                entity.collision = int(float(data.value))

                # ve data is polygon, circle, box, no shape
                # agk is no shape, circle, box, polygon
                if entity.collision == 0:
                    entity.collision = 3
                elif entity.collision == 3:
                    entity.collision = 0

            elif data.tag == "active":
                entity.active = int(float(data.value))
            elif data.tag == "physics":
                entity.physics = int(float(data.value))
            elif data.tag == "dynamic res":
                entity.dynamic_res = data.value
            elif data.tag == "edit size":
                entity.edit_size = int(float(data.value))
            elif data.tag == "edit colour red":
                entity.edit_colour_red = int(float(data.value))
            elif data.tag == "edit colour green":
                entity.edit_colour_green = int(float(data.value))
            elif data.tag == "edit colour blue":
                entity.edit_colour_blue = int(float(data.value))
            elif data.tag == "edit background red":
                entity.edit_background_red = int(float(data.value))
            elif data.tag == "edit background green":
                entity.edit_background_green = int(float(data.value))
            elif data.tag == "edit background blue":
                entity.edit_background_blue = int(float(data.value))
            elif data.tag == "edit background alpha":
                entity.edit_background_alpha = int(float(data.value))
            elif data.tag == "edit border red":
                entity.edit_border_red = int(float(data.value))
            elif data.tag == "edit border green":
                entity.edit_border_green = int(float(data.value))
            elif data.tag == "edit border blue":
                entity.edit_border_blue = int(float(data.value))
            elif data.tag == "edit border alpha":
                entity.edit_border_alpha = int(float(data.value))
            elif data.tag == "edit border size":
                entity.edit_border_size = int(float(data.value))
            elif data.tag == "edit max characters":
                entity.edit_max_characters = int(float(data.value))
            elif data.tag == "edit max lines":
                entity.edit_max_lines = int(float(data.value))
            elif data.tag == "edit multi line":
                entity.edit_multi_lines = int(float(data.value))
            elif data.tag == "edit password":
                entity.edit_password = int(float(data.value))
            elif data.tag == "edit cursor red":
                entity.edit_cursor_red = int(float(data.value))
            elif data.tag == "edit cursor green":
                entity.edit_cursor_green = int(float(data.value))
            elif data.tag == "edit cursor blue":
                entity.edit_cursor_blue = int(float(data.value))
            elif data.tag == "edit cursor width":
                entity.edit_cursor_width = int(float(data.value))
            elif data.tag == "edit cursor wrap":
                entity.edit_cursor_wrap = int(float(data.value))
            elif data.tag == "button down":
                entity.button_down = agk.replace_string(data.value, "media/", "", 1)
            elif data.tag == "button up":
                entity.button_up = agk.replace_string(data.value, "media/", "", 1)
            elif data.tag == "button text":
                entity.button_text = data.value
            elif data.tag == "button goto":
                entity.button_goto = int(float(data.value))
            elif data.tag == "particle image":
                entity.particle_image = data.value
            elif data.tag == "particle size":
                entity.particle_size = int(float(data.value))
            elif data.tag == "particle life":
                entity.particle_life = int(float(data.value))
            elif data.tag == "particle max":
                entity.particle_max = int(float(data.value))
            elif data.tag == "particle frequency":
                entity.particle_frequency = int(float(data.value))
            elif data.tag == "particle emit angle":
                entity.particle_emit_angle = int(float(data.value))
            elif data.tag == "particle face dir":
                entity.particle_face_direction = int(float(data.value))
            elif data.tag == "particle transparency":
                entity.particle_transparency = int(float(data.value))
            elif data.tag == "particle dir x":
                entity.particle_dir_x = int(float(data.value))
            elif data.tag == "particle dir y":
                entity.particle_dir_y = int(float(data.value))
            elif data.tag == "particle rot x":
                entity.particle_rot_x = int(float(data.value))
            elif data.tag == "particle rot y":
                entity.particle_rot_y = int(float(data.value))
            elif data.tag == "particle x1":
                entity.particle_x1 = int(float(data.value))
            elif data.tag == "particle y1":
                entity.particle_y1 = int(float(data.value))
            elif data.tag == "particle x2":
                entity.particle_x2 = int(float(data.value))
            elif data.tag == "particle y2":
                entity.particle_y2 = int(float(data.value))
            elif data.tag == "particle vel x":
                entity.particle_vel_x = int(float(data.value))
            elif data.tag == "particle vel y":
                entity.particle_vel_y = int(float(data.value))
            elif data.tag == "particle colours":
                entity.particle_colour_key_frames = data.value
            elif data.tag == "particle scales":
                entity.particle_scale_key_frames = data.value
            elif data.tag == "particle forces":
                entity.particle_forces = data.value
            elif data.tag == "angulardamping":
                entity.angular_damping = int(float(data.value))
            elif data.tag == "centreofmassx":
                entity.centre_of_mass_x = int(float(data.value))
            elif data.tag == "centreofmassy":
                entity.centre_of_mass_y = int(float(data.value))
            elif data.tag == "canrotate":
                entity.can_rotate = int(float(data.value))
            elif data.tag == "damping":
                entity.damping = int(float(data.value))
            elif data.tag == "friction":
                entity.friction = int(float(data.value))
            elif data.tag == "isbullet":
                entity.is_bullet = int(float(data.value))
            elif data.tag == "issensor":
                entity.is_sensor = int(float(data.value))
            elif data.tag == "mass":
                entity.mass = int(float(data.value))
            elif data.tag == "restitution":
                entity.restitution = int(float(data.value))


def parse_settings_data(self, data):

    # we have found an entity, look through all supported data, if we find
    # a match then store the data in the entities array

    # need to split this into different kinds of entities so we can parse
    # edit boxes, text, virtual buttons etc.individually
    tags = ["", "width", "height", "orientation", "custom res", "scene colours"]

    for tag in tags:
        if data.tag == tag:
            if data.tag == "width":
                self.base_width = int(float((data.value)))
            elif data.tag == "height":
                self.base_height = int(float((data.value)))
            elif data.tag == "custom res":
                self.VisualEditor_CustomResolutions = data.value
            elif data.tag == "scene colours":
                self.scene_colours = data.value
            elif data.tag == "orientation":
                if data.value == "Portrait":
                    agk.set_orientation_allowed(1, 1, 0, 0)
                elif data.value == "Landscape":
                    agk.set_orientation_allowed(0, 0, 1, 1)
                else:
                    agk.set_orientation_allowed(1, 1, 1, 1)
