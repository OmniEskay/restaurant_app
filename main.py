from db.setup import init_db
from cli.main_cli import run_cli

if __name__ == "__main__":
    init_db()
    run_cli()
