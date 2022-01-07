#!/usr/bin/python3

import sys
from jinja2 import Template

sql_foreign_tables_template = open('sql/osm_database_fdw_create.sql', 'r').read()
sql_combined_view_template = open('sql/osm_database_aggregate_view.sql',
        'r').read()

def render_sql(database_name):
    template = Template(sql_foreign_tables_template)
    final_sql = template.render({
        'database': database_name
        })
    return final_sql

def render_view_sql(dbnames):
    template = Template(sql_combined_view_template)
    final_sql = template.render({
        'databases': dbnames
        })
    return final_sql

with open('country_partition_databases.dat', 'r') as databases:
    sql = ''
    lines = [l.strip() for l in databases.readlines()]
    for db in lines:
        if not db.split():
            continue
        dbname, _ = db.split()
        sql += render_sql(dbname)

    dbnames = [db.split()[0] for db in lines if len(db) > 0]
    sql += render_view_sql(dbnames)

    print(sql)



