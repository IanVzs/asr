all: run
run:
	python test_runtime_server.py --host 0.0.0.0 --port 9009 --certfile ssl_key/server.crt --keyfile ssl_key/server.key
