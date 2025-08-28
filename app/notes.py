import json, uuid, datetime

def add_note(title, body):
    note = {
        "id": str(uuid.uuid4()),
        "title": title,
        "body": body,
        "created_at": datetime.datetime.now().isoformat()
    }
    try:
        with open("data/notes.json", "r+") as f:
            notes = json.load(f)
            notes.append(note)
            f.seek(0)
            json.dump(notes, f, indent=2)
    except FileNotFoundError:
        with open("data/notes.json", "w") as f:
            json.dump([note], f, indent=2)