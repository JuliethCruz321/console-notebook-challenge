# Importamos datetime para poder guardar
# la fecha y hora en que se crea cada nota
from datetime import datetime


class Note:
    # Estas constantes sirven para definir
    # niveles de importancia fijos y evitar errores
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    def __init__(self, code: str, title: str, text: str, importance: str):
        # code: identificador único de la nota
        self.code = code

        # title: título corto de la nota
        self.title = title

        # text: contenido de la nota
        self.text = text

        # importance: nivel de importancia (HIGH, MEDIUM o LOW)
        self.importance = importance

        # creation_date guarda automáticamente
        # la fecha y hora en que se crea la nota
        self.creation_date = datetime.now()

        # tags es una lista donde se guardan
        # las etiquetas asociadas a la nota
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        # Este método sirve para agregar etiquetas
        # sin permitir duplicados
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        # Este método define cómo se ve la nota
        # cuando se imprime con print(note)
        return f"Date: {self.creation_date} {self.title}: {self.text}"


class Notebook:
    def __init__(self):
        # notes es la lista donde se almacenan
        # todas las notas del cuaderno
        self.notes: list[Note] = []

    def _generate_code(self) -> int:
        # Este método genera un código único
        # para cada nueva nota
        existing_codes = {note.code for note in self.notes}
        code = 1
        while code in existing_codes:
            code += 1
        return code

    def add_note(self, title: str, text: str, importance: str) -> int:
        # Este método crea una nota nueva
        # y la guarda en el cuaderno
        code = self._generate_code()
        note = Note(code, title, text, importance)
        self.notes.append(note)
        return code

    def delete_note(self, code: int):
        # Elimina una nota según su código
        self.notes = [note for note in self.notes if note.code != code]

    def important_notes(self) -> list[Note]:
        # Devuelve solo las notas que
        # tienen importancia HIGH o MEDIUM
        return [
            note for note in self.notes
            if note.importance in (Note.HIGH, Note.MEDIUM)
        ]

    def notes_by_tag(self, tag: str) -> list[Note]:
        # Devuelve las notas que contienen
        # una etiqueta específica
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        # Este método busca cuál etiqueta
        # aparece más veces en todas las notas
        tag_count = {}

        for note in self.notes:
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1

        # Si no hay etiquetas, no se devuelve nada
        if not tag_count:
            return ""

        # Se busca la etiqueta con mayor cantidad
        max_count = max(tag_count.values())
        most_used = [tag for tag, count in tag_count.items() if count == max_count]

        # Si hay empate, se devuelve la primera alfabéticamente
        return sorted(most_used)[0]
