is_material_reference = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "IsMaterialReference",
    "output_package_name": "material",
    "output_module_name": "is_material_reference",

    "doc_html": """
        Verifies a material is referenced from another file.
    """,

    "syntax_html": {
        0: ("intMaterialIndex"),
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
        The zero-based material index.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 176,

    "params_com": {
        0: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

