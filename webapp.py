from flask import Flask, redirect, request, url_for, render_template
from transaction_factory import *
from transaction_factory import _create_signer

app = Flask(__name__)
action = 'create_project'
fields = {"task_name" : False, "task_description" : False, "new_password" : False}
display_project_name = ''
project_node = ProjectNode()
tasks = []

@app.route('/')
def render():


@app.route('/changeaction',methods=['POST'])
def change_action():


@app.route('/send', methods=['POST'])
def send():



@app.route('/viewproject',methods=['POST'])
def view_project():



def getProjectNode(state,project_name):
    ''' Given a project name get a project node. '''


def getTask(state, project_name,task_name):
    ''' Given a project name and task name get a task node. '''



def getData(state, address):
    ''' Gets the data from a provided address.

        State has two fields address and data.  We can create the
        address using functions in addressing.py.  The data field
        is encoded with base64 encoding.
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)