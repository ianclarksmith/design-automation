add_srf_control_pt_grid = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSrfControlPtGrid",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_srf_control_pt_grid",

    "doc_html": """
        Creates a surface from a grid of control points.
    """,

    "syntax_html": """
        Rhino.AddSrfControlPtGrid (arrCount, arrPoints [, arrDegree])
    """,

    "params_html": {
        0: {
            "name": "Count",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The number of control points in the U and V directions.
            """
        },
        1: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D control points.
            """
        },
        2: {
            "name": "Degree",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
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

    "id_com": 294,

    "params_com": {
        0: {
            "name": "vaCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

