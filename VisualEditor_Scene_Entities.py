import appgamekit as agk
from VisualEditor_Image import *
from VisualEditor_utilities import *
# from VisualEditor_properties import Resolution

def set_scene_sprite(self, scene_entity):
    entity = self.VisualEditor_Entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        if len(entity.sSubImage) > 0:
            image = self.VisualEditor_LoadSubImage(entity.sImage, entity.sSubImage)
        else:
            image = load_image(self, entity.sImage)

    scene_entity.id = agk.create_sprite(image)
    agk.set_sprite_position(scene_entity.id, entity.x, entity.y)
    agk.set_sprite_size(scene_entity.id, entity.sizeX, entity.sizeY)
    agk.set_sprite_scale(scene_entity.id, entity.scaleX, entity.scaleY)
    agk.set_sprite_offset(scene_entity.id, entity.offsetX, entity.offsetY)
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
        agk.set_sprite_physics_angular_damping(scene_entity.id, entity.angularDamping)
        agk.set_sprite_physics_com(scene_entity.id, entity.centreOfMassX, entity.centreOfMassY)
        agk.set_sprite_physics_can_rotate(scene_entity.id,entity.canRotate)
        agk.set_sprite_physics_damping(scene_entity.id, entity.damping)
        agk.set_sprite_physics_friction(scene_entity.id, entity.friction)
        agk.set_sprite_physics_is_bullet(scene_entity.id, entity.isBullet)
        agk.set_sprite_physics_is_sensor(scene_entity.id, entity.isSensor)
        agk.set_sprite_physics_mass(scene_entity.id, entity.mass)
        agk.set_sprite_physics_restitution(scene_entity.id, entity.restitution)

    agk.set_sprite_active(scene_entity.id, 1)
    agk.set_sprite_flip(scene_entity.id, entity.flipH, entity.flipV)

    if self.overrideIndex == 0:
        VisualEditor_UpdateForDifferentResolution(self, entity, scene_entity.id, self.constants.VISUAL_EDITOR_SPRITE)

    else:
        agk.set_sprite_position(scene_entity.id, entity.overrides[self.overrideIndex].x, entity.overrides[self.overrideIndex].y)
        agk.set_sprite_size(scene_entity.id, entity.overrides[self.overrideIndex].sizeX, entity.overrides[self.overrideIndex].sizeY)

    setup_animation(self, entity, scene_entity.id)


def set_scene_text(self, scene_entity):
    entity = self.VisualEditor_Entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        scene_entity.id = agk.create_text(entity.sText)

    agk.set_text_position(scene_entity.id, entity.x, entity.y)
    agk.set_text_size(scene_entity.id, entity.textSize)
    agk.set_text_alignment(scene_entity.id, entity.alignment)
    agk.set_text_color(scene_entity.id, entity.red, entity.green, entity.blue, entity.alpha)
    agk.set_text_depth(scene_entity.id, entity.depth)
    agk.set_text_angle(scene_entity.id, entity.angle)
    agk.set_text_visible(scene_entity.id, entity.visible)
    agk.fix_text_to_screen(scene_entity.id, entity.fixed)

    if entity.sFont != "":
        font = self.VisualEditor_LoadFont(entity.sFont)
        agk.set_text_font(scene_entity.id, font)
    else:
        agk.use_new_default_fonts(1)


def set_scene_text_box(self, scene_entity):
    entity = self.VisualEditor_Entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        scene_entity.id = agk.create_edit_box()

    agk.set_edit_box_position(scene_entity.id, entity.x, entity.y)
    agk.set_edit_box_size(scene_entity.id, entity.sizeX, entity.sizeY)
    agk.set_edit_box_text(scene_entity.id, entity.sText)
    agk.set_edit_box_text_size(scene_entity.id, entity.editSize)
    agk.set_edit_box_text_color(scene_entity.id, entity.editColourRed, entity.editColourGreen, entity.editColourBlue)
    agk.set_edit_box_background_color(scene_entity.id, entity.editBackgroundRed, entity.editBackgroundGreen, entity.editBackgroundBlue, entity.editBackgroundAlpha)
    agk.set_edit_box_border_color(scene_entity.id, entity.editBorderRed, entity.editBorderGreen,  entity.editBorderBlue, entity.editBorderAlpha)
    agk.set_edit_box_border_size(scene_entity.id, entity.editBorderSize)
    agk.set_edit_box_max_chars(scene_entity.id, entity.editMaxCharacters)
    agk.set_edit_box_max_lines(scene_entity.id, entity.editMaxLines)
    agk.set_edit_box_multiline(scene_entity.id, entity.editMultiLine)
    agk.set_edit_box_password_mode(scene_entity.id, entity.editPassword)
    agk.set_edit_box_cursor_color(scene_entity.id, entity.editCursorRed, entity.editCursorGreen, entity.editCursorBlue)
    agk.set_edit_box_cursor_width(scene_entity.id, entity.editCursorWidth)
    agk.set_edit_box_wrap_mode(scene_entity.id, entity.editCursorWrap)
    agk.set_edit_box_depth(scene_entity.id, entity.depth)
    agk.set_edit_box_visible(scene_entity.id, entity.visible)
    agk.fix_edit_box_to_screen(scene_entity.id, entity.fixed)


