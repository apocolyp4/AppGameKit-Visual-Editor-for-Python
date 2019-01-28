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
        self.sFile = ""
        self.id = 0

class Image:
    def __init__(self):
        self.sImage = ""
        self.id = -1

class Manager:
    def __init__(self):
        self.currentScene = 0


class Scene:
    def __init__(self):
        self.entities = [SceneEntity()]
        self.clear_colour_red = 0
        self.clear_colour_green = 0
        self.clear_colour_blue = 0


class AnimationFrame:
    def __init__(self):
        self.sImage = ""
        self.sSubImage = ""
        self.iImage = 0

class AnimationSet:
    def __init__(self):
        self.sName = ""
        self.speed = 0.0
        self.loopMode = 0
        self.startFrame = 0
        self.endFrame = 0
        self.frames = [AnimationFrame()]

class FileEntity:
    def __init__(self):
        self.sType = ""
        self.sName = ""
        self.sImage = ""
        self.sSubImage = ""
        self.sText = ""
        self.scene = 0
        self.sFont = ""
        self.x = 0.0
        self.y = 0.0
        self.sizeX = 0.0
        self.sizeY = 0.0
        self.scaleX = 0.0
        self.scaleY = 0.0
        self.offsetX = 0.0
        self.offsetY = 0.0
        self.angle = 0.0
        self.depth = 0
        self.visible = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        self.alpha = 0
        self.alignment = 0
        self.textSize = 0.0
        self.collision = 0
        self.active = 0
        self.physics = 0
        self.flipH = 0
        self.flipV = 0
        self.fixed = 0
        self.dynamicRes = ""

        self.custom = [""]

        self.animPlay = 0
        self.animationSet = [AnimationSet()]

        self.overrides = [Override()]

        # editbox properties
        self.editSize = 0.0
        self.editColourRed = 0
        self.editColourGreen = 0
        self.editColourBlue = 0
        self.editBackgroundRed = 0
        self.editBackgroundGreen = 0
        self.editBackgroundBlue = 0
        self.editBackgroundAlpha = 0
        self.editBorderRed = 0
        self.editBorderGreen = 0
        self.editBorderBlue = 0
        self.editBorderAlpha = 0
        self.editBorderSize = 0.0
        self.editMaxCharacters = 0
        self.editMaxLines = 0
        self.editMultiLine = 0
        self.editPassword = 0
        self.editCursorRed = 0
        self.editCursorGreen = 0
        self.editCursorBlue = 0
        self.editCursorWidth = 0.0
        self.editCursorWrap = 0

        # button properties
        self.buttonDown = ""
        self.buttonUp = ""
        self.buttonText = ""
        self.buttonGoto = 0

        # particle properties
        self.particleImage = ""
        self.particleSize = 0.0
        self.particleLife = 0.0
        self.particleMax = 0
        self.particleFrequency = 0
        self.particleEmitAngle = 0.0
        self.particleFaceDirection = 0
        self.particleTransparency = 0
        self.particleDirX = 0.0
        self.particleDirY = 0.0
        self.particleRotX = 0.0
        self.particleRotY = 0.0
        self.particleX1 = 0.0
        self.particleY1 = 0.0
        self.particleX2 = 0.0
        self.particleY2 = 0.0
        self.particleVelX = 0.0
        self.particleVelY = 0.0
        self.particleColourKeyFrames = ""
        self.particleScaleKeyFrames = ""
        self.particleForces = ""

        self.angularDamping = 0.0
        self.centreOfMassX = 0.0
        self.centreOfMassY = 0.0
        self.canRotate = 0
        self.damping = 0.0
        self.friction = 0.0
        self.isBullet = 0
        self.isSensor = 0
        self.mass = 0.0
        self.restitution = 0.0