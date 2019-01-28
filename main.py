import appgamekit as agk
from VisualEditor import VisualEditor


with agk.Application():
    #setup the editor
    vis_editor = VisualEditor(0)
    vis_editor.open_scene(0)

	#Get Sprite ID
    sprite = vis_editor.get_entity_id("sprite 1", 0)
    #Get Entity Type
    kind = vis_editor.get_entity_kind("sprite 1", 0)

    agk.set_clear_color(255, 255, 255)

    scene_no = 0

    while True:
        if agk.get_pointer_pressed() == 1:
            scene_no += 1
            if scene_no > 2:
                scene_no = 0
            vis_editor.open_scene(scene_no)

        agk.sync()

        if agk.get_raw_key_pressed(27):
            break
