import re
import linkGrabber
links=linkGrabber.Links("http://google.com")
link=links.find(limit=10,pretty=True)
print(link)