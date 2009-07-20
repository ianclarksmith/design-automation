text_object_plane = {
    "module_name": "geometry",
    "class_name": "Geometry",
    "method_name": "text_object_plane",

    "doc_html": """
        Returns or modifies the plane used by a text object.
    """,

    "syntax_html": """
        Rhino.TextObjectPlane(strObject [, arrPlane])
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
            "name": "Plane",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The new construction plane.  The elements of a plane array are as follows:
		Value
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If a plane is not specified, the current plane if successful."
        },
        1: {
            "type": "array",
            "doc": "If a plane is specified, the previous plane if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 476,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

