object_linetype = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectLinetype",
    "output_package_name": "object",
    "output_module_name": "object_linetype",

    "doc_html": """
        Returns or modifies the linetype of an object.
    """,

    "syntax_html": """
        Rhino.ObjectLinetype (strObject [, strLinetype])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        1: {
            "name": "Layer",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing linetype.  If omitted, the current object linetype is returned.  Note, if arrObjects is specified, strLinetype is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a linetype is not specified,  the object's current linetype if successful."
        },
        1: {
            "type": "number",
            "doc": "If a linetype is specified, the object's previous linetype if successful."
        },
        2: {
            "type": "number",
            "doc": "If arrObjects is specified, then the number of objects modified if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 646,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLinetype",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

