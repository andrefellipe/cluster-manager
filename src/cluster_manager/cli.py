"""Command Line Interface for the cluster_manager package."""

import typer
from typing_extensions import Annotated

from cluster_manager.core import say_hello

app = typer.Typer(
    name="hello-world",
    help="A state-of-the-art CLI boilerplate tool.",
    add_completion=False,
)


@app.command()
def main(
    name: Annotated[
        str,
        typer.Option("--name", "-n", help="The name of the person to greet."),
    ] = "World",
) -> None:
    """Execute the core greeting logic from the terminal.

    Args:
        name: The name of the person to greet.
    """
    message = say_hello(name)
    typer.echo(message)


if __name__ == "__main__":
    app()
