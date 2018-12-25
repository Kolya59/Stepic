def wsgi_application(environ, start_response):
	query_str = environ['QUERY_STRING']
	body = [
		bytes(i + '\n', 'ascii') for i in query_str.split('&')
	]
	status = '200'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, headers)
	return [ body ]
