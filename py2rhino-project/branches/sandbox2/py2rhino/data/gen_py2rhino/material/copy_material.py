copy_material = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "CopyMaterial",
    "output_package_name": "material",
    "output_module_name": "copy_material",

    "doc_html": """
        Copies the definition of a source material to a destination material.
    """,

    "syntax_html": {
        0: ("intSrcIndex", "intDstIndex"),
    },

    "params_html": {
        0: {
            "name": "intSrcIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "SrcIndex",
            "doc": """
        The index of the source material.
            """
        },
        1: {
            "name": "intDstIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "DstIndex",
            "doc": """
        The index of the destination material.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 812,

    "params_com": {
        0: {
            "name": "vaSrcIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDstIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

