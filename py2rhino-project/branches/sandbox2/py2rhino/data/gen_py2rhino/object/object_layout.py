object_layout = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_layout",

    "doc_html": """
        Returns or changes the layout or model space of an object.
    """,

    "syntax_html": """
        Rhino.ObjectLayout (strObject [, strLayout [, blnReturnName]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Layout",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view. To move an object from page layout space to model space, just specify Null.
            """
        },
        2: {
            "name": "ReturnName",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

