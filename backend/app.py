import json

import bottle
from PointsCurve import *
from Lenstra import *
from dotenv import load_dotenv

load_dotenv()

app = bottle.app()


@bottle.route('/')
def root_index():
    return "start page"


@bottle.post('/add')
def add():
    parsedString = json.loads(bottle.request.body.read())
    a = PointsCurve(int(parsedString["x1"]), int(parsedString["y1"]), int(parsedString["b"]))
    b = PointsCurve(int(parsedString["x2"]), int(parsedString["y2"]), int(parsedString["b"]))
    print(a)
    print(b)
    try:
        c = a.add(b)
    except Exception as e:
        print(str(e))
    return c


@bottle.post('/lenstra')
def lenstraProcess():
    parsedString = json.loads(bottle.request.body.read())
    n = int(parsedString["n"])
    limit = int(parsedString["limit"])
    print(int(n))
    print(int(limit))
    try:
        result = Lenstra.lenstra(n, limit)
    except Exception as e:
        print(e)
    print(result)
    result = {
        "result": result
    }
    return json.dumps(result)


if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(app=app, host='localhost', port=8080)
