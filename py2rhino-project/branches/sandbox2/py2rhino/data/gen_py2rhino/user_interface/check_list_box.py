check_list_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "CheckListBox",
    "output_package_name": "user_interface",
    "output_module_name": "check_list_box",

    "doc_html": """
        Displays a list of items in a checkable-style list box dialog.
    """,

    "syntax_html": {
        0: ("arrItems", "arrValues", "strMessage", "strTitle"),
    },

    "params_html": {
        0: {
            "name": "arrItems",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Items",
            "doc": """
        A zero-based, one-dimensional array of string items.
            """
        },
        1: {
            "name": "arrValues",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_bln",
            "name_main": "Values",
            "doc": """
        A zero-based, one-dimensional array of boolean values indicating the checked state of each item in the list.
            """
        },
        2: {
            "name": "strMessage",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        3: {
            "name": "strTitle",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Title",
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

