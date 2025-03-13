import click

@click.command()
@click.argument('file', type=click.File('r'), required=False)
@click.option('-b', type=click.Choice(['a', 't', 'n']), default='t')
def nl(file, b):
    stream = click.get_text_stream('stdin') if file is None else file

    if b == 'n':
        click.echo(stream.read())
    elif b == 't' :
            line_num = 1
            for line in stream.readlines():
                if line.strip():
                    click.echo(f"     {line_num}  {line}", nl=False)
                    line_num += 1
                else:
                    click.echo(f"     {line}", nl=False)
    elif b == 'a':
        for i, line in enumerate(stream.readlines(), start=1):
            click.echo(f"     {i}  {line}", nl=False)


if __name__ == "__main__":
    nl()