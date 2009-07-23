match_object_attributes = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "MatchObjectAttributes",
    "output_package_name": "object",
    "output_module_name": "match_object_attributes",

    "doc_html": """
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
    """,

    "syntax_html": {
        0: ("strTarget", "strSource"),
        1: ("arrTargets", "strSource"),
    },

    "params_html": {
        0: {
            "name": "arrTargets",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Targets",
            "doc": """
        An array of strings identifying the target objects.
            """
        },
        1: {
            "name": "strSource",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Source",
            "doc": """
        The identifier of the source object.  If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects whose attributes were modified if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 781,

    "params_com": {
        0: {
            "name": "vaTarget",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSource",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

