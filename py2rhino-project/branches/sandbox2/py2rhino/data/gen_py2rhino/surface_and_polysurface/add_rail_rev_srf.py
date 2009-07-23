add_rail_rev_srf = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddRailRevSrf",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_rail_rev_srf",

    "doc_html": """
        Create a surface by revolving a profile curve along a rail curve.
    """,

    "syntax_html": {
        0: ("strProfile", "strRail", "arrAxis"),
    },

    "params_html": {
        0: {
            "name": "strProfile",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Profile",
            "doc": """
        The identifier of the profile curve.
            """
        },
        1: {
            "name": "strRail",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Rail",
            "doc": """
        The identifier of the rail curve.
            """
        },
        2: {
            "name": "arrAxis",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Axis",
            "doc": """
        An array of two 3-D points identifying the start point and end point of the rail revolve axis.
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

    "id_com": 536,

    "params_com": {
        0: {
            "name": "vaProfile",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRail",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAxis",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

