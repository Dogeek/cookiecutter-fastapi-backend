import typer


class BaseCommand:
    def __init__(self, app: typer.Typer):
        self.app = app
        