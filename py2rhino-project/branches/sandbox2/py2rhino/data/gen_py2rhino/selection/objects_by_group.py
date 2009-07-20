objects_by_group = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "ObjectsByGroup",
    "output_package_name": "selection",
    "output_module_name": "objects_by_group",

    "doc_html": """
        Returns the identifiers of all objects based on the objects' group name.
    """,

    "syntax_html": """
        Rhino.ObjectsByGroup (strGroup [, blnSelect])
    """,

    "params_html": {
        0: {
            "name": "Group",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of a group of objects.
            """
        },
        1: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the objects.  If omitted, the objects are not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 38,

    "params_com": {
        0: {
            "name": "vaGroup",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

