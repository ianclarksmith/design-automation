get_layer = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetLayer",
    "output_package_name": "user_interface",
    "output_module_name": "get_layer",

    "doc_html": """
        Displays a dialog box prompting the user to select a layer.
    """,

    "syntax_html": {
        0: ("strTitle", "strLayer", "blnShowNewLayer", "blnShowSetCurrent"),
    },

    "params_html": {
        0: {
            "name": "strTitle",
            "py_name": "title",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Title",
            "doc": """
        A dialog box title.
            """
        },
        1: {
            "name": "strLayer",
            "py_name": "layer",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layer",
            "doc": """
        The name of a layer to pre-select. If omitted, the current layer will be pre-selected.
            """
        },
        2: {
            "name": "blnShowNewLayer",
            "py_name": "show_new_layer",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ShowNewLayer",
            "doc": """
        Display the "New" layer button. If omitted, the button is not displayed.
            """
        },
        3: {
            "name": "blnShowSetCurrent",
            "py_name": "show_set_current",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ShowSetCurrent",
            "doc": """
        Display the "Set layer current" check box.  If omitted, the check box is not displayed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the selected layer if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 672,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLayer",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaNewButton",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCurrentButton",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

