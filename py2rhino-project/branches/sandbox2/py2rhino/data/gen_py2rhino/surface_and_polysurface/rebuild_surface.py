rebuild_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "RebuildSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "rebuild_surface",

    "doc_html": """
        Rebuilds a surface to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    """,

    "syntax_html": """
        Rhino.RebuildSurface (strObject [, arrDegree [, arrPointCount]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Degree",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3 in each direction.
            """
        },
        2: {
            "name": "PointCount",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of two numbers that identify the surface point count in both the U and the V directions.  The point count must be greater than the degree.  The default value is 10 in each direction.
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

    "id_com": 816,

    "params_com": {
        0: {
            "name": "vaSrf",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPointCount",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

