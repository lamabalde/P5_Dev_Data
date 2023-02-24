# import json

# my_list = [1, 2, 3, "a", "b", "c"]

# with open("liste.json", "w") as f:
#     json.dump(my_list, f)

#     f.close()
import xml.etree.ElementTree as ET

root = ET.Element("liste1")

my_list = [1, 2, 3, "a", "b", "c"]

for item in my_list:
    element = ET.Element("item")
    element.text = str(item)
    root.append(element)

tree = ET.ElementTree(root)

with open("liste1.xml", "wb") as f:
    tree.write(f)

    f.close()

