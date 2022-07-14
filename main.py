class Graph:
    def __init__(self, data: list, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print('Графическое отображение данных:', *self.data)
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print('Столбчатая диаграмма:', *self.data)
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show):
        self.is_show = fl_show


# data_graph = list(map(int, input().split()))
data_graph = [8, 11, 10, -32, 0, 7, 18]
gr_1 = Graph(data_graph)
gr_1.show_bar()
gr_1.set_show(False)
gr_1.show_table()

