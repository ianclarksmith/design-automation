add_cone = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddCone",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_cone",

    "doc_html": """
        Adds a cone-shaped polysurface to the document.
    """,

    "syntax_html": {
        0: ("arrBase", "arrHeightPnt", "dblRadius", "blnCap"),
        1: ("arrPlane", "dblHeight", "dblRadius", "blnCap"),
    },

    "params_html": {
        0: {
            "name": "arrBase",
            "py_name": "base",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Base",
            "doc": """
        The 3-D origin point of the cone.
            """
        },
        1: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The cone's base plane.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
            """
        },
        2: {
            "name": "arrHeightPnt",
            "py_name": "height_pnt",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "HeightPnt",
            "doc": """
        The 3-D height point of the cone.  The height point defines the height and direction of the cone.
            """
        },
        3: {
            "name": "dblHeight",
            "py_name": "height",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Height",
            "doc": """
        The height of the cone.  If arrPlane is specified, then the center of the arrPlane is height * the plane's z-axis.
            """
        },
        4: {
            "name": "dblRadius",
            "py_name": "radius",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
            "doc": """
        The radius at the base of the cone.  Note, tan(cone_angle) = dblRadius/ dblHeight.
            """
        },
        5: {
            "name": "blnCap",
            "py_name": "cap",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Cap",
            "doc": """
        Cap the base of the cone.  The default is to cap the cone (True).
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

    "id_com": 75,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaHeight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCap",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

