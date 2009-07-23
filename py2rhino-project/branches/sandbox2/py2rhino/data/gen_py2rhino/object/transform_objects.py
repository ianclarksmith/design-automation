transform_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "TransformObjects",
    "output_package_name": "object",
    "output_module_name": "transform_objects",

    "doc_html": """
        Moves, scales, or rotates one or more objects given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
		1
		0
		0
		dX
		0
		1
		0
		dY
		0
		0
		1
		dZ
		0
		0
		0
		1
    """,

    "syntax_html": {
        0: ("arrObjects", "arrMatrix", "blnCopy"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to transform.
            """
        },
        1: {
            "name": "arrMatrix",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Matrix",
            "doc": """
        The transformation matrix (4x4 array of numbers).
            """
        },
        2: {
            "name": "blnCopy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Copy",
            "doc": """
        Copy the objects. If omitted, the objects will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly transformed objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 302,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaXform",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

