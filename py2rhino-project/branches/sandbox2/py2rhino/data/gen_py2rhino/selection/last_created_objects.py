last_created_objects = {
    "module_name": "selection",
    "class_name": "Selection",
    "method_name": "last_created_objects",

    "doc_html": """
        Returns the identifiers of the objects that were most recently created or changed by scripting a Rhino command using the Command function.  It is important to call this function immediately after calling the Command function as only the most recently created or changed object identifiers will be returned.
    """,

    "syntax_html": """
        Rhino.LastCreatedObjects ([blnSelect])
    """,

    "params_html": {
        0: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the object.  If omitted, the object is not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the most recently created or changed objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 485,

    "params_com": {
        0: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

