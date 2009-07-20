add_text = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddText",
    "output_package_name": "geometry",
    "output_module_name": "add_text",

    "doc_html": """
        Adds a text string to the document.
    """,

    "syntax_html": """
        Rhino.AddText (strText, arrPoint [, dblHeight [, strFont [, intStyle]]])
    """,

    "params_html": {
        0: {
            "name": "Text",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The text to display.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point.
            """
        },
        2: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane on which the text will lie.  The origin of the plane will be the origin point of the text.
            """
        },
        3: {
            "name": "Height",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The text height.  If omitted, a height of 1.0 units is used.
            """
        },
        4: {
            "name": "Font",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The text font.  If omitted, the Arial font is used.
            """
        },
        5: {
            "name": "Style",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The font style.  If omitted, a normal font style (0) is used.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal
		1
		Bold
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 76,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaHeight",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaFont",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

