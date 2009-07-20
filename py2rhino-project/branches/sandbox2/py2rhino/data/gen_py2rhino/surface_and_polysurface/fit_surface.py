fit_surface = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "FitSurface",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "fit_surface",

    "doc_html": """
        Reduces the number of surface control points while maintaining the surfaces' same general shape.  Use this function for replacing surface with too many control points.  For more information, see the Rhino help file for the FitSrf command.
    """,

    "syntax_html": """
        Rhino.FitSurface (strObject [, arrDegree [, dblTolerance]])
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
        An array of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3.
            """
        },
        2: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
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

    "id_com": 815,

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
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

