from lxml.etree import Element, SubElement, QName, tostring

namespaces = {
            "metadata" : "http://www.hp.com/maas/1.0.0/metadata"
        }
root = Element(QName(namespaces["metadata"],"metadata"), nsmap=namespaces, domain="dal")

res = tostring(root, pretty_print = True, xml_declaration = True, encoding='UTF-8', standalone=True)

with open("file.xml","wb") as output:
    output.write(res)