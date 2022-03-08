from matplotlib.pyplot import show
from note import *

class Notebook:
    def __init__(self):
        self.notes = {}
        self.last_id = 1

    def create_note(self, memo=None, tags=None):
        note = Note(memo, tags, self.last_id)
        self.notes[self.last_id] = note
        self.last_id += 1
    
    def show_notes(self, note=None):
        show_data = note
        if not note:
            show_data = self.notes
        for note in show_data:
            if type(note) == int:
                note = show_data[note]
            print(f"""Note id: {note.id}
Note tags: {note.tags}
Note text: {note.memo}\n""")

    def search(self, filter=None):
        result = []
        for note_id in self.notes:
            note = self.notes[note_id]
            if (filter in str(note.memo)) or (filter in str(note.tags)):
                result.append(note)
        return result

    def modify(self, note_id, memo=None, tags=None):
        self.notes[note_id].modify(memo, tags)

