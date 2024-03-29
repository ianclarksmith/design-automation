add_box = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddBox",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_box",

    "doc_html": """
        Adds a new box-shaped polysurface to the document.
    """,

    "syntax_html": {
        0: ("arrCorners"),
    },

    "params_html": {
        0: {
            "name": "arrCorners",
            "py_name": "corners",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Corners",
            "doc": """
        An array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
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

    "id_com": 72,

    "params_com": {
        0: {
            "name": "vaCorners",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

