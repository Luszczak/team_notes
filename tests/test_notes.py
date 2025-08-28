import json
from app.notes import add_note, list_notes

def test_add_note(tmp_path, monkeypatch):
    # Crear archivo temporal
    test_file = tmp_path / "notes.json"
    test_file.write_text("[]")

    # Redefinir open() para que use el archivo temporal
    def fake_open(file, mode="r+", *args, **kwargs):
        return open(test_file, mode, *args, **kwargs)

    monkeypatch.setattr("builtins.open", fake_open)

    # Ejecutar función
    add_note("Test Title", "Test Body")

    # Verificar contenido
    with open(test_file) as f:
        notes = json.load(f)
        assert len(notes) == 1
        assert notes[0]["title"] == "Test Title"
