import xml.etree.ElementTree as et
tree = et.ElementTree(file = '/home/mona/Documents/Python/learnpython/menu.xml')
root = tree.getroot()
print root.tag

for child in root:
	print('tag:', child.tag, 'attributes:', child.attrib)
	for grandchild in child:
		print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
