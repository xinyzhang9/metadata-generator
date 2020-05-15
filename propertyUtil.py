from lxml.etree import Element, SubElement, QName, tostring
def make(parent, prefix, params):
    propertyDescriptor = SubElement(parent, QName(prefix, "propertyDescriptor"))
    isSystem = SubElement(propertyDescriptor, QName(prefix, "isSystem"));
    isSystem.text = params["isSystem"]

    localizedLabelKey = SubElement(propertyDescriptor, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = params["localizedLabelKey"]

    name = SubElement(propertyDescriptor, QName(prefix, "name"))
    name.text = params["name"]

    if "flavors" in params.keys():
        flavors = SubElement(propertyDescriptor, QName(prefix, "flavors"))
        for f in params["flavors"]:
            flavor = SubElement(flavors, QName(prefix, "flavor"))
            flavor.text = f

    isHidden = SubElement(propertyDescriptor, QName(prefix, "isHidden"))
    isHidden.text = params["isHidden"]

    isReadOnly = SubElement(propertyDescriptor, QName(prefix, "isReadOnly"))
    isReadOnly.text = params["isReadOnly"]

    isRequired = SubElement(propertyDescriptor, QName(prefix, "isRequired"))
    isRequired.text = params["isRequired"]

    isSearchable = SubElement(propertyDescriptor, QName(prefix, "isSearchable"))
    isSearchable.text = params["isSearchable"]

    isSortable = SubElement(propertyDescriptor, QName(prefix, "isSortable"))
    isSortable.text = params["isSortable"]

    isTextSearchable = SubElement(propertyDescriptor, QName(prefix, "isTextSearchable"))
    isTextSearchable.text = params["isTextSearchable"]

    isUnique = SubElement(propertyDescriptor, QName(prefix, "isUnique"))
    isUnique.text = params["isUnique"]

    logicalType = SubElement(propertyDescriptor, QName(prefix, "logicalTypelogicalType"))
    logicalType.text = params["logicalType"]

    if logicalType.text == "ENTITY_LINK":
        referenceName = SubElement(propertyDescriptor, QName(prefix, "referenceName"))
        referenceName.text = params["referenceName"]

    if "tags" in params.keys():
        flavors = SubElement(propertyDescriptor, QName(prefix, "tags"))
        for t in params["tags"]:
            tag = SubElement(flavors, QName(prefix, "tag"))
            tag.text = t

