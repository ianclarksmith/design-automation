appearance_display = {

    "class": "Application",
    "method": "appearance_display",
    "doc": """
        Returns or modifies an application interface item's visibility.
    """,

    "syntax": """
        Rhino.AppearanceDisplay (intItem [, blnShow])
    """,

    "params": {
        0: {
            "name": "item",
            "optional": False,
            "type_vb": "number",
            "type_string": "int",
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
            "name": "show",
            "optional": True,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        The new visibility state, either visible (True) or hidden (False).  If omitted, the current visibility state is returned.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "If a blnShow is not specified, the current visibility state if successful."
        },
        1: {
            "type_vb": "Number",
            "doc": "If a blnShow is specified, the visibility state if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

