import iio_scanner
from flask import Flask
from flask import flash, render_template, request, redirect
from flask_table import Table, Col

app = Flask(__name__)

# Declare your table
class ItemTable(Table):
    id = Col('Id', show=False)
    name = Col('Device Type')
    description = Col('URI')

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

def search_for_contexts():
    boards = iio_scanner.scan_all()
    items = []
    for b in boards:
        items.append(Item(b.name,b.uri))
    table = ItemTable(items)
    return table

@app.route('/')
def iio_list():
    table = search_for_contexts()
    table.border = True
    return render_template('iio.html', table=table)

if __name__ == '__main__':
    app.run()
