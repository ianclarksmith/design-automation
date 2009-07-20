is_material_default = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "IsMaterialDefault",
    "output_package_name": "material",
    "output_module_name": "is_material_default",

    "doc_html": """
        Verifies that a material is a copy of Rhino's built-in "default" material.  The default material is used by objects and layers that have not been assigned a material.
    """,

    "syntax_html": """
        Rhino.IsMaterialDefault (intMaterialIndex)
    """,

    "params_html": {
        0: {
            "name": "MaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based material index.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 175,

    "params_com": {
        0: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

