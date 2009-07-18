appearance_color = {

    "class": "Application",
    "method": "appearance_color",
    "doc": """
        Returns or modifies an application interface item's color.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax": """
        Rhino.AppearanceColor (intItem [, lngColor])
    """,

    "params": {
        0: {
            "name": "item",
            "optional": False,
            "type_vb": "number",
            "type_string": "int",
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
            "name": "color",
            "optional": True,
            "type_vb": "number",
            "type_string": "lng",
            "doc": """
        The new color value.  If omitted, the current item color is returned.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "If a lngColor is not specified, the current item color if successful."
        },
        1: {
            "type_vb": "Number",
            "doc": "If a lngColor is specified, the previous item color if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

