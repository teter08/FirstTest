class Notebook:
    def __init__(self, notes: list):
        self._notes = notes

    @property
    def notes_list(self):
        [print(f'{i}.{value}', sep='\n') for i, value in enumerate(self._notes, start=1)]


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
