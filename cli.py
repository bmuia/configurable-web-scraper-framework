import typer
# from rich import print
from rich.console import Console
from rich.table import Table



# app = typer.Typer()


# @app.command()
# def hello(name: str):
#     print(f"Hello {name}")


# @app.command()
# def goodbye(name: str, formal: bool = False):
#     if formal:
#         print(f"Goodbye Ms. {name}. Have a good day.")
#     else:
#         print(f"Bye {name}!")


# if __name__ == "__main__":
#     app()

# data = {
#     "name": "Rick",
#     "age": 42,
#     "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
#     "active": True,
#     "affiliation": None,
# }

# def main():
#     print("Here is your data friend")
#     print(data)

#     print("[bold red]Alert![/bold red] [blue]This is a[/blue] [purple]drill[/purple] :boom:")


# if __name__ == "__main__":
#     typer.run(main)

# else:
#     print("Script not executable")

# console = Console()


# def main():
#     table = Table("[bold red]Name[/bold red]", "[bold red]Item[/bold red]")
#     table.add_row("Rick", "Portal Gun")
#     table.add_row("Morty", "Plumbus")
#     console.print(table)

# existing_usernames = ["rick", "morty"]
# new_list_usernames = []

# def maybe_create_user(username: str):
#     if username in existing_usernames:
#         print("The user already exists")
#         raise typer.Exit()
#     else:
#         new_list_usernames.append(username)
#         print(f"User created: {username}")


# def send_new_user_notification(username: str):
#     # Somehow send a notification here for the new user, maybe an email
#     print(f"Notification sent for new user: {username}")


# def main(username: str):
#     maybe_create_user(username=username)
#     send_new_user_notification(username=username)


# if __name__ == "__main__":
#     typer.run(main)

# import typer
# from typing_extensions import Annotated


# def main(name: Annotated[str, typer.Argument(help="who are you?")] = "Josh"):
#     print(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer
# from pathlib import Path

# app = typer.Typer()

# @app.command()
# def convert(
#     input_file: Path,  # Argument: required
#     output_format: str = typer.Option("png", help="Output format: png, jpg, webp"),
#     output_folder: Path = typer.Option(Path("."), help="Folder to save converted image"),
#     quality: int = typer.Option(80, help="Image quality (1-100)")
# ):
#     typer.echo(f"Converting {input_file} to {output_format}...")
#     typer.echo(f"Saving to {output_folder} with quality {quality}")
#     # Here you'd add actual conversion logic

# if __name__ == "__main__":
#     app()

import typer
import time
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn

def main():
    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
    ) as progress:

        # Task 1: Job queue loading
        job_queue_task = progress.add_task("[green]Loading jobs...", total=10)

        # Task 2: Workers processing jobs
        workers_task = progress.add_task("[magenta]Processing jobs...", total=10)

        for _ in range(10):
            # Simulate job loading
            time.sleep(0.5)
            progress.update(job_queue_task, advance=1)

            # Simulate processing work
            time.sleep(0.5)
            progress.update(workers_task, advance=1)

if __name__ == "__main__":
    typer.run(main)

