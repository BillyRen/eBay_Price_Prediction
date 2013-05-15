import httplib
from xml.dom.minidom import parse, parseString, Node

devKey='054eef23-9b5e-4934-9edd-bf9a57181b4d'
appKey='ZJU362bff-d43a-45f4-9744-ee28469423d'
certKey='1a714f88-1b1c-43ee-a821-15b8bdd72ebc'
userToken='token'
serverUrl='api.ebay.com'

def getHeaders(apicall,siteID="0",compatabilityLevel = "433"):
    headers = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatabilityLevel,    
             "X-EBAY-API-DEV-NAME": devKey,
             "X-EBAY-API-APP-NAME": appKey,
             "X-EBAY-API-CERT-NAME": certKey,
             "X-EBAY-API-CALL-NAME": apicall,
             "X-EBAY-API-SITEID": siteID,
             "Content-Type": "text/xml"}
    return headers

def sendRequest(apicall,xmlparameters):
    connection = httplib.HTTPSConnection(serverUrl)
    connection.request("POST", '/ws/api.dll', xmlparameters, getHeaders(apicall))
    response = connection.getresponse()
    if response.status != 200:
        print "Error sending request:" + response.reason
    else: 
        data = response.read()
        connection.close()
    return data

def getSingleValue(node,tag):
    nl=node.getElementsByTagName(tag)
    if len(nl)>0:
        tagNode=nl[0]
        if tagNode.hasChildNodes():
            return tagNode.firstChild.nodeValue
    return '-1'

