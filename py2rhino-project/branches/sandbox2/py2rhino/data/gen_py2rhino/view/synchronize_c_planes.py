synchronize_c_planes = {
    "module_name": "view",
    "class_name": "View",
    "method_name": "synchronize_c_planes",

    "doc_html": """
        Synchronizes all views and their construction plane to that of a specified view's construction plane.
		Normally, changing a view's construction plane is unique to that view.  This method changes the construction planes and normal views of all views to be of a right-angle orientation based on a specified view's construction plane.  This save the effort of changing all views independently, and maintains a standard right-angle view arrangement.
		The view synchronization only applies to Rhino's standard-named, parallel-projected views (e.g. Back, Bottom, Front, Left, Right, and Top).  All other views (e.g. Perspective, etc) simply have their construction plane synchronized to that of the specified view's construction plane.
    """,

    "syntax_html": """
        Rhino.SynchronizeCPlanes ([strView])
    """,

    "params_html": {
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 289,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

