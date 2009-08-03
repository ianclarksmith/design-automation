#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

add_object_mesh = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "add_object_mesh",
    "method_parameters": (("object","str","REQ"),("quality","int","OPT"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
box_morph_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "box_morph_object",
    "method_parameters": (("objects","array_of str","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","array","null")
    }
copy_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "copy_object",
    "method_parameters": (("object","str","REQ"),("start","arr","OPT"),("end","arr","OPT")),
    "method_returns": ("string","null")
    }
copy_object_2 = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "copy_object_2",
    "method_parameters": (("object","str","REQ"),("translation","arr","OPT")),
    "method_returns": ("string","null")
    }
copy_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "copy_objects",
    "method_parameters": (("objects","array_of str","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
    "method_returns": ("array","null")
    }
copy_objects_2 = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "copy_objects_2",
    "method_parameters": (("translation","array_of dbl","OPT"),),
    "method_returns": ("array","null")
    }
delete_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "delete_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
delete_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "delete_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
enable_object_mesh = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "enable_object_mesh",
    "method_parameters": (("objects","array_of str","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
flash_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "flash_object",
    "method_parameters": (("objects","array_of str","REQ"),("style","bln","OPT")),
    "method_returns": ()
    }
hide_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "hide_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
hide_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "hide_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
is_layout_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_layout_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ()
    }
is_object_hidden = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_hidden",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_in_box = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_in_box",
    "method_parameters": (("object","str","REQ"),("box","array_of dbl","REQ"),("mode","bln","OPT")),
    "method_returns": ("null",)
    }
is_object_in_group = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_in_group",
    "method_parameters": (("object","str","REQ"),("group","str","OPT")),
    "method_returns": ("null",)
    }
is_object_locked = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_locked",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_normal = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_normal",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_reference = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_reference",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_selectable = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_selectable",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_selected = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_selected",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_solid = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_solid",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_object_valid = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_object_valid",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("null",)
    }
is_visible_in_view = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "is_visible_in_view",
    "method_parameters": (("object","str","REQ"),("view","str","OPT")),
    "method_returns": ("null",)
    }
lock_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "lock_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
lock_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "lock_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
match_object_attributes = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "match_object_attributes",
    "method_parameters": (("targets","array_of str","REQ"),("source","str","OPT")),
    "method_returns": ("number","null")
    }
