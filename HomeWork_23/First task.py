import xml.etree.ElementTree as ET

class XMLProcessor:
    def __init__(self):
        self.xml_data = None

    def xml_to_string(self):
        if self.xml_data is not None:
            return ET.tostring(self.xml_data).decode('utf-8')
        else:
            return "XML data is not loaded."

    def string_to_xml(self, xml_string):
        try:
            self.xml_data = ET.fromstring(xml_string)
            return "XML successfully decoded from string."
        except ET.ParseError as e:
            return f"Error decoding XML from string: {e}"

    def perform_xml_operation(self, operation_func):
        if self.xml_data is not None:
            return operation_func(self.xml_data)
        else:
            return "XML data is not loaded."

# Приклад використання:
xml_processor = XMLProcessor()
xml_data_str = "<root><element>value</element></root>"
xml_processor.string_to_xml(xml_data_str)

# Перегляд XML у вигляді рядка
xml_string = xml_processor.xml_to_string()
print(f"XML as string: {xml_string}")

# Ваші власні операції з xml.etree.ElementTree тут
# Наприклад, знайдемо всі елементи з тегом 'element'
elements = xml_processor.perform_xml_operation(lambda xml_data: xml_data.findall('.//element'))
print(f"Found elements: {elements}")
