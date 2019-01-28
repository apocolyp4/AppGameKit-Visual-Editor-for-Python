# AppGameKit Visual Editor for Python

You can find the AppGameKit for Python here https://fascimania.itch.io/appgamekit-for-python

version 1.0

AppGameKit Visual Editor for Python currently supports Sprites, Text, Edit Boxes, Virtual Buttons.

The test project is loaded from the main.agc file.


Commands:
	
VisualEditor(int load)

visual_editor = VisualEditor(0)

visual_editor.open_scene(0)

sprite = vis_editor.get_entity_id("sprite 8", 0)
kind = vis_editor.get_entity_kind("sprite 8", 0)
