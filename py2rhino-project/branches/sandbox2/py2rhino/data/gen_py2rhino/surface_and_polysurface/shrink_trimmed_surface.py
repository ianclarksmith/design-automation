shrink_trimmed_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ShrinkTrimmedSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "shrink_trimmed_surface",

    "doc_html": """
        Shrinks the underlying untrimmed surfaces near to trimming boundaries. For more details, see the ShrinkTrimmedSrf command in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.ShrinkTrimmedSurface (strSurface)
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface or polysurface to shrink.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 700,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

