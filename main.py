import appgamekit as agk
from VisualEditor import VisualEditor


with agk.Application():
    # Setup the editor and load first scene.
    vis_editor = VisualEditor(True)

    # Load new scene numbers start at 0
    vis_editor.open_scene(0)

    # Get Sprite ID
    sprite = vis_editor.get_entity_id("sprite 1", 0)
    # Get Entity Type
    kind = vis_editor.get_entity_kind("sprite 1", 0)

    while True:
        agk.sync()

        if agk.get_raw_key_pressed(27):
            break
