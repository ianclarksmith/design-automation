add_srf_contour_crvs = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSrfContourCrvs",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_srf_contour_crvs",

    "doc_html": """
        Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.
    """,

    "syntax_html": """
        Rhino.AddSrfContourCrvs (strObject, arrStartPoint, arrEndPoint [, dblInterval])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a surface or polysurface object.
            """
        },
        1: {
            "name": "StartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D starting point of a center line.
            """
        },
        2: {
            "name": "EndPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D ending point of a center line.
            """
        },
        3: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A plane that defines the cutting plane.
            """
        },
        4: {
            "name": "Interval",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

