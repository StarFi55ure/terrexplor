import plpy

SQL = """
SELECT way, highway as type

FROM planet_osm_line
    WHERE highway IS NOT NULL
    --AND (tunnel IS NULL OR tunnel = 'no')
    --AND (bridge IS NULL OR bridge = 'no')
"""

def mainfunc(bbox = None):
    '''
    Return all the roads
    '''

    final_SQL = SQL
    if bbox:
        final_SQL += "AND ST_Intersects(way, {})".format(bbox)

    cursor = plpy.cursor(SQL)

    while True:
        rows = cursor.fetch(5)
        if not rows:
            break
        for row in rows:
            yield row

    #for row in plpy.cursor(SQL):
    #    yield row


