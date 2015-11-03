# Author of this AMAZING code:  Neil de Jubinville, the one and only.
import requests
import simplejson as json
from pprint import pprint

def opportunityInjector():
    #cv = open("cv.txt").read()
    cl = open("cover.txt").read()
    # cl.replace(':', '\:')

    urls = (
             "https://github.com/Neil-Jubinville/close.io"
             "https://goo.gl/1O6UT6",
             "https://goo.gl/ZSZBDD",
             "http://www.orbitalsoftware.ca",
             "https://goo.gl/Hk2QfE"
           )

    payload = {}
    payload['first_name'] = ''
    payload['last_name'] = ''
    payload['phone'] = ''
    payload['email'] = ''
    payload['cover_letter'] = cl

    payload['urls'] = urls

    res = requests.post("https://app.close.io/hackwithus/", data = json.dumps(payload) )
    print res.status_code
    print res.json

    # pre-lint yo stuff homies 
    print(json.dumps(payload))


if __name__== "__main__":
    opportunityInjector()
