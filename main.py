class Server:
    idip = 1

    def __init__(self):
        self.ip = Server.idip
        self.buffer = []
        self.myrouter = None
        Server.idip += 1

    def send_data(self, data):
        if self.myrouter:
            self.myrouter.buffer.append(data)

    def get_data(self) -> list:
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self) -> int:
        return self.ip


class Router:
    def __init__(self):
        self.servs = {}
        self.buffer = []

    def link(self, server):
        self.servs[server.ip] = server
        server.myrouter = self

    def unlink(self, server):
        s = self.servs.pop(server.ip)
        if s:
            s.myrouter = None

    def send_data(self):
        for b in self.buffer:
            if b.ip in self.servs:
                self.servs[b.ip].buffer.append(b)
        self.buffer.clear()


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


router = Router()
s1 = Server()
s2 = Server()
router.link(s1)
router.link(s2)
router.link(Server())
router.link(Server())
s3 = Server()
router.link(s3)
s1.send_data(Data("Hello", s3.get_ip()))
s2.send_data(Data("Hello", s3.get_ip()))
s3.send_data(Data("Hi", s1.get_ip()))
router.send_data()
msg_lst_from = s1.get_data()
msg_lst_to = s3.get_data()
print(msg_lst_to)
