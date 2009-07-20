add_box = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddBox",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_box",

    "doc_html": """
        Adds a new box-shaped polysurface to the document.
    """,

    "syntax_html": """
        Rhino.AddBox (arrCorners)
    """,

    "params_html": {
        0: {
            "name": "Corners",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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

