import sys

import click


@click.command()
@click.argument('file', type=click.File('r'), required=False)
@click.option('-b', type=click.Choice(['a', 't', 'n']), default='t')
def nl(file, b):
    stream = sys.stdin if file is None else file

    if b == 'n':
        while line := stream.readline():
            click.echo(f"{line}", nl=False)
    elif b == 't' or b == 'a':
        line_num = 1

        while line := stream.readline():
            if line.strip():
                click.echo(f"     {line_num}  {line}", nl=False)
                line_num += 1
            else:
                if b == 't':
                    click.echo(f"     {line}", nl=False)
                if b == 'a':
                    click.echo(f"     {line_num}  {line}", nl=False)
                    line_num += 1



if __name__ == "__main__":
    nl()
