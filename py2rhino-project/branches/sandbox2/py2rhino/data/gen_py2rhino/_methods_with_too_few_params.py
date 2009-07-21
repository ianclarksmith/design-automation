#These methods have too few parameters when compared to the COM definition

application = {
},
block = {
    "block_instances": {
    	# The COM object lists the following parameters
    	# 0: vaName, Required
    	# 1: vaSelect, Optional
        "Block": 	("Required", "str"),
    },
},
curve = {
    "curve_mid_point": {
    	# The COM object lists the following parameters
    	# 0: vaObject, Required
    	# 1: vaIndex, Optional
        "Object": 	("Required", "str"),
    },
},
dimension = {
},
document = {
},
geometry = {
},
group = {
},
hatch = {
},
layer = {
},
light = {
},
line_and_plane = {
},
linetype = {
},
material = {
},
math = {
},
mesh = {
},
object = {
},
object_grip = {
},
point_and_vector = {
},
selection = {
},
surface_and_polysurface = {
},
transformation = {
},
user_data = {
},
user_interface = {
    "get_rectangle": {
    	# The COM object lists the following parameters
    	# 0: vaMode, Optional
    	# 1: vaPoint, Optional
    	# 2: vaPrompt1, Optional
    	# 3: vaPrompt2, Optional
    	# 4: vaPrompt3, Optional
    	# 5: vaPlane, Optional
        "Mode": 	("Optional", "int"),
        "Point": 	("Optional", "arr_of_???"),
        "Prompt1": 	("Optional", "str"),
        "Prompt2": 	("Optional", "str"),
        "Prompt3": 	("Optional", "str"),
    },
},
utility = {
    "color_h_l_s_to_r_g_b": {
    	# The COM object lists the following parameters
    	# 0: vaUpperBound, Required
    	# 1: vaValue, Optional
        "RGB": 	("Required", "lng"),
    },
},
view = {
    "wallpaper": {
    	# The COM object lists the following parameters
    	# 0: vaView, Optional
    	# 1: vaFileName, Optional
    	# 2: vaHidden, Optional
    	# 3: vaGrayscale, Optional
        "View": 	("Optional", "str"),
        "FileName": 	("Optional", "str"),
    },
},
