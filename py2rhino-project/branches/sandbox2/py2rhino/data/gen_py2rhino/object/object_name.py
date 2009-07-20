object_name = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectName",
    "output_package_name": "object",
    "output_module_name": "object_name",

    "doc_html": """
        Returns or modifies the user-definable name of an object.
    """,

    "syntax_html": """
        Rhino.ObjectName (strObject [, strName])
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
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        2: {
            "name": "Name",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The new object name.  If omitted, the current object name is returned.  Note, if arrObjects is specified, strName is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If an object name is not specified,  the current object name if successful."
        },
        1: {
            "type": "string",
            "doc": "If an object name is specified,  the previous object name if successful."
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

    "id_com": 196,

    "params_com": {
        0: {
            "name": "vaObject",
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

