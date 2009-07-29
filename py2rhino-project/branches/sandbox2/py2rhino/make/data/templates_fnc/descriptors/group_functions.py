#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_group = {
    "function_location": "group",
    "function_com_id": 133,
    "function_vb_name": "AddGroup",
    "function_name": "add_group",
    "function_parameters": (("group","str","OPT"),),
    "function_returns": ("string","null")
    }
add_object_to_group = {
    "function_location": "group",
    "function_com_id": 134,
    "function_vb_name": "AddObjectToGroup",
    "function_name": "add_object_to_group",
    "function_parameters": (("object","str","REQ"),("group","str","REQ")),
    "function_returns": ("boolean","null")
    }
add_objects_to_group = {
    "function_location": "group",
    "function_com_id": 135,
    "function_vb_name": "AddObjectsToGroup",
    "function_name": "add_objects_to_group",
    "function_parameters": (("objects","array_of str","REQ"),("group","str","REQ")),
    "function_returns": ("number","null")
    }
delete_group = {
    "function_location": "group",
    "function_com_id": 136,
    "function_vb_name": "DeleteGroup",
    "function_name": "delete_group",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("boolean","null")
    }
group_count = {
    "function_location": "group",
    "function_com_id": 137,
    "function_vb_name": "GroupCount",
    "function_name": "group_count",
    "function_parameters": (),
    "function_returns": ("number","null")
    }
group_names = {
    "function_location": "group",
    "function_com_id": 138,
    "function_vb_name": "GroupNames",
    "function_name": "group_names",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
hide_group = {
    "function_location": "group",
    "function_com_id": 871,
    "function_vb_name": "HideGroup",
    "function_name": "hide_group",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("number","null")
    }
is_group = {
    "function_location": "group",
    "function_com_id": 139,
    "function_vb_name": "IsGroup",
    "function_name": "is_group",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_group_empty = {
    "function_location": "group",
    "function_com_id": 140,
    "function_vb_name": "IsGroupEmpty",
    "function_name": "is_group_empty",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("boolean","null")
    }
lock_group = {
    "function_location": "group",
    "function_com_id": 873,
    "function_vb_name": "LockGroup",
    "function_name": "lock_group",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("number","null")
    }
remove_object_from_all_groups = {
    "function_location": "group",
    "function_com_id": 141,
    "function_vb_name": "RemoveObjectFromAllGroups",
    "function_name": "remove_object_from_all_groups",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
remove_object_from_group = {
    "function_location": "group",
    "function_com_id": 142,
    "function_vb_name": "RemoveObjectFromGroup",
    "function_name": "remove_object_from_group",
    "function_parameters": (("object","str","REQ"),("group","str","REQ")),
    "function_returns": ("boolean","null")
    }
remove_object_from_top_group = {
    "function_location": "group",
    "function_com_id": 143,
    "function_vb_name": "RemoveObjectFromTopGroup",
    "function_name": "remove_object_from_top_group",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
remove_objects_from_group = {
    "function_location": "group",
    "function_com_id": 144,
    "function_vb_name": "RemoveObjectsFromGroup",
    "function_name": "remove_objects_from_group",
    "function_parameters": (("objects","array_of str","REQ"),("group","str","REQ")),
    "function_returns": ("number","null")
    }
rename_group = {
    "function_location": "group",
    "function_com_id": 145,
    "function_vb_name": "RenameGroup",
    "function_name": "rename_group",
    "function_parameters": (("old_group","str","REQ"),("new_group","str","REQ")),
    "function_returns": ("string","null")
    }
show_group = {
    "function_location": "group",
    "function_com_id": 872,
    "function_vb_name": "ShowGroup",
    "function_name": "show_group",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("number","null")
    }
unlock_group = {
    "function_location": "group",
    "function_com_id": 874,
    "function_vb_name": "UnlockGroup",
    "function_name": "unlock_group",
    "function_parameters": (("group","str","REQ"),),
    "function_returns": ("number","null")
    }
