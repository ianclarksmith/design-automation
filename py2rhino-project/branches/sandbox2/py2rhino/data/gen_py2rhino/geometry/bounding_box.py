bounding_box = {
    "module_name": "geometry",
    "class_name": "Geometry",
    "method_name": "bounding_box",

    "doc_html": """
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.
    """,

    "syntax_html": """
        Rhino.BoundingBox (strObject [, strView [, blnWorldCoords]])
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
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects.
            """
        },
        2: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
            """
        },
        3: {
            "name": "WorldCoords",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Whether or not to return the bounding box as world coordinates or construction plane coordinates.  The default is to return world coordinates (True).  Note, this option does not apply to world axis-aligned bounding boxes.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 117,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaSystem",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

