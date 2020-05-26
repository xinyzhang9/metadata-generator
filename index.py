from metadata import Metadata

namespaces = {"metadata": "http://www.hp.com/maas/1.0.0/metadata"}

Metadata(namespaces, "Product", "sam").export()
Metadata(namespaces, "Vendor", "sam").export()
Metadata(namespaces, "LicenseMetric", "sam").export()
