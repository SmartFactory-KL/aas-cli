from typer.testing import CliRunner

from aas_cli.app import app

runner = CliRunner()


def test_cli_encode():
    result = runner.invoke(app, ["encode", "test"])
    assert result.exit_code == 0
    assert "dGVzdA" in result.output.strip()
