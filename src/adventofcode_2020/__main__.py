"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Advent Of Code 2020."""


if __name__ == "__main__":
    main(prog_name="adventofcode-2020")  # pragma: no cover
