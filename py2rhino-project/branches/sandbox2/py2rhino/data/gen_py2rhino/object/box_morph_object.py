box_morph_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "BoxMorphObject",
    "output_package_name": "object",
    "output_module_name": "box_morph_object",

    "doc_html": """
        Morphs an object by mapping its eight bounding box points to eight new points. Note, this function only works on non-planar objects.
    """,

    "syntax_html": {
        0: ("strObject", "arrBoxPoints", "blnCopy"),
        1: ("arrObjects", "arrBoxPoints", "blnCopy"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to morph.
            """
        },
        1: {
            "name": "arrBoxPoints",
            "py_name": "box_points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "BoxPoints",
            "doc": """
        An array of eight 3-D points that contain the modified bounding box points.
            """
        },
        2: {
            "name": "blnCopy",
            "py_name": "copy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Copy",
            "doc": """
        Copy the object. If omitted, the object will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the morphed object if successful."
        },
        1: {
            "type": "array",
            "doc": "An array of strings identifying the morphed objects if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 918,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaCopy",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

