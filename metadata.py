from lxml.etree import Element, SubElement, QName, tostring
import json
from entityUtil import make as makeEntity
from relationUtil import make as makeRelation
from enumUtil import make as makeEnum

import os


class Metadata:
    def __init__(self, namespaces, entity, domain):
        super().__init__()
        self.namespaces = namespaces
        self.domain = domain
        self.entity = entity

    def outputfilename(self):
        return "./results/" + self.entity + "Metadata.xml"

    def entityconf(self):
        return "./entities/" + self.entity + ".json"

    def getRelationFiles(self):
        res = []
        for file in os.listdir("relations"):
            if file.lower().startswith(self.entity.lower()):
                res.append("./relations/" + file)
        return res

    def getEnumFiles(self):
        res = []
        for file in os.listdir("enumerations"):
            if file.lower().startswith(self.entity.lower()):
                res.append("./enumerations/" + file)
        return res

    def export(self):
        prefix = self.namespaces["metadata"]
        root = Element(QName(prefix, "metadata"),
                       nsmap=self.namespaces, domain=self.domain)
        complexTypeDescriptors = SubElement(
            root, QName(prefix, "complexTypeDescriptors"))
        entityDescriptors = SubElement(
            root, QName(prefix, "entityDescriptors"))
        makeEntity(entityDescriptors, prefix,
                   json.load(open(self.entityconf())))

        enumerationDescriptors = SubElement(
            root, QName(prefix, "enumerationDescriptors"))
        enums = self.getEnumFiles()
        if len(enums) > 0:
            for enum in enums:
                makeEnum(enumerationDescriptors, prefix, json.load(open(enum)))
        pathDescriptors = SubElement(root, QName(prefix, "pathDescriptors"))

        relationDescriptors = SubElement(
            root, QName(prefix, "relationDescriptors"))
        relations = self.getRelationFiles()
        if len(relations) > 0:
            for rel in relations:
                makeRelation(relationDescriptors, prefix, json.load(open(rel)))

        resourceDescriptors = SubElement(
            root, QName(prefix, "resourceDescriptors"))
        res = tostring(root, pretty_print=True,
                       xml_declaration=True, encoding='UTF-8', standalone=True)

        with open(self.outputfilename(), "wb") as output:
            output.write(res)

