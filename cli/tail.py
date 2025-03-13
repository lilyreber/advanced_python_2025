import click


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'), required=False)
def tail(files):
    num_lines = 10

    if not files:
        files = [click.get_text_stream('stdin')]
        num_lines = 17

    for file in files:
        filename = file.name
        if len(files) > 1:
            click.echo(f"==> {filename} <==")

        lines = file.readlines()[-num_lines:]
        for line in lines:
            click.echo(line, nl=False)
        if len(files) > 1:
            click.echo(f"\n", nl=False)


if __name__ == '__main__':
    tail()
