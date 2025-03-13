import click


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'), required=False)
def wc(files):
    if not files:
        files = [click.get_text_stream('stdin')]

    total_words, total_lines, total_bytes = 0, 0, 0

    for file in files:
        filename = file.name if file.name != "<stdin>" else ""
        data = file.read()

        words = len(data.split())
        lines = data.count('\n')
        bytes_num = len(data)

        click.echo(f"    {lines:4}    {words:4}    {bytes_num:4} {filename}")

        total_words += words
        total_lines += lines
        total_bytes += bytes_num

    if len(files) > 1:
        click.echo(f"    {total_lines:4}    {total_words:4}    {total_bytes:4} total")


if __name__ == '__main__':
    wc()
