transform_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "TransformObject",
    "output_package_name": "object",
    "output_module_name": "transform_object",

    "doc_html": """
        Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
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

    "syntax_html": """
        Rhino.TransformObject (strObject, arrMatrix [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Matrix",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The transformation matrix (4x4 array of numbers).
            """
        },
        2: {
            "name": "Copy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Copy the object. If omitted, the object will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "The identifier of the transformed object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 272,

    "params_com": {
        0: {
            "name": "vaObject",
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

