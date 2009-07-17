screen_size = {

    "class": "Application",
    "method": "screen_size",
    "doc": """
        Returns the current width and height, in pixels, of the screen of the primary display monitor.
    """,

    "syntax": """
        Rhino.ScreenSize ()
    """,

    "params": {
    },

    "returns": {
        0: {
            "type_vb": "Array",
            "doc": "A zero-based, one-dimensional array containing two numbers identifying the width and height if successful"
        },
        1: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}

