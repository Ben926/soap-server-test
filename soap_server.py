from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class MySoapService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def AddNumbers(ctx, a, b):
        return a + b

    @rpc(Unicode, _returns=Unicode)
    def SayHello(ctx, name):
        return f"Hello, {name}!"

application = Application(
    [MySoapService],
    'spyne.examples.hello.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    import os
    port = int(os.environ.get("PORT", 8000))
    server = make_server('0.0.0.0', port, wsgi_app)
    print(f"SOAP server running on http://0.0.0.0:{port}")
    server.serve_forever()