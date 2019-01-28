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
    self.VisualEditor_EntitiesIndex = 0
    self.VisualEditor_Lines = []

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
    self.VisualEditor_Entities = []
    data_type = "settings"
    for data in self.project_data:
        if data.tag == "settings":
            data_type = "settings"

        elif data.tag == "/settings":
            data_type = ""

        if data.tag == "entity":
            data_type = "entity"
            self.VisualEditor_Entities.append(FileEntity())

        elif data.tag == "/entity":
            data_type = ""

        elif data_type == "settings":
            parse_settings_data(self, data)

        elif data_type == "entity":
            parse_entity_data(self, self.VisualEditor_Entities[-1], data)




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
                entity.sType = data.value
            elif data.tag == "name":
                entity.sName = data.value
            elif data.tag == "font":
                entity.sFont = data.value
            elif data.tag == "scene":
                entity.scene = int(data.value)
            elif data.tag == "visible":
                entity.visible = int(data.value)
            elif data.tag == "fliph":
                entity.flipH = int(data.value)
            elif data.tag == "flipv":
                entity.flipV = int(data.value)
            elif data.tag == "x":
                entity.x = int(float(data.value))
            elif data.tag == "y":
                entity.y = int(float(data.value))
            elif data.tag == "custom":
                new_size = len(entity.custom) + 1
                entity.custom = resize_list(entity.custom, new_size, "")
                entity.custom[len(entity.custom) - 1] = data.value
            elif data.tag == "animplay":
                entity.animPlay = int(float(data.value))
            elif data.tag == "animset":
                new_size = len(entity.animationSet) + 1
                entity.animationSet = resize_list(entity.animationSet, new_size, "")
                entity.animationSet.animationSet[len(entity.animationSet) - 1].sName = data.value
            elif data.tag == "animspeed":
                entity.animationSet[len(entity.animationSet) - 1].speed = int(float(data.value))
            elif data.tag == "animloop":
                entity.animationSet[len(entity.animationSet) - 1].loopMode = int(float(data.value))
            elif data.tag == "animframe":
                i = len(entity.animationSet)
                new_size = len(entity.animationSet[i].frames) + 1
                entity.animationSet[i].frames = resize_list(entity.animationSet[i].frames, new_size, AnimationFrame())
                j = len(entity.animationSet[i].frames)
                entity.animationSet[i].frames[j].sImage = data.value
            elif data.tag == "image":
                entity.sImage = agk.replace_string(data.value, "media/", "", 1)
            elif data.tag == "subimage":
                entity.sSubImage = data.value
            elif data.tag == "size x":
                entity.sizeX = int(float(data.value))
            elif data.tag == "size y":
                entity.sizeY = int(float(data.value))
            elif data.tag == "scale x":
                entity.scaleX = int(float(data.value))
            elif data.tag == "scale y":
                entity.scaleY = int(float(data.value))
            elif data.tag == "offset x":
                entity.offsetX = int(float(data.value))
            elif data.tag == "offset y":
                entity.offsetY = int(float(data.value))
            elif data.tag == "angle":
                entity.angle = int(float(data.value))
            elif data.tag == "fixed":
                entity.fixed = int(float(data.value))
            elif data.tag == "text":
                entity.sText = entity.sText + data.value + chr(10)
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
                entity.textSize = int(float(data.value))
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
                entity.dynamicRes = data.value
            elif data.tag == "edit size":
                entity.editSize = int(float(data.value))
            elif data.tag == "edit colour red":
                entity.editColourRed = int(float(data.value))
            elif data.tag == "edit colour green":
                entity.editColourGreen = int(float(data.value))
            elif data.tag == "edit colour blue":
                entity.editColourBlue = int(float(data.value))
            elif data.tag == "edit background red":
                entity.editBackgroundRed = int(float(data.value))
            elif data.tag == "edit background green":
                entity.editBackgroundGreen = int(float(data.value))
            elif data.tag == "edit background blue":
                entity.editBackgroundBlue = int(float(data.value))
            elif data.tag == "edit background alpha":
                entity.editBackgroundAlpha = int(float(data.value))
            elif data.tag == "edit border red":
                entity.editBorderRed = int(float(data.value))
            elif data.tag == "edit border green":
                entity.editBorderGreen = int(float(data.value))
            elif data.tag == "edit border blue":
                entity.editBorderBlue = int(float(data.value))
            elif data.tag == "edit border alpha":
                entity.editBorderAlpha = int(float(data.value))
            elif data.tag == "edit border size":
                entity.editBorderSize = int(float(data.value))
            elif data.tag == "edit max characters":
                entity.editMaxCharacters = int(float(data.value))
            elif data.tag == "edit max lines":
                entity.editMaxLines = int(float(data.value))
            elif data.tag == "edit multi line":
                entity.editMultiLine = int(float(data.value))
            elif data.tag == "edit password":
                entity.editPassword = int(float(data.value))
            elif data.tag == "edit cursor red":
                entity.editCursorRed = int(float(data.value))
            elif data.tag == "edit cursor green":
                entity.editCursorGreen = int(float(data.value))
            elif data.tag == "edit cursor blue":
                entity.editCursorBlue = int(float(data.value))
            elif data.tag == "edit cursor width":
                entity.editCursorWidth = int(float(data.value))
            elif data.tag == "edit cursor wrap":
                entity.editCursorWrap = int(float(data.value))
            elif data.tag == "button down":
                entity.buttonDown = agk.replace_string(data.value, "media/", "", 1)
            elif data.tag == "button up":
                entity.buttonUp = agk.replace_string(data.value, "media/", "", 1)
            elif data.tag == "button text":
                entity.buttonText = data.value
            elif data.tag == "button goto":
                entity.buttonGoto = int(float(data.value))
            elif data.tag == "particle image":
                entity.particleImage = data.value
            elif data.tag == "particle size":
                entity.particleSize = int(float(data.value))
            elif data.tag == "particle life":
                entity.particleLife = int(float(data.value))
            elif data.tag == "particle max":
                entity.particleMax = int(float(data.value))
            elif data.tag == "particle frequency":
                entity.particleFrequency = int(float(data.value))
            elif data.tag == "particle emit angle":
                entity.particleEmitAngle = int(float(data.value))
            elif data.tag == "particle face dir":
                entity.particleFaceDirection = int(float(data.value))
            elif data.tag == "particle transparency":
                entity.particleTransparency = int(float(data.value))
            elif data.tag == "particle dir x":
                entity.particleDirX = int(float(data.value))
            elif data.tag == "particle dir y":
                entity.particleDirY = int(float(data.value))
            elif data.tag == "particle rot x":
                entity.particleRotX = int(float(data.value))
            elif data.tag == "particle rot y":
                entity.particleRotY = int(float(data.value))
            elif data.tag == "particle x1":
                entity.particleX1 = int(float(data.value))
            elif data.tag == "particle y1":
                entity.particleY1 = int(float(data.value))
            elif data.tag == "particle x2":
                entity.particleX2 = int(float(data.value))
            elif data.tag == "particle y2":
                entity.particleY2 = int(float(data.value))
            elif data.tag == "particle vel x":
                entity.particleVelX = int(float(data.value))
            elif data.tag == "particle vel y":
                entity.particleVelY = int(float(data.value))
            elif data.tag == "particle colours":
                entity.particleColourKeyFrames = data.value
            elif data.tag == "particle scales":
                entity.particleScaleKeyFrames = data.value
            elif data.tag == "particle forces":
                entity.particleForces = data.value
            elif data.tag == "angulardamping":
                entity.angularDamping = int(float(data.value))
            elif data.tag == "centreofmassx":
                entity.centreOfMassX = int(float(data.value))
            elif data.tag == "centreofmassy":
                entity.centreOfMassY = int(float(data.value))
            elif data.tag == "canrotate":
                entity.canRotate = int(float(data.value))
            elif data.tag == "damping":
                entity.damping = int(float(data.value))
            elif data.tag == "friction":
                entity.friction = int(float(data.value))
            elif data.tag == "isbullet":
                entity.isBullet = int(float(data.value))
            elif data.tag == "issensor":
                entity.isSensor = int(float(data.value))
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
                self.VisualEditor_BaseWidth = int(float((data.value)))
            elif data.tag == "height":
                self.VisualEditor_BaseHeight = int(float((data.value)))
            elif data.tag == "custom res":
                self.VisualEditor_CustomResolutions = data.value
            elif data.tag == "scene colours":
                self.VisualEditor_SceneColours = data.value
            elif data.tag == "orientation":
                if data.value == "Portrait":
                    agk.set_orientation_allowed(1, 1, 0, 0)
                elif data.value == "Landscape":
                    agk.set_orientation_allowed(0, 0, 1, 1)
                else:
                    agk.set_orientation_allowed(1, 1, 1, 1)
