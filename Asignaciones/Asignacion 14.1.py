import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Important: As of January, 2024 this course no longer includes
# The use of Google's Geocoding API in the content.   This
# has been replaced by OpenStreetMap data
# See the file opengeo.py

# This file is here for previous versions of the course
# materials and since it uses a proxy server to access the API,
# it should work for a while.

#print("See https://www.py4e.com/code3/opengeo.py")

#api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#print(data)
check = False
done = "Done"
while check == False:
    address = input('Enter location: ')
    address = address.strip()
    parms = dict()
    parms['q'] = address
    url = address #serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        info = json.loads(data)
        check = True
    except:
        if address == done :
            print("See you soon")
            exit() 
        else:
            print("The url",address,"is not valid, try again, if you don't want to continue, please type Done")
            continue
#print(json.dumps(info["comments"][0], indent=4))
count = 0
for item in info["comments"]:
    #print(json.dumps(info["comments"]["count"]))
    #print("Count:", item["count"])
    count = count + int(item["count"])
print(count)