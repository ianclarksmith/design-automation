pull_curve = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "PullCurve",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "pull_curve",

    "doc_html": """
        Pulls a curve object to a surface object. For more information, see the Rhino help file for information on the Pull command.
    """,

    "syntax_html": """
        Rhino.PullCurve (strSurface, strCurve [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface object that pulls.
            """
        },
        1: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve object to pull.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete input curve.  If omitted, the input curve will not be deleted (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the new curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 493,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

