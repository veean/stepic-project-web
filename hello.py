def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    url_payload =  environ['QUERY_STRING'].split('&')
    env_dict = [element +"\r\n" for element in url_payload]
    return env_dict

