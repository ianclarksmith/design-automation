osnap_mode = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "OsnapMode",
    "output_package_name": "application",
    "output_module_name": "osnap_mode",

    "doc_html": """
        Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects.
    """,

    "syntax_html": """
        Rhino.OsnapMode ([intMode])
    """,

    "params_html": {
        0: {
            "name": "Mode",
            "opt_or_req": "Optional",
            "type": "Number",
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

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intMode is not specified, then the current object snap mode or modes if successful."
        },
        1: {
            "type": "number",
            "doc": "If intMode is specified, then the previous object snap mode or modes if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 343,

    "params_com": {
        0: {
            "name": "vaModes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

