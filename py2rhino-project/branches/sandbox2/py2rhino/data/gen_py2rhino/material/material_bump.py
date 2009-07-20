material_bump = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialBump",
    "output_package_name": "material",
    "output_module_name": "material_bump",

    "doc_html": """
        Returns or modifies a material's bump bitmap filename.
    """,

    "syntax_html": """
        Rhino.MaterialBump (intMaterialIndex [, strFileName])
    """,

    "params_html": {
        0: {
            "name": "MaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based source material index.
            """
        },
        1: {
            "name": "FileName",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The bump bitmap filename.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strFileName is not specified, the current bump bitmap filename if successful."
        },
        1: {
            "type": "string",
            "doc": "If strFileName is specified, the previous bump bitmap filename if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 177,

    "params_com": {
        0: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBump",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

