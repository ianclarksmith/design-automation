add_srf_pt_grid = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSrfPtGrid",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_srf_pt_grid",

    "doc_html": """
        Creates a surface from a grid of points.
    """,

    "syntax_html": {
        0: ("arrCount", "arrPoints", "arrDegree", "arrClosed"),
    },

    "params_html": {
        0: {
            "name": "arrCount",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Count",
            "doc": """
        The number of points in the U and V directions.
            """
        },
        1: {
            "name": "arrPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points.
            """
        },
        2: {
            "name": "arrDegree",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Degree",
            "doc": """
        The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
            """
        },
        3: {
            "name": "arrClosed",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_bln",
            "name_main": "Closed",
            "doc": """
        Whether or not the surface is closed in the U and V directions.  If omitted, the new surface will not be closed in either the U or V directions.
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

    "id_com": 293,

    "params_com": {
        0: {
            "name": "vaCount",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaClosed",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

