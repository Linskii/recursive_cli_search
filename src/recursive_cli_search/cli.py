import click
import subprocess
from typing import List
from anytree import Node
from collections import deque


@click.command()
@click.argument("searchword")
@click.argument("commandname")
def cli(searchword, commandname):
    root = Node(commandname)

    recursive_help(root)


def recursive_help(command_node: Node) -> str:
    try:
        command_chain = deque([command_node.name])
        while command_node.parent:
            command_node = command_node.parent

            command_chain.appendleft(command_node.name)

        command = list(command_chain) + ["--help"]
        print(command)
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        if not result.stdout.strip():
            print("Command ran but returned no output.")

        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print(e.stderr)
        return ""
    except FileNotFoundError:
        print("Command not found.")
        return ""


def parse_output(output: str) -> List[str]:
    pass


if __name__ == "__main__":
    cli()
