from lxml.etree import Element, SubElement, QName, tostring
import json
from entityUtil import make as makeEntity

class Metadata:
    def __init__(self, namespaces, domain):
        super().__init__()
        self.namespaces = namespaces
        self.domain = domain
        self.prefix = namespaces["metadata"]

    def export(self, file):
        prefix = self.prefix
        root = Element(QName(prefix,"metadata"), nsmap=self.namespaces, domain=self.domain)
        complexTypeDescriptors = SubElement(root, QName(prefix,"complexTypeDescriptors"))
        entityDescriptors = SubElement(root, QName(prefix,"entityDescriptors"))
        makeEntity(entityDescriptors, prefix, json.load(open("./entities/product.json")))
        enumerationDescriptors = SubElement(root, QName(prefix,"enumerationDescriptors"))
        pathDescriptors = SubElement(root, QName(prefix,"pathDescriptors"))
        relationDescriptors = SubElement(root, QName(prefix,"relationDescriptors"))
        resourceDescriptors = SubElement(root, QName(prefix,"resourceDescriptors"))
        res = tostring(root, pretty_print = True, xml_declaration = True, encoding='UTF-8', standalone=True)

        with open(file,"wb") as output:
            output.write(res)

