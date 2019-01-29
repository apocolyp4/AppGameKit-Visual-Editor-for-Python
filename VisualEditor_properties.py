class Constants:
    def __init__(self):
        self.VISUAL_EDITOR_SPRITE = 1
        self.VISUAL_EDITOR_TEXT = 2
        self.VISUAL_EDITOR_EDIT_BOX = 3
        self.VISUAL_EDITOR_VIRTUAL_BUTTON = 4
        self.VISUAL_EDITOR_PARTICLES = 5
        self.VISUAL_EDITOR_LOAD_FOR_SCENE = 0
        self.VISUAL_EDITOR_LOAD_ALL_MEDIA = 1

class Resolution:
    def __init__(self):
        self.width = 0
        self.height = 0

class Override:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.x = 0.0
        self.y = 0.0
        self.size_x = 0.0
        self.size_y = 0.0

class SceneEntity:
    def __init__(self):
        self.id = 0
        self.kind = 0
        self.index = 0
        self.created = 0

class Font:
    def __init__(self):
        self.s_file = ""
        self.id = 0

class Image:
    def __init__(self):
        self.image = ""
        self.id = -1

class Manager:
    def __init__(self):
        self.current_scene = -1

class Scene:
    def __init__(self):
        self.entities = [SceneEntity()]
        self.clear_colour_red = 0
        self.clear_colour_green = 0
        self.clear_colour_blue = 0


class AnimationFrame:
    def __init__(self):
        self.image = ""
        self.sub_image = ""
        self.i_image = 0

class AnimationSet:
    def __init__(self):
        self.name = ""
        self.speed = 0.0
        self.loop_mode = 0
        self.start_frame = 0
        self.end_frame = 0
        self.frames = [AnimationFrame()]

class FileEntity:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.image = ""
        self.sub_image = ""
        self.text = ""
        self.scene = 0
        self.s_font = ""
        self.x = 0.0
        self.y = 0.0
        self.size_x = 0.0
        self.size_y = 0.0
        self.scale_x = 0.0
        self.scale_y = 0.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.angle = 0.0
        self.depth = 0
        self.visible = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        self.alpha = 0
        self.alignment = 0
        self.text_size = 0.0
        self.collision = 0
        self.active = 0
        self.physics = 0
        self.flip_h = 0
        self.flip_v = 0
        self.fixed = 0
        self.dynamic_res = ""

        self.custom = [""]

        self.anim_play = 0
        self.animation_set = [AnimationSet()]

        self.overrides = [Override()]

        # editbox properties
        self.edit_size = 0.0
        self.edit_colour_red = 0
        self.edit_colour_green = 0
        self.edit_colour_blue = 0
        self.edit_background_red = 0
        self.edit_background_green = 0
        self.edit_background_blue = 0
        self.edit_background_alpha = 0
        self.edit_border_red = 0
        self.edit_border_green = 0
        self.edit_border_blue = 0
        self.edit_border_alpha = 0
 
        self.edit_border_size = 0.0
        self.edit_max_characters = 0
        self.edit_max_lines = 0
        self.edit_multi_lines = 0
        self.edit_password = 0
        self.edit_cursor_red = 0
        self.edit_cursor_green = 0
        self.edit_cursor_blue = 0
        self.edit_cursor_width = 0.0
        self.edit_cursor_wrap = 0

        # button properties
        self.button_down = ""
        self.button_up = ""
        self.button_text = ""
        self.button_goto = 0

        # particle properties
        self.particle_image = ""
        self.particle_size = 0.0
        self.particle_life = 0.0
        self.particle_max = 0
        self.particle_frequency = 0
        self.particle_emit_angle = 0.0
        self.particle_face_direction = 0
        self.particle_transparency = 0
        self.particle_dir_x = 0.0
        self.particle_dir_y = 0.0
        self.particle_rot_x = 0.0
        self.particle_rot_y = 0.0
        self.particle_x1 = 0.0
        self.particle_y1 = 0.0
        self.particle_x2 = 0.0
        self.particle_y2 = 0.0
        self.particle_vel_x = 0.0
        self.particle_vel_y = 0.0
        self.particle_colour_key_frames = ""
        self.particle_scale_key_frames = ""
        self.particle_forces = ""

        self.angular_damping = 0.0
        self.centre_of_mass_x = 0.0
        self.centre_of_mass_y = 0.0
        self.can_rotate = 0
        self.damping = 0.0
        self.friction = 0.0
        self.is_bullet = 0
        self.is_sensor = 0
        self.mass = 0.0
        self.restitution = 0.0
