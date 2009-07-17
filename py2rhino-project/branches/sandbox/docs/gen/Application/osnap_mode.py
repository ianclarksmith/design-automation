osnap_mode = {

    "class": "Application",
    "method": "osnap_mode",
    "doc": """
        Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects.
    """,

    "syntax": """
        Rhino.OsnapMode ([intMode])
    """,

    "params": {
        0: {
            "name": "mode",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
            "doc": """
        The object snap mode or modes to set.  Object snap modes can be added together to set multiple modes.
		Value
		Description
		0
		None
		1
		Near
		2
		Focus
		4
		Center
		8
		Knot
		16
		Quadrant
		32
		Midpoint
		64
		Intersection
		128
		End
		256
		Perpendicular
		512
		Tangent
		1024
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "If intMode is not specified, then the current object snap mode or modes if successful."
        },
        1: {
            "type_vb": "Number",
            "doc": "If intMode is specified, then the previous object snap mode or modes if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

