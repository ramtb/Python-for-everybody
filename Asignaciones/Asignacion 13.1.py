import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the XML link: ")
uh = urllib.request.urlopen(url, context=ctx)
xml_data = uh.read()

root = ET.fromstring(xml_data)
lst = root.findall("comments/comment")
#print(lst)
count = 0
for item in lst:
    x = int(item.find("count").text)
    count = count + x
print(count)
    #counts = item.findall('.//count')
    #count = counts[0].find("comment").find("count").text
    #print(count)