class Server:
    idip = 1

    def __init__(self, buffer=None):
        self.ip = Server.idip
        self.buffer = buffer
        Server.idip += 1


class Router:
    servs = {}

    def link(self, server):
        self.servs[id(server)] = server

    def unlink(self, server):
        self.servs.pop(id(server))


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


s1 = Server()
s2 = Server()
s3 = Server()
s4 = Server()
r1 = Router()
r1.link(s1)
r1.link(s2)
r1.link(s3)
r1.link(s4)
r1.unlink(s1)
