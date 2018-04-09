# -*- coding: utf-8 -*-
import click
import pymysql


@click.command()
@click.option('--query', help="Excuting SQL as STRING.")
@click.option('--dest', type=click.File('wb'), help="Output Destination.")
def export(query, dest):
    """Excute Query and export CSV
    """
    click.echo('Executing bellow query..')
    click.echo(query)
