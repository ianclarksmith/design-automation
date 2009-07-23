appearance_display = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AppearanceDisplay",
    "output_package_name": "application",
    "output_module_name": "appearance_display",

    "doc_html": """
        Returns or modifies an application interface item's visibility.
    """,

    "syntax_html": {
        0: ("intItem", "blnShow"),
    },

    "params_html": {
        0: {
            "name": "intItem",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Item",
            "doc": """
        Item number to either query or modify.  The available items are as follows:
		Value
		Description
		0
		Application menu
		1
		Command prompt
		2
		Status bar
		3
		View title bars
		4
		Application title bar
		5
		Full path in application title bar
		6
            """
        },
        1: {
            "name": "blnShow",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Show",
            "doc": """
        The new visibility state, either visible (True) or hidden (False).  If omitted, the current visibility state is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a blnShow is not specified, the current visibility state if successful."
        },
        1: {
            "type": "number",
            "doc": "If a blnShow is specified, the visibility state if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 752,

    "params_com": {
        0: {
            "name": "vaItem",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDisplay",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

