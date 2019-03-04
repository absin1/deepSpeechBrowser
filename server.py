


import http.server
import socketserver
import ssl

def startHTTP():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        #sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mycert.pem -out mycert.pem
        httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/home/absin/git/deepSpeechStreaming/mycert.pem', server_side=True)
        httpd.serve_forever()



if(__name__=='__main__'):
    startHTTP()
    
