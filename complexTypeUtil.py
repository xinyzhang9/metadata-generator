from lxml.etree import Element, SubElement, QName, tostring

# complexType is amlost hard coded
def make(parent, prefix, entity):
    # first complexType
    calculatedFields = SubElement(parent, QName(prefix, "complexTypeDescriptor"))

    isSystem = SubElement(calculatedFields, QName(prefix, "isSystem"))
    isSystem.text = 'false'

    localizedLabelKey = SubElement(calculatedFields, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = 'CalculatedFields'

    name = SubElement(calculatedFields, QName(prefix, "name"))
    name.text = entity.capitalize()+'CalculatedFields'

    isVolatileComplexType = SubElement(calculatedFields, QName(prefix, "isVolatileComplexType"))
    isVolatileComplexType.text = 'false'


    # second complexType
    calculatedTmpFields = SubElement(parent, QName(prefix, "complexTypeDescriptor"))

    isSystem = SubElement(calculatedTmpFields, QName(prefix, "isSystem"))
    isSystem.text = 'false'

    localizedLabelKey = SubElement(calculatedTmpFields, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = 'CalculatedTmpFields'

    name = SubElement(calculatedTmpFields, QName(prefix, "name"))
    name.text = entity.capitalize()+'CalculatedTmpFields'

    isVolatileComplexType = SubElement(calculatedTmpFields, QName(prefix, "isVolatileComplexType"))
    isVolatileComplexType.text = 'false'







    