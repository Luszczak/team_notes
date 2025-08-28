import sys
from app.notes import add_note

if sys.argv[1] == "add":
    title = sys.argv[2]
    body = sys.argv[3]
    add_note(title, body)