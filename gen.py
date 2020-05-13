from lxml import etree
tree = etree.Element("root")
res = etree.tostring(tree, pretty_print = True, xml_declaration = True, encoding='UTF-8', standalone=True)

with open("file.xml","wb") as output:
    output.write(res)