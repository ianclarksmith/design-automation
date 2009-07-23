bounding_box = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "BoundingBox",
    "output_package_name": "geometry",
    "output_module_name": "bounding_box",

    "doc_html": """
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects.
    """,

    "syntax_html": {
        0: ("strObject", "strView", "blnWorldCoords"),
        1: ("arrObjects", "strView", "blnWorldCoords"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects.
            """
        },
        1: {
            "name": "strView",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
            """
        },
        2: {
            "name": "blnWorldCoords",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "WorldCoords",
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

