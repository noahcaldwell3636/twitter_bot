def get_all_request_codes(urls: list):
    for url in urls:
        response = requests.get(url).status_code
        if response <= 299 and response >= 200:
            print("\n")
            print(f"(({url})) === {response}... success!")
            if response == 200: 
                print("Definition: OK!")
                print("The request succeeded. The result meaning of 'success'" 
                      "depends on the HTTP method:"
                    "\n - GET: The resource has been fetched and transmitted in" 
                    "the message body."
                    "\n - HEAD: The representation headers are included in the "
                    "response without any message body."
                    "\n - PUT or POST: The resource describing the result of the"
                    " action is transmitted in the message body."
                    "\n - TRACE: The message body contains the request message as"
                    " received by the server.")
            elif response == 201: 
                print("Definition: Created")
                print("The request succeeded, and a new resource was created as"
                      " a result. This is typically the response sent after "
                      "POST requests, or some PUT requests.")
            elif response == 202: 
                print("Definition: Accepted")
                print("The request has been received but not yet acted upon. "
                      "It is noncommittal, since there is no way in HTTP to "
                      "later send an asynchronous response indicating the "
                      "outcome of the request. It is intended for cases where"
                      " another process or server handles the request, or for"
                      " batch processing.")
            elif response == 203: 
                print("Definition: Non-Authoriative Information")
                print("This response code means the returned metadata is not "
                      "exactly the same as is available from the origin server,"
                      " but is collected from a local or a third-party copy. "
                      "This is mostly used for mirrors or backups of another "
                      "resource. Except for that specific case, the 200 OK"
                      " response is preferred to this status.")
            elif response == 204: 
                print("Definition: No Content")
                print("There is no content to send for this request, but the "
                      "headers may be useful. The user agent may update its "
                      "cached headers for this resource with the new ones.")
            elif response == 205: 
                print("Definition: Reset Content")
                print("Tells the user agent to reset the document which sent "
                      "this request.")
            elif response == 206: 
                print("Definition: Partial Content")
                print("This response code is used when the Range header is "
                      "sent from the client to request only part of a "
                      "resource.")
            elif response == 207: 
                print("Definition: Multi-Status")
                print("Conveys information about multiple resources, for"
                      " situations where multiple status codes might be "
                      "appropriate.")
            elif response == 208: 
                print("Definition: Already Reported")
                print("Used inside a <dav:propstat> response element to avoid "
                      "repeatedly enumerating the internal members of multiple"
                      " bindings to the same collection.")
            elif response == 226: 
                print("Definition: IM Used")
                print("The server has fulfilled a GET request for the resource,"
                      " and the response is a representation of the result of"
                      " one or more instance-manipulations applied to the "
                      "current instance.")
            else: print("unhandled successful response")
            print("\n")
            
            
        elif response <= 499 and response >= 400:
            print(f"{url} === {response}... ERROR!")