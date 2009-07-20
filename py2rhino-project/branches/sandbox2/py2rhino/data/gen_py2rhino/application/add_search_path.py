add_search_path = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AddSearchPath",
    "output_package_name": "application",
    "output_module_name": "add_search_path",

    "doc_html": """
        Adds a new path to Rhino's search path list. Search path items can be added manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.
    """,

    "syntax_html": """
        Rhino.AddSearchPath (strFolder [, intIndex])
    """,

    "params_html": {
        0: {
            "name": "Folder",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A valid folder, or path, to add.
            """
        },
        1: {
            "name": "Index",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        A zero-based position index in the search path list to insert the string. If omitted, the path will be appended to the end of the search path list.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The zero-based index of the new search path item. If the index is less than zero, then the path item was not added to the search path list."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 511,

    "params_com": {
        0: {
            "name": "vaFolder",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

