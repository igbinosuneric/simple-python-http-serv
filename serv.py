#import python libraries 
from http.server import HTTPServer, BaseHTTPRequestHandler

#create the class to hold the server 
class Serv(BaseHTTPRequestHandler):
    
    #calling the do get method which is built into the class 
    def do_GET(self):
        #the above methods run everything we revice a get request 
        if self.path == '/':
            #we check if its a forward slash
            self.path = '/index.html'
        #read file to access and send response 200 or 404 
        try: 
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "file not found"
            self.send_response(404) 
        self.end_headers()
        #convert to byte using utf-8 so it can be displayed on screen 
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()

 