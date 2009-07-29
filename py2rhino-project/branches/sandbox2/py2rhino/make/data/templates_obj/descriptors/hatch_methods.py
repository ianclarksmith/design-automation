#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# Hatch
#===============================================================================

#constructors

add_hatch = {
    "method_location": "_Object._OtherType.Hatch",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_hatch",
    "method_parameters": (("","self","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT"),),
    "method_returns": ("_Entity.Hatch","null")
    }
add_hatches = {
    "method_location": "_Object._OtherType.Hatch",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_hatches",
    "method_parameters": (("curves","array_of str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT"),),
    "method_returns": ("array_of _Entity.Hatch","null")
    }

#methods

explode_hatch = {
    "method_location": "_Object._OtherType.Hatch",
    "method_type": "METHOD",
    "method_name": "explode",
    "method_parameters": (("","self","REQ"),("delete","bln","OPT"),),
    "method_returns": ("array_of _Entity.Hatch","null")
    }
hatch_rotation = {
    "method_location": "_Object._OtherType.Hatch",
    "method_type": "METHOD",
    "method_name": "rotation",
    "method_parameters": (("","self","REQ"),("rotation","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
hatch_scale = {
    "method_location": "_Object._OtherType.Hatch",
    "method_type": "METHOD",
    "method_name": "scale",
    "method_parameters": (("","self","REQ"),("scale","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
#===============================================================================
# HatchPattern
#===============================================================================

#constructors

#methods

add_hatch_patterns = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_patterns",
    "method_parameters": (("","str","REQ"),("replace","bln","OPT"),),
    "method_returns": ("array_of string","null")
    }
current_hatch_pattern = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "current_hatch_pattern",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("string","string","null")
    }
hatch_pattern = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern",
    "method_parameters": (("object","str","REQ"),("hatch","str","OPT"),),
    "method_returns": ("string","string","null")
    }
hatch_pattern_count = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
hatch_pattern_description = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_description",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("string","null")
    }
hatch_pattern_fill_type = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_fill_type",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
hatch_pattern_names = {
    "method_location": "_Entity.Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_names",
    "method_parameters": (),
    "method_returns": ("array","null")
    }
#===============================================================================
# _Entity
#===============================================================================
is_hatch = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_hatch",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_hatch_pattern = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_hatch_pattern",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_hatch_pattern_current = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_hatch_pattern_current",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_hatch_pattern_reference = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_hatch_pattern_reference",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }