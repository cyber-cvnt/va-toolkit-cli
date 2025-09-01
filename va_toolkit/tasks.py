import csv, uuid, pathlib

DATA = pathlib.Path("tasks.csv")

def add_task(title):
    DATA.touch(exist_ok=True)
    with DATA.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([str(uuid.uuid4()), title, "open"])

def list_tasks():
    if not DATA.exists():
        return []
    with DATA.open() as f:
        rows = list(csv.DictReader(f, fieldnames=["id", "title", "status"]))
    return rows
