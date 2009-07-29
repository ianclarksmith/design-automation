#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

attribute_data_count = {
    "function_location": "user_data",
    "function_com_id": 685,
    "function_vb_name": "AttributeDataCount",
    "function_name": "attribute_data_count",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
delete_attribute_data = {
    "function_location": "user_data",
    "function_com_id": 684,
    "function_vb_name": "DeleteAttributeData",
    "function_name": "delete_attribute_data",
    "function_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("boolean","null")
    }
delete_document_data = {
    "function_location": "user_data",
    "function_com_id": 237,
    "function_vb_name": "DeleteDocumentData",
    "function_name": "delete_document_data",
    "function_parameters": (("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("boolean","null")
    }
delete_object_data = {
    "function_location": "user_data",
    "function_com_id": 238,
    "function_vb_name": "DeleteObjectData",
    "function_name": "delete_object_data",
    "function_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("boolean","null")
    }
document_data_count = {
    "function_location": "user_data",
    "function_com_id": 239,
    "function_vb_name": "DocumentDataCount",
    "function_name": "document_data_count",
    "function_parameters": (),
    "function_returns": ("number",)
    }
get_attribute_data = {
    "function_location": "user_data",
    "function_com_id": 682,
    "function_vb_name": "GetAttributeData",
    "function_name": "get_attribute_data",
    "function_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("array","array","string","null")
    }
get_document_data = {
    "function_location": "user_data",
    "function_com_id": 240,
    "function_vb_name": "GetDocumentData",
    "function_name": "get_document_data",
    "function_parameters": (("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("array","array","string","null")
    }
get_object_data = {
    "function_location": "user_data",
    "function_com_id": 241,
    "function_vb_name": "GetObjectData",
    "function_name": "get_object_data",
    "function_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("array","array","string","null")
    }
get_user_text = {
    "function_location": "user_data",
    "function_com_id": 729,
    "function_vb_name": "GetUserText",
    "function_name": "get_user_text",
    "function_parameters": (("object","str","REQ"),("key","str","OPT"),("attach_to_geometry","bln","OPT")),
    "function_returns": ("string","array","null")
    }
is_attribute_data = {
    "function_location": "user_data",
    "function_com_id": 686,
    "function_vb_name": "IsAttributeData",
    "function_name": "is_attribute_data",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_document_data = {
    "function_location": "user_data",
    "function_com_id": 278,
    "function_vb_name": "IsDocumentData",
    "function_name": "is_document_data",
    "function_parameters": (),
    "function_returns": ("boolean",)
    }
is_object_data = {
    "function_location": "user_data",
    "function_com_id": 279,
    "function_vb_name": "IsObjectData",
    "function_name": "is_object_data",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_user_text = {
    "function_location": "user_data",
    "function_com_id": 730,
    "function_vb_name": "IsUserText",
    "function_name": "is_user_text",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
object_data_count = {
    "function_location": "user_data",
    "function_com_id": 242,
    "function_vb_name": "ObjectDataCount",
    "function_name": "object_data_count",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
set_attribute_data = {
    "function_location": "user_data",
    "function_com_id": 683,
    "function_vb_name": "SetAttributeData",
    "function_name": "set_attribute_data",
    "function_parameters": (("object","str","REQ"),("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
    "function_returns": ("string","null")
    }
set_document_data = {
    "function_location": "user_data",
    "function_com_id": 243,
    "function_vb_name": "SetDocumentData",
    "function_name": "set_document_data",
    "function_parameters": (("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
    "function_returns": ("string","null")
    }
set_object_data = {
    "function_location": "user_data",
    "function_com_id": 244,
    "function_vb_name": "SetObjectData",
    "function_name": "set_object_data",
    "function_parameters": (("object","str","REQ"),("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
    "function_returns": ("string","null")
    }
set_user_text = {
    "function_location": "user_data",
    "function_com_id": 728,
    "function_vb_name": "SetUserText",
    "function_name": "set_user_text",
    "function_parameters": (("object","str","REQ"),("key","str","REQ"),("value","str","OPT"),("attach_to_geometry","bln","OPT")),
    "function_returns": ("boolean","null")
    }
