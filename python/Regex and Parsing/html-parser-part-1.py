from html.parser import HTMLParser

n = int(input())


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print("Start :", tag)
        for element in attributes:
            print("->", element[0], ">", element[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attributes):
        print("Empty :", tag)
        for element in attributes:
            print("->", element[0], ">", element[1])


Parser = MyHTMLParser()
Parser.feed("".join([input().strip() for _ in range(n)]))
