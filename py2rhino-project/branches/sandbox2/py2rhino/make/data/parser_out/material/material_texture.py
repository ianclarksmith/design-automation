material_texture = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialTexture",
    "output_package_name": "material",
    "output_module_name": "material_texture",

    "doc_html": """
        Returns or modifies a material's texture bitmap filename.
    """,

    "syntax_html": {
        0: ("intMaterialIndex", "strFileName"),
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
            "name": "strFileName",
            "py_name": "file_name",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "FileName",
            "doc": """
        The texture bitmap filename.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFileName is not specified, the current texture bitmap filename if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFileName is specified, the previous texture bitmap filename if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 182,

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

