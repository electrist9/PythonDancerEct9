from dancer.cli import cmd
from dancer.util import cli_args

if __name__ == "__main__":
    cmd(cli_args().parse_args())
