import xml.dom.minidom
from xml.dom.minidom import parse


importxml = xml.dom.minidom.parse("xml-1.xml")
root = importxml.documentElement

if root.hasAttribute("shelf"):
    print("New Arrivals %s" % root.getAttribute("shelf"))

    movies = root.getElementsByTagName("movie")

    for mov in movies:
        title = mov.getElementsByTagName("type")[0]
        print("Movie Title %s" % title.childNodes[0].data)