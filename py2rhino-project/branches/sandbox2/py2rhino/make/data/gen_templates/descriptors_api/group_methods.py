#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

add_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "add_group",
    "method_parameters": (("group","str","OPT")),
    "method_returns": ("string","null")
    }
add_object_to_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "add_object_to_group",
    "method_parameters": (("object","str","REQ"),("group","str","REQ")),
    "method_returns": ("boolean","null")
    }
add_objects_to_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "add_objects_to_group",
    "method_parameters": (("objects","arr_of_str","REQ"),("group","str","REQ")),
    "method_returns": ("number","null")
    }
delete_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "delete_group",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("boolean","null")
    }
group_count = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "group_count",
    "method_parameters": (),
    "method_returns": ("number","null")
    }
group_names = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "group_names",
    "method_parameters": (),
    "method_returns": ("array","null")
    }
hide_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "hide_group",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("number","null")
    }
is_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "is_group",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_group_empty = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "is_group_empty",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("boolean","null")
    }
lock_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "lock_group",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("number","null")
    }
remove_object_from_all_groups = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "remove_object_from_all_groups",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
remove_object_from_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "remove_object_from_group",
    "method_parameters": (("object","str","REQ"),("group","str","REQ")),
    "method_returns": ("boolean","null")
    }
remove_object_from_top_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "remove_object_from_top_group",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
remove_objects_from_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "remove_objects_from_group",
    "method_parameters": (("objects","arr_of_str","REQ"),("group","str","REQ")),
    "method_returns": ("number","null")
    }
rename_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "rename_group",
    "method_parameters": (("old_group","str","REQ"),("new_group","str","REQ")),
    "method_returns": ("string","null")
    }
show_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "show_group",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("number","null")
    }
unlock_group = {
    "method_location": "Group",
    "method_type": "METHOD",
    "method_name": "unlock_group",
    "method_parameters": (("group","str","REQ")),
    "method_returns": ("number","null")
    }
