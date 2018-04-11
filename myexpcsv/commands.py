# -*- coding: utf-8 -*-
import csv
import click
import pymysql


def _build_records(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        for record in cursor:
            yield record


def _output(asgen, dest):
    with open(dest, 'w', newline='') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for record in asgen:
            w.writerow(record)


@click.command()
@click.option('--host', help="Target host.", default="127.0.0.1")
@click.option('--port', type=int, help="Target port.", default=3306)
@click.option('--db', help="Target Database")
@click.option('--user', help="Username.")
@click.option(
        '--password',
        help="Password.",
        prompt=True,
        hide_input=True,)
@click.option(
        '--charset',
        help="Target Database's charset.",
        default='utf8mb4')
@click.option('--query', help="Excuting SQL as STRING.")
@click.argument('dest',  type=click.Path(exists=False))
def export(
        host,
        port,
        db,
        user,
        password,
        charset,
        query,
        dest):
    """Execute Query and export CSV.
    """
    click.echo('Executing bellow query..')
    click.echo(query)
    click.echo('Output bellow file..')
    click.echo(dest)
    click.echo('or,')
    formatted = click.format_filename(dest)
    click.echo(formatted)

    try:
        connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                db=db,
                charset=charset,
                cursorclass=pymysql.cursors.Cursor,
                )
        # Building records as result set.
        asgen = _build_records(connection, query)
        # Output
        _output(asgen, formatted)
    finally:
        connection.close()


if __name__ == '__main__':
    export()
