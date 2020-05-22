from lxml.etree import Element, SubElement, QName, tostring
def make(parent, prefix, params):
    enumerationDescriptor = SubElement(parent, QName(prefix, "enumerationDescriptor"))
    isSystem = SubElement(enumerationDescriptor, QName(prefix, "isSystem"));
    isSystem.text = params["isSystem"]

    localizedLabelKey = SubElement(enumerationDescriptor, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = params["localizedLabelKey"]

    name = SubElement(enumerationDescriptor, QName(prefix, "name"))
    name.text = params["name"]

    isVolatileEnumeration = SubElement(enumerationDescriptor, QName(prefix, "isVolatileEnumeration"))
    isVolatileEnumeration.text = params["isVolatileEnumeration"]

    values = SubElement(enumerationDescriptor, QName(prefix, "values"))
    if "values" in params.keys():
        for t in params["values"]:
            value = SubElement(values, QName(prefix, "value"))

            isSystem = SubElement(value, QName(prefix, "isSystem"))
            isSystem.text = t["isSystem"]

            localizedLabelKey = SubElement(value, QName(prefix, "localizedLabelKey"))
            localizedLabelKey.text = t["localizedLabelKey"]

            name = SubElement(value, QName(prefix, "name"))
            name.text = t["name"]

            order = SubElement(value, QName(prefix, "order"))
            order.text = t["order"]





