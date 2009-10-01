#The data below will be used to generate the Rhinoscript function wrappers

#===============================================================================
# 
#===============================================================================
class block(object):    
    folder = "ent"

    class Functions(object):

        block_container_count = {
            "method_name": "container_count",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("number","null")
            }
        block_containers = {
            "method_name": "containers",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("array_of str","null")
            }
        block_count = {
            "method_name": "count",
            "method_parameters": (),
            "method_returns": ("number","null")
            }
        block_description = {
            "method_name": "description",
            "method_parameters": (("block_name","str","REQ"),("text","str","OPT")),
            "method_returns": ("str","null")
            }
        block_instance_count = {
            "method_name": "instance_count",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("number","null")
            }
        block_names = {
            "method_name": "names",
            "method_parameters": (("sort","bln","OPT"),),
            "method_returns": ("array_of str","null")
            }
        block_object_count = {
            "method_name": "object_count",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("number","null")
            }
        block_path = {
            "method_name": "path",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("str","null")
            }
        block_u_r_l = {
            "method_name": "url",
            "method_parameters": (("block_name","str","REQ"),("url","str","OPT")),
            "method_returns": ("str","null")
            }
        block_u_r_l_tag = {
            "method_name": "url_tag",
            "method_parameters": (("block_name","str","REQ"),("url","str","OPT")),
            "method_returns": ("str","null")
            }
        delete_block = {
            "method_name": "delete",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("bln","null")
            }
        is_block = {
            "method_name": "is_block",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("bln","null")
            }
        is_block_embedded = {
            "method_name": "is_embedded",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("bln","null")
            }
        is_block_in_use = {
            "method_name": "is_in_use",
            "method_parameters": (("block_name","str","REQ"),("where","int","OPT")),
            "method_returns": ("bln","null")
            }
        is_block_reference = {
            "method_name": "is_reference",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("bln","null")
            }
        rename_block = {
            "method_name": "rename",
            "method_parameters": (("old_block_name","str","REQ"),("new_block_name","str","REQ")),
            "method_returns": ("str","null")
            }
        block_objects = {
            "method_name": "objects",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("array_of str","null") #returns object identifiers - should be wrapped
            }
        
        
        #these return new instances - they are like constructors
        block_instances = {
            "method_name": "instances",
            "method_parameters": (("block_name","str","REQ"),),
            "method_returns": ("array_of str","null")#instance identifier
            } 
        insert_block = {
            "method_name": "insert",
            "method_parameters": (("block_name","str","REQ"),("insertion_point","array_of dbl","REQ"),("scale","array_of dbl","OPT"),("angle","dbl","OPT"),("normal","array_of dbl","OPT")),
            "method_returns": ("str","null") #instance identifier
            }
        insert_block_2 = {
            "method_name": "insert_by_xform",
            "method_parameters": (("block_name","str","REQ"),("xform","array_of dbl","REQ")),
            "method_returns": ("str","null") #instance identifier
            }
        
        
        
        block_instance_name = {#why object
            "method_name": "instance_name",
            "method_parameters": (("block_id","str","REQ"),),
            "method_returns": ("str","null")
            }
        explode_block_instance = {#why object
            "method_name": "explode_instance",
            "method_parameters": (("block_id","str","REQ"),),
            "method_returns": ("array_of str","null")
            }
        is_block_instance = {#this looks odd - what is this str
            "method_name": "is_instance",
            "method_parameters": (("block_id","str","REQ"),),
            "method_returns": ("bln","null")
            }
        block_instance_insert_point = {#why object
            "method_name": "instance_insert_point",
            "method_parameters": (("block_id","str","REQ"),),
            "method_returns": ("array_of str","null")
            }
        block_instance_xform = {#why object
            "method_name": "instance_xform",
            "method_parameters": (("block_id","str","REQ"),),
            "method_returns": ("array_of str","null")
            }