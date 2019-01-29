import appgamekit as agk
from VisualEditor_Image import *
from VisualEditor_utilities import *
# from VisualEditor_properties import Resolution

def set_scene_sprite(self, scene_entity):
    entity = self.entities[scene_entity.index]

    if self.load_all_media is False or scene_entity.created == 0:
        if len(entity.sub_image) > 0:
            image = self.load_sub_image(entity.image, entity.sub_image)
        else:
            image = load_image(self, entity.image)

    scene_entity.id = agk.create_sprite(image)
    agk.set_sprite_position(scene_entity.id, entity.x, entity.y)
    agk.set_sprite_size(scene_entity.id, entity.size_x, entity.size_y)
    agk.set_sprite_scale(scene_entity.id, entity.scale_x, entity.scale_y)
    agk.set_sprite_offset(scene_entity.id, entity.offset_x, entity.offset_y)
    agk.set_sprite_angle(scene_entity.id, entity.angle)
    agk.set_sprite_depth(scene_entity.id, entity.depth)
    agk.set_sprite_color(scene_entity.id, entity.red, entity.green, entity.blue, entity.alpha)
    agk.set_sprite_shape(scene_entity.id, entity.collision)
    agk.set_sprite_visible(scene_entity.id, entity.visible)
    agk.fix_sprite_to_screen(scene_entity.id, entity.fixed)

    # switch to static if nothing has been set
    if entity.physics == 1:
        entity.physics = 2

    if entity.physics >= 1:
        agk.set_sprite_physics_on(scene_entity.id, entity.physics)
        agk.set_sprite_physics_angular_damping(scene_entity.id, entity.angular_damping)
        agk.set_sprite_physics_com(scene_entity.id, entity.centre_of_mass_x, entity.centre_of_mass_y)
        agk.set_sprite_physics_can_rotate(scene_entity.id,entity.can_rotate)
        agk.set_sprite_physics_damping(scene_entity.id, entity.damping)
        agk.set_sprite_physics_friction(scene_entity.id, entity.friction)
        agk.set_sprite_physics_is_bullet(scene_entity.id, entity.is_bullet)
        agk.set_sprite_physics_is_sensor(scene_entity.id, entity.is_sensor)
        agk.set_sprite_physics_mass(scene_entity.id, entity.mass)
        agk.set_sprite_physics_restitution(scene_entity.id, entity.restitution)

    agk.set_sprite_active(scene_entity.id, 1)
    agk.set_sprite_flip(scene_entity.id, entity.flip_h, entity.flip_v)

    if self.override_index == 0:
        update_for_different_resolution(self, entity, scene_entity.id, self.constants.VISUAL_EDITOR_SPRITE)

    else:
        agk.set_sprite_position(scene_entity.id, entity.overrides[self.override_index].x, entity.overrides[self.override_index].y)
        agk.set_sprite_size(scene_entity.id, entity.overrides[self.override_index].size_x, entity.overrides[self.override_index].size_y)

    setup_animation(self, entity, scene_entity.id)


def set_scene_text(self, scene_entity):
    entity = self.entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        scene_entity.id = agk.create_text(entity.text)

    agk.set_text_position(scene_entity.id, entity.x, entity.y)
    agk.set_text_size(scene_entity.id, entity.text_size)
    agk.set_text_alignment(scene_entity.id, entity.alignment)
    agk.set_text_color(scene_entity.id, entity.red, entity.green, entity.blue, entity.alpha)
    agk.set_text_depth(scene_entity.id, entity.depth)
    agk.set_text_angle(scene_entity.id, entity.angle)
    agk.set_text_visible(scene_entity.id, entity.visible)
    agk.fix_text_to_screen(scene_entity.id, entity.fixed)

    if entity.s_font != "":
        font = self.VisualEditor_LoadFont(entity.s_font)
        agk.set_text_font(scene_entity.id, font)
    else:
        agk.use_new_default_fonts(1)


