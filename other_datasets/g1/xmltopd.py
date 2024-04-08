import xml.etree.ElementTree as ET

def extract_dataframe(path: str) -> list[dict]:
    xtree = ET.parse(path)
    xroot = xtree.getroot()

    doc_list: list[dict] = []

    for i, child in enumerate(xroot):
        for subchild in child:
            if(subchild.tag == "item"):
                document: dict = {}
                
                for grandchild in subchild:
                    
                    if grandchild.tag == "description" and "<br />" in grandchild.text:
                        document[grandchild.tag] = grandchild.text.split("<br />  ")[1]
                    
                    else:
                        document[grandchild.tag] = grandchild.text
                    
                doc_list.append(document)
                
    return doc_list