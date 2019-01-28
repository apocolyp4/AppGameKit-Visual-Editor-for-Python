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
        self.VisualEditor_Entities = []
        self.VisualEditor_Characters = [""]
        self.images = []
        self.VisualEditor_SubImages = []
        self.VisualEditor_Resolutions = [Resolution()]
        self.VisualEditor_Fonts = [Font()]
        self.constants = Constants()
        self.project_data = []
        self.overrideIndex = 0

        self.VisualEditor_CustomResolutions = ""
        self.VisualEditor_SceneColours = ""
        self.manager = Manager()
        self.VisualEditor_FileIndex = 0
        self.load_all_media = 0

        self.VisualEditor_Width = 0
        self.VisualEditor_Height = 0

        self.VisualEditor_BaseWidth = 1024
        self.VisualEditor_BaseHeight = 768

        self.VisualEditor_OriginalWidth = 0.0
        self.VisualEditor_OriginalHeight = 0.0
        self.VisualEditor_TargetWidth = 0.0
        self.VisualEditor_TargetHeight = 0.0
        self. VisualEditor_BorderInPixels = 0.0
        self.VisualEditor_BorderInPixelsY = 0.0

        self.VisualEditor_Lines = [""] * 100000
        self.VisualEditor_EntitiesIndex = 0
        self.VisualEditor_Buttons = 1

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

        self.VisualEditor_Width = self.VisualEditor_BaseWidth
        self.VisualEditor_Height = self.VisualEditor_BaseHeight

        # need to the closest resolution to the one we support
        find_closest_resolution(self)

        # to override the resolution adjust the values here
        # self.VisualEditor_Width = 320
        # self.VisualEditor_Height = 480

        agk.set_virtual_resolution(self.VisualEditor_Width, self.VisualEditor_Height)
        agk.set_window_size(self.VisualEditor_Width, self.VisualEditor_Height, 0)

        get_new_resolution(self, self.VisualEditor_Width, self.VisualEditor_Height)

        setup_scenes(self)

    def open_scene(self, scene_id):
        set_scene(self, scene_id)

    def get_entity_id(self, entity_name, scene_id):
        return get_id(self, entity_name, scene_id)

    def get_entity_kind(self, entity_name, scene_id):
        return get_kind(self, entity_name, scene_id)