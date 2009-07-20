property_list_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "PropertyListBox",
    "output_package_name": "user_interface",
    "output_module_name": "property_list_box",

    "doc_html": """
        Displays a list of items and their values in a property-style list box dialog.
    """,

    "syntax_html": """
        Rhino.PropertyListBox (arrItems, arrValues [, strMessage [, strTitle]])
    """,

    "params_html": {
        0: {
            "name": "Items",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A zero-based, one-dimensional array of string items.
            """
        },
        1: {
            "name": "Values",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A zero-based, one-dimensional array of strings indicating the value of each item in the list.
            """
        },
        2: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        3: {
            "name": "Title",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A dialog box title.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A zero-based, one-dimensional array of strings indicating the new value of each item in the list."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 58,

    "params_com": {
        0: {
            "name": "vaList",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValues",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

