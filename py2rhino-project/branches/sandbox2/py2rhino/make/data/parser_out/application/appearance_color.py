appearance_color = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AppearanceColor",
    "output_package_name": "application",
    "output_module_name": "appearance_color",

    "doc_html": """
        Returns or modifies an application interface item's color.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": {
        0: ("intItem", "lngColor"),
    },

    "params_html": {
        0: {
            "name": "intItem",
            "py_name": "item",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Item",
            "doc": """
        Item number to either query or modify.  The available items are as follows:
		Value
		Description
		0
		View background
		1
		Major grid line
		2
		Minor grid line
		3
		X-axis line
		4
		Y-axis line
		5
		Selected objects
		6
		Locked objects
		7
		New layers
		8
		Feedback
		9
		Tracking
		10
		Crosshair
		11
		Text
		12
		Text background
		13
            """
        },
        1: {
            "name": "lngColor",
            "py_name": "color",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "lng",
            "name_main": "Color",
            "doc": """
        The new color value.  If omitted, the current item color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a lngColor is not specified, the current item color if successful."
        },
        1: {
            "type": "number",
            "doc": "If a lngColor is specified, the previous item color if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 335,

    "params_com": {
        0: {
            "name": "vaItem",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

