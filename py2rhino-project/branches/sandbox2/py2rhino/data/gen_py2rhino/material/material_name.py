material_name = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialName",
    "output_package_name": "material",
    "output_module_name": "material_name",

    "doc_html": """
        Returns or modifies a material's user-definable name.
    """,

    "syntax_html": """
        Rhino.MaterialName (intMaterialIndex [, strName])
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
            "name": "Name",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new name.  If omitted, the current name is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strName is not specified, the current material name if successful."
        },
        1: {
            "type": "string",
            "doc": "If strName is specified, the previous material name if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 179,

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

