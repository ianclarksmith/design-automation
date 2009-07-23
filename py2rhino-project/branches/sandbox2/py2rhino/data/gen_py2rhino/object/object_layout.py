object_layout = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectLayout",
    "output_package_name": "object",
    "output_module_name": "object_layout",

    "doc_html": """
        Returns or changes the layout or model space of an object.
    """,

    "syntax_html": {
        0: ("strObject", "strLayout", "blnReturnName"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "strLayout",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layout",
            "doc": """
        To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view. To move an object from page layout space to model space, just specify Null.
            """
        },
        2: {
            "name": "blnReturnName",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnName",
            "doc": """
        If True (default), then the name, or title, of the page layout view is returned. If False, then the identifier of the page layout view is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strLayout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned."
        },
        1: {
            "type": "string",
            "doc": "If strLayout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 924,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLayout",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

