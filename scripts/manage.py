import click
from flask.cli import FlaskGroup
from app import create_app


cli = FlaskGroup(create_app=create_app)


@cli.command("test")
@click.option("--test_name")
def test(test_name=None):
    """ Runs the unit tests."""
    import unittest
    if test_name is None:
        tests = unittest.TestLoader().discover('tests', pattern="test_*.py")
    else:
        tests = unittest.TestLoader().loadTestsFromName('tests.' + test_name)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    cli()
