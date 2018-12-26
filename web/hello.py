CONFIG = {
	# 'mode': 'wsgi',
	'working_dir' : 'home/box/web/etc/',
	'args': (
		# '--bind=127.0.0.1:8080',
		'--workers=16'
		'--timeout=60'
		'hello.wsgi_application'
	),
}