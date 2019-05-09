#这个是ServerSide的demo
from http.server import HTTPServer,SimpleHTTPRequestHandler
import ssl

class MySimpleHandler(SimpleHTTPRequestHandler):


    def do_handle(self):
        '''
        官方文档里说不准override handle(),可以用do_*()
        do_handle()监听客户端发过来信息并做处理
        下面一段是抄 official doc随便写的
        '''
        self.data = self.request.recv(1024).strip()
        print('{0} wrote:'.format(self.client_address[0]))
        print(self.data)
        #只是把客户端发过来的信息原样大写返回一下
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 4430

    #创建httpserver，连到localhost和端口4430
    with HTTPServer((HOST,PORT),MySimpleHandler) as httpd:
        http.socket = ssl.wrap_socket(httpd.socket,certfile='./mypem/certfile.pem',server_side=True) #用server包裹一下就是https了吧
        server.server_forever()
