zoom_bounding_box = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ZoomBoundingBox",
    "output_package_name": "view",
    "output_module_name": "zoom_bounding_box",

    "doc_html": """
        Zooms to the extents of a specified bounding box in the specified view, or in the active view.
    """,

    "syntax_html": """
        Rhino.ZoomBoundingBox (arrCorners [, strView [, blnAll]])
    """,

    "params_html": {
        0: {
            "name": "Corners",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.  Use BoundingBox to obtain the bounding box of objects.
            """
        },
        1: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        2: {
            "name": "All",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Zoom extents in all views.  If omitted, only the specified view is zoomed (False).
            """
        },
    },

    "returns_html": {
    },

    "id_com": 479,

    "params_com": {
        0: {
            "name": "vaCorners",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAll",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}
