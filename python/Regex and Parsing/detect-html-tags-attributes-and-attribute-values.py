from html.parser import HTMLParser


class Web(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        if attr:
            for item in attr:
                print("->", item[0], ">", item[1])


html_code = [input() for _ in range(int(input()))]

my_object = Web()
my_object.feed("".join(html_code))
