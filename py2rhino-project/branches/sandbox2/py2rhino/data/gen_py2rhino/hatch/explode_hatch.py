explode_hatch = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "ExplodeHatch",
    "output_package_name": "hatch",
    "output_module_name": "explode_hatch",

    "doc_html": """
        Explodes a hatch object into its component objects. The exploded objects will be added to the document. If the hatch object uses a solid pattern, then planar face Brep objects will be created. Otherwise, line curve objects will be created.
    """,

    "syntax_html": """
        Rhino.ExplodeHatch (strObject [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Hatch",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an object.
            """
        },
        1: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete the hatch object. The default is to not delete the hatch object (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created objects if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 841,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

