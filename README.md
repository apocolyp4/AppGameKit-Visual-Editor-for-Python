# AppGameKit Visual Editor for Python

You can find the AppGameKit for Python here https://fascimania.itch.io/appgamekit-for-python

version 1.0

AppGameKit Visual Editor for Python currently supports Sprites, Text, Edit Boxes, Virtual Buttons.

The test project is loaded from the main.agc file.


Commands:
	
# Setups up the editor
VisualEditor(Bool: load_all_media) returns VisualEditor instance

Setting load_all_media to True will load all the projects media at this point. 
Setting this to false will result in a scenes media loading when each scene is 
opened and deleted when the scene is closed. 

Example :
vis_editor = VisualEditor(True)


# Loads new scene
open_scene(int: scene_number)

The first scene is 0, second is 1 ect

Example:
vis_editor.open_scene(0)


#Get Sprite ID
get_entity_id(String: entity_name, int scene_number) returns int entity_id 

This command is use to get the entity id needed to be used in AppGameKit commands
Te entity returned is an integer id for a sprite, text, virtual button, editbox, or particles.
entity_name is the string name given to the entity within the AppGameKit Visual Editor.

Example:
sprite_id = vis_editor.get_entity_id("sprite 1", 0)

             
# Get Entity Type
kind = get_entity_kind(String: entity_name, int scene_number) returns int entity_kind

This command is use to get the kind of entity the entity is. The values can be returned 
are the following: Sprite, Text, Edit Box, Virtual Button and Particles

Example:
kind = vis_editor.get_entity_kind("sprite 1", 0)

