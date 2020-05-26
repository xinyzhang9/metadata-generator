from lxml.etree import Element, SubElement, QName, tostring


def make(parent, prefix, params):
    propertyDescriptor = SubElement(
        parent, QName(prefix, "propertyDescriptor"))
    isSystem = SubElement(propertyDescriptor, QName(prefix, "isSystem"))
    isSystem.text = params["isSystem"]

    localizedLabelKey = SubElement(
        propertyDescriptor, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = params["localizedLabelKey"]

    name = SubElement(propertyDescriptor, QName(prefix, "name"))
    name.text = params["name"]

    flavors = SubElement(propertyDescriptor, QName(prefix, "flavors"))
    if "flavors" in params.keys():
        for f in params["flavors"]:
            flavor = SubElement(flavors, QName(prefix, "flavor"))
            flavor.text = f

    isHidden = SubElement(propertyDescriptor, QName(prefix, "isHidden"))
    isHidden.text = params["isHidden"]

    isReadOnly = SubElement(propertyDescriptor, QName(prefix, "isReadOnly"))
    isReadOnly.text = params["isReadOnly"]

    isRequired = SubElement(propertyDescriptor, QName(prefix, "isRequired"))
    isRequired.text = params["isRequired"]

    isSearchable = SubElement(
        propertyDescriptor, QName(prefix, "isSearchable"))
    isSearchable.text = params["isSearchable"]

    isSortable = SubElement(propertyDescriptor, QName(prefix, "isSortable"))
    isSortable.text = params["isSortable"]

    isTextSearchable = SubElement(
        propertyDescriptor, QName(prefix, "isTextSearchable"))
    isTextSearchable.text = params["isTextSearchable"]

    isUnique = SubElement(propertyDescriptor, QName(prefix, "isUnique"))
    isUnique.text = params["isUnique"]

    if "searchEngineAlias" in params.keys():
        searchEngineAlias = SubElement(
            propertyDescriptor, QName(prefix, "searchEngineAlias"))
        searchEngineAlias = params = ["searchEngineAliass"]

    logicalType = SubElement(propertyDescriptor, QName(prefix, "logicalType"))
    logicalType.text = params["logicalType"]

    if logicalType.text == "ENTITY_LINK" or logicalType.text == "ENUM":
        referenceName = SubElement(
            propertyDescriptor, QName(prefix, "referenceName"))
        referenceName.text = params["referenceName"]

    tags = SubElement(propertyDescriptor, QName(prefix, "tags"))
    if "tags" in params.keys():
        for t in params["tags"]:
            tag = SubElement(tags, QName(prefix, "tag"))
            tag.text = t
