class Server:
    idip = 1

    def __init__(self, buffer=None):
        self.ip = Server.idip
        self.buffer = buffer
        Server.idip += 1

    def send_data(self, data, ip):
        pass

    def get_data(self) -> list:
        pass

    def get_ip(self) -> int:
        return self.ip


class Router:
    servs = {}
    buffer = []

    def link(self, server):
        self.servs[id(server)] = server

    def unlink(self, server):
        self.servs.pop(id(server))

    def send_data(self):
        pass


class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
