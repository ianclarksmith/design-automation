#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# Group
#===============================================================================
add_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("_Object._OtherType.Group","null")
    }
delete_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "delete_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
group_count = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "group_count",
    "method_parameters": (),
    "method_returns": ("number","null")
    }
group_names = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "group_names",
    "method_parameters": (),
    "method_returns": ("array of str","null")
    }
hide_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "hide_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
lock_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "lock_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
rename_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "rename_group",
    "method_parameters": (("old_group","str","REQ"),("new_group","str","REQ"),),
    "method_returns": ("string","null")
    }
show_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "show_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
unlock_group = {#ed
    "method_location": "_Object._OtherType.Group",
    "method_type": "METHOD",
    "method_name": "unlock_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
#===============================================================================
# _OtherType
#===============================================================================
add_object_to_group = {#ed
    "method_location": "_Object._OtherType",
    "method_type": "METHOD",
    "method_name": "add_object_to_group",
    "method_parameters": (("","self","REQ"),("group","str","REQ"),),
    "method_returns": ("boolean","null")
    }
add_objects_to_group = {#ed
    "method_location": "_Object._OtherType",
    "method_type": "METHOD",
    "method_name": "add_objects_to_group",
    "method_parameters": (("objects","array of str","REQ"),("group","str","REQ"),),
    "method_returns": ("number","null")
    }
remove_object_from_all_groups = {#ed
    "method_location": "_Object._OtherType",
    "method_type": "METHOD",
    "method_name": "remove_object_from_all_groups",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
remove_object_from_group = {#ed
    "method_location": "_Object._OtherType",
    "method_type": "METHOD",
    "method_name": "remove_object_from_group",
    "method_parameters": (("","self","REQ"),("group","str","REQ"),),
    "method_returns": ("boolean","null")
    }
remove_object_from_top_group = {#ed
    "method_location": "_Object._OtherType",
    "method_type": "METHOD",
    "method_name": "remove_object_from_top_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
remove_objects_from_group = {#ed
    "method_location": "_Object._OtherType",
    "method_type": "METHOD",
    "method_name": "remove_objects_from_group",
    "method_parameters": (("objects","array of str","REQ"),("group","str","REQ"),),
    "method_returns": ("number","null")
    }
#===============================================================================
# _Object
#===============================================================================
is_group = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_group",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_group_empty = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_group_empty",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
