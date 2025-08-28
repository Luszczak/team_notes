from app.notes import list_notes, find_notes

if __name__ == "__main__":
    if sys.argv[1] == "list":
        for note in list_notes():
            print(note)

    elif sys.argv[1] == "search":
        query = sys.argv[2]
        for note in find_notes(query):
            print(note)