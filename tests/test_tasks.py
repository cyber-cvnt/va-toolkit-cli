from va_toolkit import tasks

def test_add_and_list(tmp_path, monkeypatch):
    testfile = tmp_path / "tasks.csv"
    monkeypatch.setattr(tasks, "DATA", testfile)

    tasks.add_task("Test Task")
    rows = tasks.list_tasks()
    assert len(rows) == 1
    assert rows[0]['title'] == "Test Task"
