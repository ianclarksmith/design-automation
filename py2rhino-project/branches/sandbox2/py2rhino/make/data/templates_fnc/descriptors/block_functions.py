#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

block_container_count = {
    "function_location": "block",
    "function_com_id": 411,
    "function_vb_name": "BlockContainerCount",
    "function_name": "block_container_count",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("number","null")
    }
block_containers = {
    "function_location": "block",
    "function_com_id": 412,
    "function_vb_name": "BlockContainers",
    "function_name": "block_containers",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("array","null")
    }
block_count = {
    "function_location": "block",
    "function_com_id": 397,
    "function_vb_name": "BlockCount",
    "function_name": "block_count",
    "function_parameters": (),
    "function_returns": ("number","null")
    }
block_description = {
    "function_location": "block",
    "function_com_id": 400,
    "function_vb_name": "BlockDescription",
    "function_name": "block_description",
    "function_parameters": (("block","str","REQ"),("text","str","OPT")),
    "function_returns": ("string","string","null")
    }
block_instance_count = {
    "function_location": "block",
    "function_com_id": 404,
    "function_vb_name": "BlockInstanceCount",
    "function_name": "block_instance_count",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("number","null")
    }
block_instance_insert_point = {
    "function_location": "block",
    "function_com_id": 413,
    "function_vb_name": "BlockInstanceInsertPoint",
    "function_name": "block_instance_insert_point",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
block_instance_name = {
    "function_location": "block",
    "function_com_id": 571,
    "function_vb_name": "BlockInstanceName",
    "function_name": "block_instance_name",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("string","null")
    }
block_instance_xform = {
    "function_location": "block",
    "function_com_id": 415,
    "function_vb_name": "BlockInstanceXform",
    "function_name": "block_instance_xform",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
block_instances = {
    "function_location": "block",
    "function_com_id": 414,
    "function_vb_name": "BlockInstances",
    "function_name": "block_instances",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("array","null")
    }
block_names = {
    "function_location": "block",
    "function_com_id": 396,
    "function_vb_name": "BlockNames",
    "function_name": "block_names",
    "function_parameters": (("sort","bln","OPT")),
    "function_returns": ("array","null")
    }
block_object_count = {
    "function_location": "block",
    "function_com_id": 416,
    "function_vb_name": "BlockObjectCount",
    "function_name": "block_object_count",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("number","null")
    }
block_objects = {
    "function_location": "block",
    "function_com_id": 417,
    "function_vb_name": "BlockObjects",
    "function_name": "block_objects",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("array","null")
    }
block_path = {
    "function_location": "block",
    "function_com_id": 408,
    "function_vb_name": "BlockPath",
    "function_name": "block_path",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("string","null")
    }
block_u_r_l = {
    "function_location": "block",
    "function_com_id": 402,
    "function_vb_name": "BlockURL",
    "function_name": "block_u_r_l",
    "function_parameters": (("block","str","REQ"),("u_r_l","str","OPT")),
    "function_returns": ("string","string","null")
    }
block_u_r_l_tag = {
    "function_location": "block",
    "function_com_id": 403,
    "function_vb_name": "BlockURLTag",
    "function_name": "block_u_r_l_tag",
    "function_parameters": (("block","str","REQ"),("u_r_l","str","OPT")),
    "function_returns": ("string","string","null")
    }
delete_block = {
    "function_location": "block",
    "function_com_id": 418,
    "function_vb_name": "DeleteBlock",
    "function_name": "delete_block",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("boolean","null")
    }
explode_block_instance = {
    "function_location": "block",
    "function_com_id": 419,
    "function_vb_name": "ExplodeBlockInstance",
    "function_name": "explode_block_instance",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("array","null")
    }
insert_block = {
    "function_location": "block",
    "function_com_id": 633,
    "function_vb_name": "InsertBlock",
    "function_name": "insert_block",
    "function_parameters": (("name","str","REQ"),("point","array_of dbl","REQ"),("scale","array_of int","OPT"),("angle","dbl","OPT"),("normal","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
insert_block_2 = {
    "function_location": "block",
    "function_com_id": 633,
    "function_vb_name": "InsertBlock",
    "function_name": "insert_block_2",
    "function_parameters": (("name","str","REQ"),("xform","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
is_block = {
    "function_location": "block",
    "function_com_id": 398,
    "function_vb_name": "IsBlock",
    "function_name": "is_block",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_block_embedded = {
    "function_location": "block",
    "function_com_id": 405,
    "function_vb_name": "IsBlockEmbedded",
    "function_name": "is_block_embedded",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_block_in_use = {
    "function_location": "block",
    "function_com_id": 406,
    "function_vb_name": "IsBlockInUse",
    "function_name": "is_block_in_use",
    "function_parameters": (("block","str","REQ"),("where","int","OPT")),
    "function_returns": ("boolean","null")
    }
is_block_instance = {
    "function_location": "block",
    "function_com_id": 420,
    "function_vb_name": "IsBlockInstance",
    "function_name": "is_block_instance",
    "function_parameters": (("object","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_block_reference = {
    "function_location": "block",
    "function_com_id": 407,
    "function_vb_name": "IsBlockReference",
    "function_name": "is_block_reference",
    "function_parameters": (("block","str","REQ")),
    "function_returns": ("boolean","null")
    }
rename_block = {
    "function_location": "block",
    "function_com_id": 399,
    "function_vb_name": "RenameBlock",
    "function_name": "rename_block",
    "function_parameters": (("old_block","str","REQ"),("new_block","str","REQ")),
    "function_returns": ("string","null")
    }
