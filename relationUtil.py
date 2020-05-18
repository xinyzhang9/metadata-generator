from lxml.etree import Element, SubElement, QName, tostring
def make(parent, prefix, params):
    relationDescriptor = SubElement(parent, QName(prefix, "relationDescriptor"))
    isSystem = SubElement(relationDescriptor, QName(prefix, "isSystem"));
    isSystem.text = params["isSystem"]

    localizedLabelKey = SubElement(relationDescriptor, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = params["localizedLabelKey"]

    name = SubElement(relationDescriptor, QName(prefix, "name"))
    name.text = params["name"]

    localizedOppositeLabelKey = SubElement(relationDescriptor, QName(prefix, "localizedOppositeLabelKey"))
    localizedOppositeLabelKey.text = params["localizedOppositeLabelKey"]

    cardinality = SubElement(relationDescriptor, QName(prefix, "cardinality"))
    cardinality.text = params["cardinality"]

    firstEndpointEntityName = SubElement(relationDescriptor, QName(prefix, "firstEndpointEntityName"))
    firstEndpointEntityName.text = params["firstEndpointEntityName"]

    nature = SubElement(relationDescriptor, QName(prefix, "nature"))
    nature.text = params["nature"]

    secondEndpointEntityName = SubElement(relationDescriptor, QName(prefix, "secondEndpointEntityName"))
    secondEndpointEntityName.text = params["secondEndpointEntityName"]


    tags = SubElement(relationDescriptor, QName(prefix, "tags"))
    if "tags" in params.keys():
        for t in params["tags"]:
            tag = SubElement(tags, QName(prefix, "tag"))
            tag.text = t
