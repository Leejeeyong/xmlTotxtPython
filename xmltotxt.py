from xml.etree import ElementTree
import glob

path = "./*"
file_list = glob.glob(path)
file_list_xml = [file for file in file_list if file.endswith(".xml")]

print ("file_list_xml: {}".format(file_list_xml))

for xmlfile in file_list_xml:

    tree = ElementTree.parse(xmlfile)
    iterElement1 = tree.iter(tag="object")
    for element1 in iterElement1:
        iterElement2 = element1.iter(tag = "bndbox")

        for element2 in iterElement2:
            print(xmlfile + " " + element2.find("xmin").text + " " + element2.find("ymin").text + " " + element2.find("xmax").text + " " + element2.find("ymax").text + ", " + element1.find("name").text)

            txt_fn = xmlfile[:-3] + 'txt'
            with open(txt_fn, 'w') as f:
                f.writelines(element2.find("xmin").text+ ", " +element2.find("ymin").text+ ", " +element2.find("xmax").text+ ", " +element2.find("ymax").text + ", " + element1.find("name").text)