def set_scene_text_box(self, scene_entity):
    entity = self.entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        scene_entity.id = agk.create_edit_box()

    agk.set_edit_box_position(scene_entity.id, entity.x, entity.y)
    agk.set_edit_box_size(scene_entity.id, entity.size_x, entity.size_y)
    agk.set_edit_box_text(scene_entity.id, entity.text)
    agk.set_edit_box_text_size(scene_entity.id, entity.edit_size)
    agk.set_edit_box_text_color(scene_entity.id, entity.edit_colour_red, entity.edit_colour_green, entity.edit_colour_blue)
    agk.set_edit_box_background_color(scene_entity.id, entity.edit_background_red, entity.edit_background_green, entity.edit_background_blue, entity.edit_background_alpha)
    agk.set_edit_box_border_color(scene_entity.id, entity.edit_border_red, entity.edit_border_green,  entity.edit_border_blue, entity.edit_border_alpha)
    agk.set_edit_box_border_size(scene_entity.id, entity.edit_border_size)
    agk.set_edit_box_max_chars(scene_entity.id, entity.edit_max_characters)
    agk.set_edit_box_max_lines(scene_entity.id, entity.edit_max_lines)
    agk.set_edit_box_multiline(scene_entity.id, entity.edit_multi_lines)
    agk.set_edit_box_password_mode(scene_entity.id, entity.edit_password)
    agk.set_edit_box_cursor_color(scene_entity.id, entity.edit_cursor_red, entity.edit_cursor_green, entity.edit_cursor_blue)
    agk.set_edit_box_cursor_width(scene_entity.id, entity.edit_cursor_width)
    agk.set_edit_box_wrap_mode(scene_entity.id, entity.edit_cursor_wrap)
    agk.set_edit_box_depth(scene_entity.id, entity.depth)
    agk.set_edit_box_visible(scene_entity.id, entity.visible)
    agk.fix_edit_box_to_screen(scene_entity.id, entity.fixed)


def set_scene_virtual_button(self, scene_entity):
    entity = self.entities[scene_entity.index]

    offset = entity.size_x / 2.0
    scene_entity.id = self.buttons

    if self.load_all_media == 0 or scene_entity.created == 0:
        agk.add_virtual_button(scene_entity.id, entity.x + offset, entity.y + offset, entity.size_x)
        agk.set_virtual_button_size(scene_entity.id, entity.size_x, entity.size_y)

    agk.set_virtual_button_visible(scene_entity.id, entity.visible)

    if self.override_index == 0:
        update_for_different_resolution(self, entity, scene_entity.id, self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON)
    else:
        agk.set_virtual_button_position(scene_entity.id, entity.overrides[self.override_index].x + offset, entity.overrides[self.override_index].y + offset)
        agk.set_virtual_button_size(scene_entity.id, entity.overrides[self.override_index].size_x, entity.overrides[self.override_index].size_y)

    if agk.find_string(entity.button_up, ".png") or agk.find_string(entity.button_up, ".jpg"):
        agk.set_virtual_button_image_up(scene_entity.id, agk.load_image(entity.button_up))

    if agk.find_string(entity.button_down, ".png") or agk.find_string(entity.button_down, ".jpg"):
        agk.set_virtual_button_image_down(scene_entity.id, agk.load_image(entity.button_down))

    agk.set_virtual_button_color(scene_entity.id, entity.red, entity.green, entity. blue)
    agk.set_virtual_button_alpha(scene_entity.id, entity.alpha)
    agk.set_virtual_button_text(scene_entity.id, entity.button_text)

    self.buttons += 1


