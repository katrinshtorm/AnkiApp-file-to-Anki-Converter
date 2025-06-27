import xml.etree.ElementTree as ET
import re

def extract_text_from_richtext(elem):
    text_parts = []
    for part in elem.iter():
        if part.text:
            text_parts.append(part.text.strip())
    return ' / '.join(filter(None, text_parts))

tree = ET.parse('ankiapp_export.xml')  # Replace with your XML file name if it’s different
root = tree.getroot()

with open('anki_import.txt', 'w', encoding='utf-8') as f:
    for card in root.findall('.//card'):
        front_elem = card.find(".//rich-text[@name='Front']")
        back_elem = card.find(".//rich-text[@name='Back']")
        front = extract_text_from_richtext(front_elem)
        back = extract_text_from_richtext(back_elem)
        f.write(f"{front}\t{back}\n")  
