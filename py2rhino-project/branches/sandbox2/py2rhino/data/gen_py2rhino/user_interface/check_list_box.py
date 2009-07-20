check_list_box = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "check_list_box",

    "doc_html": """
        Displays a list of items in a checkable-style list box dialog.
    """,

    "syntax_html": """
        Rhino.CheckListBox (arrItems, arrValues [, strMessage [, strTitle]])
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
        A zero-based, one-dimensional array of boolean values indicating the checked state of each item in the list.
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
            "doc": "A zero-based, one-dimensional array of boolean values indicating the new checked state of each item in the list."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 52,

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

