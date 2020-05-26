from lxml.etree import Element, SubElement, QName, tostring
import json
from propertyUtil import make as makeProperty

fieldDir = "./properties/"


def conf(subdir, name):
    return fieldDir + subdir + '/' + name + '.json'


def make(parent, prefix, params):
    entityDescriptor = SubElement(parent, QName(prefix, "entityDescriptor"))
    isSystem = SubElement(entityDescriptor, QName(prefix, "isSystem"))
    isSystem.text = params["isSystem"]

    localizedLabelKey = SubElement(
        entityDescriptor, QName(prefix, "localizedLabelKey"))
    localizedLabelKey.text = params["localizedLabelKey"]

    name = SubElement(entityDescriptor, QName(prefix, "name"))
    name.text = params["name"]

    propertyDescriptors = SubElement(
        entityDescriptor, QName(prefix, "propertyDescriptors"))
    # make properties here
    for prop in params["properties"]:
        makeProperty(propertyDescriptors, prefix, json.load(
            open(conf(name.text.lower(), prop))))

    # ...
    if "tags" in params.keys():
        flavors = SubElement(parent, QName(prefix, "tags"))
        for t in params["tags"]:
            tag = SubElement(flavors, QName(prefix, "tag"))
            tag.text = t
