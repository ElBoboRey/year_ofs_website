import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode("div", "text", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_single_props(self):
        node = HTMLNode("abc", "text", None, {"abc" : "123"})
        self.assertEqual(node.props_to_html(), ' abc="123"')

    def test_multi_props(self):
        node = HTMLNode(
            "a", 
            "Click me", 
            None, 
            {"href": "https://example.com", "target": "_blank"}
        )
        
        result = node.props_to_html()
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertEqual(len(result.split()), 2)  

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_attributes(self):
        node = LeafNode("abc", "text", {"abc": "123"})
        self.assertEqual(node.to_html(), '<abc abc="123">text</abc>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "test sentence")
        self.assertEqual(node.to_html(), "test sentence")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()