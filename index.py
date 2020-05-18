from metadata import Metadata

namespaces = {"metadata" : "http://www.hp.com/maas/1.0.0/metadata"}

Metadata(namespaces,"product","sam").export()
Metadata(namespaces,"vendor","sam").export()