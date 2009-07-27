#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

block_container_count = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_container_count",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("number","null")
    }
block_containers = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_containers",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("array","null")
    }
block_count = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_count",
    "method_parameters": (),
    "method_returns": ("number","null")
    }
block_description = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_description",
    "method_parameters": (("block","str","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
block_instance_count = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_instance_count",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("number","null")
    }
block_instance_insert_point = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_instance_insert_point",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
block_instance_name = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_instance_name",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("string","null")
    }
block_instance_xform = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_instance_xform",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
block_instances = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_instances",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("array","null")
    }
block_names = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_names",
    "method_parameters": (("sort","bln","OPT")),
    "method_returns": ("array","null")
    }
block_object_count = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_object_count",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("number","null")
    }
block_objects = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_objects",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("array","null")
    }
block_path = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_path",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("string","null")
    }
block_u_r_l = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_u_r_l",
    "method_parameters": (("block","str","REQ"),("u_r_l","str","OPT")),
    "method_returns": ("string","string","null")
    }
block_u_r_l_tag = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "block_u_r_l_tag",
    "method_parameters": (("block","str","REQ"),("u_r_l","str","OPT")),
    "method_returns": ("string","string","null")
    }
delete_block = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "delete_block",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("boolean","null")
    }
explode_block_instance = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "explode_block_instance",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
insert_block = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "insert_block",
    "method_parameters": (("name","str","REQ"),("point","arr_of_dbl","REQ"),("scale","arr_of_int","OPT"),("angle","dbl","OPT"),("normal","arr_of_dbl","OPT"),("xform","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
is_block = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "is_block",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_block_embedded = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "is_block_embedded",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_block_in_use = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "is_block_in_use",
    "method_parameters": (("block","str","REQ"),("where","int","OPT")),
    "method_returns": ("boolean","null")
    }
is_block_instance = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "is_block_instance",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_block_reference = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "is_block_reference",
    "method_parameters": (("block","str","REQ")),
    "method_returns": ("boolean","null")
    }
rename_block = {
    "method_location": "Block",
    "method_type": "METHOD",
    "method_name": "rename_block",
    "method_parameters": (("old_block","str","REQ"),("new_block","str","REQ")),
    "method_returns": ("string","null")
    }
