```bash

```
```python

from lxml import etree
tree = etree.parse('updated_diagram.drawio')
root = tree.getroot()
root_element = root.xpath(".//root")[0]
root_element = root.find(".//root")	
#原始获mxCell列表,#可能存在多个用findall
nodes = root_element.findall(".//mxCell")
nodes = root_element.findall(".//object")
obj = nodes[0]
#注意object的结构
obj.get("id")
obj.find(".//mxCell").get
obj.find(".//mxCell").find("mxGeometry").get
obj.find(".//mxCell").find("mxGeometry").set("x","100")
with open("updated_diagram_with_modified_id.drawio", "wb") as files:
    files.write(etree.tostring(root, pretty_print=True))


```
```bash 
docker run -it --rm -p 8011:8080 jgraph/drawio 
```