def set_scene_virtual_button(self, scene_entity):
    entity = self.VisualEditor_Entities[scene_entity.index]

    offset = entity.sizeX / 2.0
    scene_entity.id = self.VisualEditor_Buttons

    if self.load_all_media == 0 or scene_entity.created == 0:
        agk.add_virtual_button(scene_entity.id, entity.x + offset, entity.y + offset, entity.sizeX)
        agk.set_virtual_button_size(scene_entity.id, entity.sizeX, entity.sizeY)

    agk.set_virtual_button_visible(scene_entity.id, entity.visible)

    if self.overrideIndex == 0:
        VisualEditor_UpdateForDifferentResolution(self, entity, scene_entity.id, self.constants.VISUAL_EDITOR_VIRTUAL_BUTTON)
    else:
        agk.set_virtual_button_position(scene_entity.id, entity.overrides[self.overrideIndex].x + offset, entity.overrides[self.overrideIndex].y + offset)
        agk.set_virtual_button_size(scene_entity.id, entity.overrides[self.overrideIndex].size_x, entity.overrides[self.overrideIndex].size_y)

    if agk.find_string(entity.buttonUp, ".png") or agk.find_string(entity.buttonUp, ".jpg"):
        agk.set_virtual_button_image_up(scene_entity.id, agk.load_image(entity.buttonUp))

    if agk.find_string(entity.buttonDown, ".png") or agk.find_string(entity.buttonDown, ".jpg"):
        agk.set_virtual_button_image_down(scene_entity.id, agk.load_image(entity.buttonDown))

    agk.set_virtual_button_color(scene_entity.id, entity.red, entity.green, entity. blue)
    agk.set_virtual_button_alpha(scene_entity.id, entity.alpha)
    agk.set_virtual_button_text(scene_entity.id, entity.buttonText)

    self.VisualEditor_Buttons += 1


def set_scene_virtual_particles(self, scene_entity):
    entity = self.VisualEditor_Entities[scene_entity.index]

    if self.load_all_media == 0 or scene_entity.created == 0:
        scene_entity.id = agk.create_particles(entity .x, entity .y)

    agk.clear_particles_colors(scene_entity.id)
    agk.clear_particles_forces(scene_entity.id)
    agk.clear_particles_scales(scene_entity.id)

    agk.set_particles_position(scene_entity.id, entity.x, entity.y)
    agk.set_particles_size(scene_entity.id, entity.particleSize)
    agk.set_particles_depth(scene_entity.id, entity.depth)
    agk.set_particles_visible(scene_entity.id, entity.visible)
    agk.fix_particles_to_screen(scene_entity.id, entity.fixed)

    agk.set_particles_life(scene_entity.id, entity.particleLife)
    agk.set_particles_max(scene_entity.id, entity.particleMax)
    agk.set_particles_frequency(scene_entity.id, entity.particleFrequency)
    agk.set_particles_angle(scene_entity.id, entity.particleEmitAngle)
    agk.set_particles_face_direction(scene_entity.id, entity.particleFaceDirection)
    agk.set_particles_transparency(scene_entity.id, entity.particleTransparency)
    agk.set_particles_direction(scene_entity.id, entity.particleDirX, entity.particleDirY)
    agk.set_particles_rotation_range(scene_entity.id, entity.particleRotX, entity.particleRotY)
    agk.set_particles_start_zone(scene_entity.id, entity.particleX1, entity.particleY1, entity.particleX2, entity.particleY2)
    agk.set_particles_velocity_range(scene_entity.id, entity.particleVelX, entity.particleVelY)

    # colour key frames
    count = agk.count_string_tokens(entity.particleColourKeyFrames, " ")


    if count % 5 == 0:
        offset = 1

        for i in range(0, int(count / 5)):
            time = float(agk.get_string_token(entity.particleColourKeyFrames, " ", offset + 0))
            red = int(agk.get_string_token(entity.particleColourKeyFrames, " ", offset + 1))
            green = int(agk.get_string_token(entity.particleColourKeyFrames, " ", offset + 2))
            blue = int(agk.get_string_token(entity.particleColourKeyFrames, " ", offset + 3))
            alpha = int(agk.get_string_token(entity.particleColourKeyFrames, " ", offset + 4))
            debug_text = str(time) + " " + str(red) + " " + str(green) + " " +  str(blue) + " " + str(alpha)
            agk.add_particles_color_key_frame(scene_entity.id, time, red, green, blue, alpha)
            offset += 5

    # scale key frames
    count = agk.count_string_tokens(entity.particleScaleKeyFrames, " ")

    if count % 2 == 0:
        offset = 1

    for i in range(int(count / 2)):
        time = float(agk.get_string_token(entity.particleScaleKeyFrames, " ", offset + 0))
        scale = float(agk.get_string_token(entity.particleScaleKeyFrames, " ", offset + 1))
        agk.add_particles_scale_key_frame(scene_entity.id, time, scale)
        offset += 2

    # forces
    count = agk.count_string_tokens(entity.particleForces, " ")

    if count % 5 == 0:
        offset = 1

        for i in range(int(count / 4)):
            start_time = float(agk.get_string_token(entity.particleForces, " ", offset + 0 ))
            end_time = float(agk.get_string_token(entity.particleForces, " ", offset + 1 ))
            x = float(agk.get_string_token(entity.particleForces, " ", offset + 2 ))
            y = float(agk.get_string_token(entity.particleForces, " ", offset + 3 ))
            agk.add_particles_force(scene_entity.id, start_time, end_time, x, y)
            offset = offset + 4

    if agk.find_string(entity.particleImage, ".png") or agk.find_string(entity.particleImage, ".jpg"):
        agk.set_particles_image(scene_entity.id, agk.load_image(entity.particleImage))
    else:
        agk.set_particles_image(scene_entity.id, agk.load_image("default_particle.png"))

    if self.overrideIndex == 0:
        VisualEditor_UpdateForDifferentResolution(self, entity, scene_entity.id, self.constants.VISUAL_EDITOR_PARTICLES)
    else:
        agk.Set_particles_position(scene_entity.id, entity.overrides[self.overrideIndex].x, entity.overrides[self.overrideIndex].y)

