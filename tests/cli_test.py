from recursive_cli_search.cli import cli
from click.testing import CliRunner


def test_cli_receives_args():
    runner = CliRunner()
    result = runner.invoke(cli, ["searchword", "commandname"])

    assert result.exit_code == 0
