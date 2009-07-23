material_transparency = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialTransparency",
    "output_package_name": "material",
    "output_module_name": "material_transparency",

    "doc_html": """
        Returns or modifies a material's transparency value.
    """,

    "syntax_html": {
        0: ("intMaterialIndex", "dblTransparency"),
    },

    "params_html": {
        0: {
            "name": "intMaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "MaterialIndex",
            "doc": """
        The zero-based source material index.
            """
        },
        1: {
            "name": "dblTransparency",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Transparency",
            "doc": """
        The new transparency value.  A material's transparency value ranges from 0.0 to 1.0, with 0.0 being opaque and 1.0 being transparent.  If omitted, the current transparency value is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblTransparency is not specified, the current transparency value if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblTransparency is specified, the previous transparency value if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 183,

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

