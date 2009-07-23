material_environment_map = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialEnvironmentMap",
    "output_package_name": "material",
    "output_module_name": "material_environment_map",

    "doc_html": """
        Returns or modifies a material's environment bitmap filename.
    """,

    "syntax_html": {
        0: ("intMaterialIndex", "strFileName"),
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
            "name": "strFileName",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "FileName",
            "doc": """
        The environment bitmap filename.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFileName is not specified, the current environment bitmap filename if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFileName is specified, the previous environment bitmap filename if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 754,

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

