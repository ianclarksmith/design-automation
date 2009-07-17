add_search_path = {

    "class": "Application",
    "method": "add_search_path",
    "doc": """
        Adds a new path to Rhino's search path list. Search path items can be added manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.
    """,

    "syntax": """
        Rhino.AddSearchPath (strFolder [, intIndex])
    """,

    "params": {
        0: {
            "name": "folder",
            "optional": False,
            "type_vb": "string",
            "type_string": "str",
            "doc": """
        A valid folder, or path, to add.
            """
        },
        1: {
            "name": "index",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
            "doc": """
        A zero-based position index in the search path list to insert the string. If omitted, the path will be appended to the end of the search path list.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "The zero-based index of the new search path item. If the index is less than zero, then the path item was not added to the search path list."
        },
        1: {
            "type_vb": "Null",
            "doc": "On error."
        },
    }

}

