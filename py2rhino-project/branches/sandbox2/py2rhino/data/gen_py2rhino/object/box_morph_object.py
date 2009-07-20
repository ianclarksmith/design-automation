box_morph_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "box_morph_object",

    "doc_html": """
        Morphs an object by mapping its eight bounding box points to eight new points. Note, this function only works on non-planar objects.
    """,

    "syntax_html": """
        Rhino.BoxMorphObject (strObject, arrBoxPoints [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to morph.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to morph.
            """
        },
        2: {
            "name": "BoxPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of eight 3-D points that contain the modified bounding box points.
            """
        },
        3: {
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

