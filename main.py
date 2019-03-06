import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom
import pydot
import os
import xml.etree.ElementTree as ET



graph = {}

path = '/home/shunya/setool/xmls/bb'
path2 = './'
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    DOMtree =xml.dom.minidom.parse(fullname)
    collection = DOMtree.documentElement
    compound_name = collection.getElementsByTagName('compoundname')
    nodes= collection.getElementsByTagName('label')
    temp_lst =[]
    for node in nodes:
     temp_lst.append(str(node.childNodes[0].data))
    graph[compound_name[0].childNodes[0].data] = temp_lst
print(graph)
print("-------------------------------------------------------------------------------------------------\n")




for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    DOMtree =xml.dom.minidom.parse(fullname)
    collection = DOMtree.documentElement
    compound_name = collection.getElementsByTagName('compoundname')
    includes = collection.getElementsByTagName('includes')
    temp_lst =[]
    for include in includes:
     temp_lst.append(str(include.childNodes[0].data))
    graph[compound_name[0].childNodes[0].data] = temp_lst
print(graph)







g = pydot.Dot(graph_type = "graph" )

for node,neighbours in graph.items():
    gnode = pydot.Node(str(node),style = "filled",fillcolor = "yellow")
    g.add_node(gnode)
    for neighbour in neighbours:
        gedge = pydot.Edge(str(neighbour),gnode)
        g.add_edge(gedge)
im = g.write_png('tst2.png',prog = 'dot')
print("-------------------------------------------------------------------------------\n")
graph = {}

for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    DOMtree =xml.dom.minidom.parse(fullname)
    tree = ET.parse(fullname)
    root = tree.getroot()
    compound_name2 = root.findall('compounddef')
    print(compound_name2[0].find('compoundname').text)
    members2 = root.iter('memberdef')
    for member in members2:
        if member.get('kind') == 'define':
            print('d : ',member.find('name').text)
        else:
            print('f : ',member.find('name').text)
    collection = DOMtree.documentElement
    compound_name = collection.getElementsByTagName('coumpundname')
    members= collection.getElementsByTagName('memberdef')
    temp_lst =[]












class compund(xml.sax.ContentHandler):
     def __init__(self):
         self.CurrentData = ""
         self.include = ""
     def startElement(self,tag,attributes):
         self.CurrentData = tag
     def endElement(self,tag):
         if self.CurrentData == "includes":
             print ("Include : ",self.include)
      #
if (__name__ == "main"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    Handler = compound()
    parser.setContentHandler(Handler)

    parser.parse("bluray_8c.xml")
