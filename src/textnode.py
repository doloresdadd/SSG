from enum import Enum

class TextTypes(Enum):
    PLAIN_TEXT = "text(plain)"
    BOLD_TEXT = "**Bold Text**"
    ITALIC_TEXT = "_Italic Text_"
    CODE_TEXT = "`Code Text`"
    LINKS = "[Link Text](http://example.com)"
    IMAGES = "![Alt Text](http://example.com/image.jpg)"

class TextNode:
    def __init__(self, text_type: TextTypes, text: str):
        self.text_type = text_type
        self.text = text
        self.url = None

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return true if self.text == other.text && self.text_type == other.text_type && self.url == other.url else False 

    