from textnode import TextNode, TextTypes 


def main():
    node1 = TextNode("This is plain text.", TextTypes.PLAIN_TEXT)
    node2 = TextNode(TextTypes.LINKS, "This is a link.", "boot.dev")
    print(node1)
    print(node2)

if __name__ == "__main__":
    main()