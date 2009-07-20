copy_material = {
    "module_name": "material",
    "class_name": "Material",
    "method_name": "copy_material",

    "doc_html": """
        Copies the definition of a source material to a destination material.
    """,

    "syntax_html": """
        Rhino.CopyMaterial (intSrcIndex, intDstIndex)
    """,

    "params_html": {
        0: {
            "name": "SrcIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The index of the source material.
            """
        },
        1: {
            "name": "DstIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
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

