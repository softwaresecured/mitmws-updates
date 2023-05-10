# Example
# An example HTTP upgrade script that uses python. The script must return a valid HTTP request.
sample_http_request = """GET http://localhost:7878/custom/hellowebsocket HTTP/1.1\r\nX-TEST: FROM PYTHON SCRIPT 1\r\nHost: localhost:7878\r\nSec-WebSocket-Version: 13\r\nSec-WebSocket-Extensions: __WS_EXTENSIONS__\r\nSec-WebSocket-Key: __SEC_WEBSOCKET_KEY__\r\nConnection: keep-alive, Upgrade\r\nHeyMorty: Look I've turned myself into a HTTP request\r\nUpgrade: websocket\r\n\r\n"""
print(sample_http_request)
