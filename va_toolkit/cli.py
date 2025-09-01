import typer
from va_toolkit import tasks

app = typer.Typer()

@app.command()
def add_task(title: str):
    tasks.add_task(title)
    typer.echo(f"Task added: {title}")

@app.command()
def list_tasks():
    for t in tasks.list_tasks():
        typer.echo(f"{t['id']} - {t['title']} ({t['status']})")

if __name__ == "__main__":
    app()
