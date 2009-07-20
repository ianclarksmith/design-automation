osnap = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "osnap",

    "doc_html": """
        Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.
    """,

    "syntax_html": """
        Rhino.Osnap ([blnEnable])
    """,

    "params_html": {
        0: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The new enabled status, either True or False.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnEnable is not specified, then the current object snap status if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnEnable is specified, then the previous object snap status if successful."
        },
    },

    "id_com": 347,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

