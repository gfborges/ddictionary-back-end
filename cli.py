import cli
import click
import subprocess
import time


@click.group()
def cli():
    pass


@cli.command()
def test():
    subprocess.run(
        ["docker-compose", "-f", "test-db.yml", "down"], capture_output=True
    )
    subprocess.run(["docker-compose", "-f", "test-db.yml", "up", "-d"])
    time.sleep(0.05)
    subprocess.run("pytest")
    subprocess.run(["docker-compose", "-f", "test-db.yml", "down"])


if __name__ == "__main__":
    cli()