mirror_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "mirror_object",
    "method_parameters": (("object","str","REQ"),("start_pt","arr","REQ"),("end_pt","arr","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
mirror_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "mirror_objects",
    "method_parameters": (("objects","array_of str","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
move_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "move_object",
    "method_parameters": (("object","str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "method_returns": ("boolean","null")
    }
move_object_2 = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "move_object_2",
    "method_parameters": (("object","str","REQ"),("translation","array_of dbl","REQ")),
    "method_returns": ("boolean","null")
    }
move_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "move_objects",
    "method_parameters": (("objects","array_of str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "method_returns": ("number","null")
    }
move_objects_2 = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "move_objects_2",
    "method_parameters": (("translation","array_of dbl","REQ"),),
    "method_returns": ("number","null")
    }
object_color = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_color",
    "method_parameters": (("objects","array_of str","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_color_source = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_color_source",
    "method_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_description = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_description",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("string","null")
    }
object_dump = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_dump",
    "method_parameters": (("object","str","REQ"),("type","int","OPT")),
    "method_returns": ("string","null")
    }
object_groups = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_groups",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("array","null")
    }
object_has_mesh = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_has_mesh",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
object_layer = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_layer",
    "method_parameters": (("objects","array_of str","REQ"),("layer","str","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_layout = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_layout",
    "method_parameters": (("object","str","REQ"),("layout","str","OPT"),("return_name","bln","OPT")),
    "method_returns": ("string","string","null")
    }
object_linetype = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_linetype",
    "method_parameters": (("objects","array_of str","REQ"),("layer","str","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_linetype_source = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_linetype_source",
    "method_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_material_index = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_material_index",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("number","null")
    }
object_material_source = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_material_source",
    "method_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_mesh_density = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_density",
    "method_parameters": (("object","str","REQ"),("density","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_angle = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_max_angle",
    "method_parameters": (("object","str","REQ"),("angle","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_aspect_ratio = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_max_aspect_ratio",
    "method_parameters": (("object","str","REQ"),("ratio","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_dist_edge_to_srf = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_max_dist_edge_to_srf",
    "method_parameters": (("object","str","REQ"),("distance","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_max_edge_length = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_max_edge_length",
    "method_parameters": (("object","str","REQ"),("length","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_min_edge_length = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_min_edge_length",
    "method_parameters": (("object","str","REQ"),("length","dbl","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_min_initial_grid_quads = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_min_initial_grid_quads",
    "method_parameters": (("object","str","REQ"),("quads","int","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_quality = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_quality",
    "method_parameters": (("object","str","REQ"),("quality","int","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_mesh_settings = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_mesh_settings",
    "method_parameters": (("object","str","REQ"),("settings","int","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
object_name = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_name",
    "method_parameters": (("objects","arr","REQ"),("name","str","OPT")),
    "method_returns": ("string","string","number","null")
    }
object_names = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_names",
    "method_parameters": (("objects","array_of str","REQ"),("names","array_of str","OPT")),
    "method_returns": ("array","array","null")
    }
object_print_color = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_print_color",
    "method_parameters": (("objects","array_of str","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_print_color_source = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_print_color_source",
    "method_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_print_width = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_print_width",
    "method_parameters": (("objects","array_of str","REQ"),("width","dbl","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_print_width_source = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_print_width_source",
    "method_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "method_returns": ("number","number","number","null")
    }
object_top_group = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_top_group",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("string","null")
    }
object_type = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_type",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("number","null")
    }
object_u_r_l = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "object_u_r_l",
    "method_parameters": (("objects","array_of str","REQ"),("u_r_l","str","OPT")),
    "method_returns": ("string","string","number","null")
    }
orient_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "orient_object",
    "method_parameters": (("object","str","REQ"),("reference","arr","REQ"),("target","arr","REQ"),("flags","int","OPT")),
    "method_returns": ("string","null")
    }
orient_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "orient_objects",
    "method_parameters": (("objects","array_of str","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
    "method_returns": ("array","null")
    }
remap_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "remap_object",
    "method_parameters": (("object","str","REQ"),("src_plane","arr","REQ"),("dst_plane","arr","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
remap_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "remap_objects",
    "method_parameters": (("object","array_of str","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    }
rotate_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "rotate_object",
    "method_parameters": (("object","str","REQ"),("point","arr","REQ"),("angle","dbl","REQ"),("axis","arr","OPT"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
rotate_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "rotate_objects",
    "method_parameters": (("objects","array_of str","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
scale_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "scale_object",
    "method_parameters": (("object","str","REQ"),("origin","arr","REQ"),("scale","arr","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
scale_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "scale_objects",
    "method_parameters": (("objects","array_of str","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    }
select_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "select_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
select_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "select_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
shear_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "shear_object",
    "method_parameters": (("object","str","REQ"),("origin","arr","REQ"),("ref_pt","arr","REQ"),("scale","arr","REQ"),("copy","bln","OPT")),
    "method_returns": ("string","null")
    }
shear_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "shear_objects",
    "method_parameters": (("objects","array_of str","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","array_of int","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    }
show_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "show_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
show_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "show_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
transform_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "transform_object",
    "method_parameters": (("object","str","REQ"),("matrix","arr","REQ"),("copy","bln","OPT")),
    "method_returns": ("boolean","null")
    }
transform_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "transform_objects",
    "method_parameters": (("objects","array_of str","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),
    "method_returns": ("array","null")
    }
unlock_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "unlock_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
unlock_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "unlock_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
unselect_object = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "unselect_object",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
unselect_objects = {
    "method_location": "Object",
    "method_type": "METHOD",
    "method_name": "unselect_objects",
    "method_parameters": (("objects","array_of str","REQ"),),
    "method_returns": ("number","null")
    }
