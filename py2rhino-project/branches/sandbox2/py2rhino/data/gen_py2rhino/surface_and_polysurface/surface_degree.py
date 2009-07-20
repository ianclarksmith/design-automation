surface_degree = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceDegree",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_degree",

    "doc_html": """
        Returns the degree of a  surface object in the specified direction.
    """,

    "syntax_html": """
        Rhino.SurfaceDegree (strObject [, intDirection])
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
            "name": "Direction",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction, either 0 = U, or 1 = V, or 2 = Both.  Of omitted, both the degrees in the U and V directions are returned (2 = Both).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If intDirection is not specified, or intDirection is set to 2, then the degree in both the U and V directions is returned."
        },
        1: {
            "type": "number",
            "doc": "If intDirection is specified, and intDirection is set to either 0 or 1, then the degree in either the U or V direction is returned."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 216,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

