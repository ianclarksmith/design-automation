add_sphere = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSphere",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_sphere",

    "doc_html": """
        Adds a spherical surface to the document.
    """,

    "syntax_html": {
        0: ("arrCenter", "dblRadius"),
        1: ("arrPlane", "dblRadius"),
    },

    "params_html": {
        0: {
            "name": "arrCenter",
            "py_name": "center",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Center",
            "doc": """
        The center point of the sphere.
            """
        },
        1: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Plane",
            "doc": """
        An equatorial plane.  The origin of the plane will be the center point of the sphere.
            """
        },
        2: {
            "name": "dblRadius",
            "py_name": "radius",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
            "doc": """
        The radius of the sphere in current model units.
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

    "id_com": 71,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

