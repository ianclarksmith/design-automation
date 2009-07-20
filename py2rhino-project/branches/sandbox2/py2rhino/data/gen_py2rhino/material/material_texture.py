material_texture = {
    "module_name": "material",
    "class_name": "Material",
    "method_name": "material_texture",

    "doc_html": """
        Returns or modifies a material's texture bitmap filename.
    """,

    "syntax_html": """
        Rhino.MaterialTexture (intMaterialIndex [, strFileName])
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

