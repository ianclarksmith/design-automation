combo_list_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "ComboListBox",
    "output_package_name": "user_interface",
    "output_module_name": "combo_list_box",

    "doc_html": """
        Displays a list of items in a combo-style list box dialog.
    """,

    "syntax_html": {
        0: ("arrItems", "strMessage", "strTitle"),
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
            "name": "strMessage",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        2: {
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
            "type": "string",
            "doc": "The selected item if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 53,

    "params_com": {
        0: {
            "name": "vaList",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTitle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

