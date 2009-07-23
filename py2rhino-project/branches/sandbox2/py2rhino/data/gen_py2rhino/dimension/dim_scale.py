dim_scale = {
    "input_folder_name": "Dimension_Methods",
    "input_file_name": "DimScale",
    "output_package_name": "dimension",
    "output_module_name": "dim_scale",

    "doc_html": """
        Returns or changes the document's global dimension scale.
    """,

    "syntax_html": {
        0: ("dblScale"),
    },

    "params_html": {
        0: {
            "name": "dblScale",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Scale",
            "doc": """
        The new global dimension scale value.  If omitted, the current dimension scale will be returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a dimension scale is not specified, the current dimension scale if successful."
        },
        1: {
            "type": "number",
            "doc": "If a dimension scale is specified, the previous dimension scale if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 460,

    "params_com": {
        0: {
            "name": "vaScale",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

