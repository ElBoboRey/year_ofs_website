class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        text = ""
        for key, value in self.props.items():
            text += f' {key}="{value}"'
        return text
    
    def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        html = f"<{self.tag}"
        if self.props:
            for prop_name, prop_value in self.props.items():
                html += f' {prop_name}="{prop_value}"'
        html += f">{self.value}</{self.tag}>"

        return html