import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

check = False
done = "Done"
while check == False:
    try:
        address = input('Enter location: ')

        address = address.strip()
        parms = dict()
        parms['q'] = address

        url = serviceurl + urllib.parse.urlencode(parms)
        print('Retrieving', url)
        check = True
    except:
        if address == done :
            print("See you soon")
            exit() 
        else:
            print("The url",address,"is not valid, try again, if you don't want to continue, please type Done")
            continue
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None


    #print(json.dumps(js, indent=4))

    plus_code = js['features'][0]['properties']['plus_code']
    #lon = js['features'][0]['properties']['lon']
    #print('lat', lat, 'lon', lon)
    #location = js['features'][0]['properties']['formatted']
    #print(location)
    print("Plus code: ", plus_code)



