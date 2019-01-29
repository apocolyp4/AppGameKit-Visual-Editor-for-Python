# AppGameKit Visual Editor for Python

You can find the AppGameKit for Python here https://fascimania.itch.io/appgamekit-for-python

version 1.0

AppGameKit Visual Editor for Python currently supports Sprites, Text, Edit Boxes, Virtual Buttons.

The test project is loaded from the main.agc file.


Commands:
	
# Setups up the editor
vis_editor = VisualEditor(0)

    # Load new scene first scene is 0
    vis_editor.open_scene(0)

	# Get Sprite ID
    sprite = vis_editor.get_entity_id("sprite 1", 0)
    # Get Entity Type
    kind = vis_editor.get_entity_kind("sprite 1", 0)
