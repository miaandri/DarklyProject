import sys
import urllib.request
from html.parser import HTMLParser

array = []


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    self.links.append(value)


def check_readme(url):
    try:
        req = urllib.request.urlopen(url)
        html = req.read().decode("utf-8", errors="ignore")

        parser = LinkParser()
        parser.feed(html)

        for link in parser.links:
            if link == "README":
                try:
                    f = urllib.request.urlopen(url + "/" + link)
                    myfile = f.read()

                    if myfile not in array:
                        array.append(myfile)
                        print(myfile.decode("utf-8", errors="ignore"))

                except Exception as e:
                    print("Error reading README:", e)

                break

            elif link != "../":
                check_readme(url + "/" + link)

    except Exception as e:
        print("Error accessing", url, ":", e)


def main(arg):
    url = "http://" + arg + "/.hidden/"
    check_readme(url)


if __name__ == "__main__":
    try:
        arg = sys.argv[1]
        main(arg)
    except IndexError:
        print("error arg")
