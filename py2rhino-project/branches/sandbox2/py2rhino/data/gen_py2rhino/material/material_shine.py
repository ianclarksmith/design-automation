material_shine = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialShine",
    "output_package_name": "material",
    "output_module_name": "material_shine",

    "doc_html": """
        Returns or modifies a material's shine value.
    """,

    "syntax_html": {
        0: ("intMaterialIndex", "dblShine"),
    },

    "params_html": {
        0: {
            "name": "intMaterialIndex",
            "py_name": "material_index",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "MaterialIndex",
            "doc": """
        The zero-based source material index.
            """
        },
        1: {
            "name": "dblShine",
            "py_name": "shine",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Shine",
            "doc": """
        The new shine value.  A material's shine value ranges from 0.0 to 255.0, with 0.0 being matte and 255.0 being glossy.  If omitted, the current shine value is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblShine is not specified, the current shine value if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblShine is specified, the previous shine value if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 181,

    "params_com": {
        0: {
            "name": "vaIndex",
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

