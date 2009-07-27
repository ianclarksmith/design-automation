read_file_version = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "ReadFileVersion",
    "output_package_name": "document",
    "output_module_name": "read_file_version",

    "doc_html": """
        Returns the file version of the current document.  Use this function to determine which version of Rhino last saved the document. Note, this function will not return values from referenced or merged files.
    """,

    "syntax_html": {
        0: (),
    },

    "params_html": {
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The file version of the document if successful.  Note, values less than zero indicate that the current document has not been read (from disk)."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 737,

    "params_com": {
    },

    "returns_com": "tagVARIANT",

}