def set_scene_virtual_particles(self, scene_entity):
    entity = self.entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        scene_entity.id = agk.create_particles(entity .x, entity .y)

    agk.clear_particles_colors(scene_entity.id)
    agk.clear_particles_forces(scene_entity.id)
    agk.clear_particles_scales(scene_entity.id)

    agk.set_particles_position(scene_entity.id, entity.x, entity.y)
    agk.set_particles_size(scene_entity.id, entity.particle_size)
    agk.set_particles_depth(scene_entity.id, entity.depth)
    agk.set_particles_visible(scene_entity.id, entity.visible)
    agk.fix_particles_to_screen(scene_entity.id, entity.fixed)

    agk.set_particles_life(scene_entity.id, entity.particle_life)
    agk.set_particles_max(scene_entity.id, entity.particle_max)
    agk.set_particles_frequency(scene_entity.id, entity.particle_frequency)
    agk.set_particles_angle(scene_entity.id, entity.particle_emit_angle)
    agk.set_particles_face_direction(scene_entity.id, entity.particle_face_direction)
    agk.set_particles_transparency(scene_entity.id, entity.particle_transparency)
    agk.set_particles_direction(scene_entity.id, entity.particle_dir_x, entity.particle_dir_y)
    agk.set_particles_rotation_range(scene_entity.id, entity.particle_rot_x, entity.particle_rot_y)
    agk.set_particles_start_zone(scene_entity.id, entity.particle_x1, entity.particle_y1, entity.particle_x2, entity.particle_y2)
    agk.set_particles_velocity_range(scene_entity.id, entity.particle_vel_x, entity.particle_vel_y)

    # colour key frames
    count = agk.count_string_tokens(entity.particle_colour_key_frames, " ")


    if count % 5 == 0:
        offset = 1

        for i in range(0, int(count / 5)):
            time = float(agk.get_string_token(entity.particle_colour_key_frames, " ", offset + 0))
            red = int(agk.get_string_token(entity.particle_colour_key_frames, " ", offset + 1))
            green = int(agk.get_string_token(entity.particle_colour_key_frames, " ", offset + 2))
            blue = int(agk.get_string_token(entity.particle_colour_key_frames, " ", offset + 3))
            alpha = int(agk.get_string_token(entity.particle_colour_key_frames, " ", offset + 4))
            debug_text = str(time) + " " + str(red) + " " + str(green) + " " +  str(blue) + " " + str(alpha)
            agk.add_particles_color_key_frame(scene_entity.id, time, red, green, blue, alpha)
            offset += 5

    # scale key frames
    count = agk.count_string_tokens(entity.particle_scale_key_frames, " ")

    if count % 2 == 0:
        offset = 1

    for i in range(int(count / 2)):
        time = float(agk.get_string_token(entity.particle_scale_key_frames, " ", offset + 0))
        scale = float(agk.get_string_token(entity.particle_scale_key_frames, " ", offset + 1))
        agk.add_particles_scale_key_frame(scene_entity.id, time, scale)
        offset += 2

    # forces
    count = agk.count_string_tokens(entity.particle_forces, " ")

    if count % 5 == 0:
        offset = 1

        for i in range(int(count / 4)):
            start_time = float(agk.get_string_token(entity.particle_forces, " ", offset + 0 ))
            end_time = float(agk.get_string_token(entity.particle_forces, " ", offset + 1 ))
            x = float(agk.get_string_token(entity.particle_forces, " ", offset + 2 ))
            y = float(agk.get_string_token(entity.particle_forces, " ", offset + 3 ))
            agk.add_particles_force(scene_entity.id, start_time, end_time, x, y)
            offset = offset + 4

    if agk.find_string(entity.particle_image, ".png") or agk.find_string(entity.particle_image, ".jpg"):
        agk.set_particle_image(scene_entity.id, agk.load_image(entity.particle_image))
    else:
        agk.set_particles_image(scene_entity.id, agk.load_image("default_particle.png"))

    if self.override_index == 0:
        update_for_different_resolution(self, entity, scene_entity.id, self.constants.VISUAL_EDITOR_PARTICLES)
    else:
        agk.Set_particles_position(scene_entity.id, entity.overrides[self.override_index].x, entity.overrides[self.override_index].y)

