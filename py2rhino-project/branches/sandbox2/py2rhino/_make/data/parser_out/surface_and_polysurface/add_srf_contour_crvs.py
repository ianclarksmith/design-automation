add_srf_contour_crvs = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSrfContourCrvs",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_srf_contour_crvs",

    "doc_html": """
        Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.
    """,

    "syntax_html": {
        0: ("strObject", "arrStartPoint", "arrEndPoint", "dblInterval"),
        1: ("strObject", "arrPlane", "dblInterval"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a surface or polysurface object.
            """
        },
        1: {
            "name": "arrStartPoint",
            "py_name": "start_point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartPoint",
            "doc": """
        The 3-D starting point of a center line.
            """
        },
        2: {
            "name": "arrEndPoint",
            "py_name": "end_point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndPoint",
            "doc": """
        The 3-D ending point of a center line.
            """
        },
        3: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        A plane that defines the cutting plane.
            """
        },
        4: {
            "name": "dblInterval",
            "py_name": "interval",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Interval",
            "doc": """
        The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created contour curves if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 747,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "va0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "va1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "va2",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

