import appgamekit as agk
from VisualEditor_utilities import *
from VisualEditor_properties import *
from VisualEditor_load import *
from VisualEditor_Scene import *
from VisualEditor_utilities import *


class VisualEditor():
    def __init__(self, load_all_media):

        self.pairs = [[0 for x in range(2)] for y in range(2)] #String
        self.scenes = [Scene()]
        self.entities = []
        self.characters = [""]
        self.images = []
        self.sub_images = []
        self.resolutions = [Resolution()]
        self.fonts = [Font()]
        self.constants = Constants()
        self.project_data = []
        self.override_index = 0

        self.custom_resolutions = ""
        self.scene_colours = ""
        self.manager = Manager()
        self.file_index = 0
        self.load_all_media = 0

        self.width = 0
        self.height = 0

        self.base_width = 1024
        self.base_height = 768

        self.original_width = 0.0
        self.original_height = 0.0
        self.target_width = 0.0
        self.target_height = 0.0
        self.border_in_pixels = 0.0
        self.border_in_pixels_y = 0.0

        self.buttons = 1

        self.load_all_media = load_all_media

        self.constants = Constants()

        agk.use_new_default_fonts(1)
        agk.set_clear_color(255, 255, 255)
        agk.set_print_color(0, 0, 0)
        agk.set_print_size(24)
        agk.set_scissor(0, 0, 0, 0)

        # default resolutions - needs to be replaced by data from the project file
        add_resolution(self, 640, 960)
        add_resolution(self, 768, 1024)
        add_resolution(self, 720, 1280)
        add_resolution(self, 1080, 1920)
        add_resolution(self, 1200, 1920)
        add_resolution(self, 1536, 2048)
        add_resolution(self, 960, 640)
        add_resolution(self, 1024, 768)
        add_resolution(self, 1280, 720)
        add_resolution(self, 1920, 1080)
        add_resolution(self, 1920, 1200)
        add_resolution(self, 2048, 1536)

        load_project(self, "data.agkd")

        update_custom_resolutions(self)

        self.width = self.base_width
        self.height = self.base_height

        # need to the closest resolution to the one we support
        find_closest_resolution(self)

        # to override the resolution adjust the values here
        # self.width = 320
        # self.height = 480

        agk.set_virtual_resolution(self.width, self.height)
        agk.set_window_size(self.width, self.height, 0)

        get_new_resolution(self, self.width, self.height)

        setup_scenes(self)

    def open_scene(self, scene_id):
        set_scene(self, scene_id)

    def get_entity_id(self, entity_name, scene_id):
        return get_id(self, entity_name, scene_id)

    def get_entity_kind(self, entity_name, scene_id):
        return get_kind(self, entity_name, scene_id)
