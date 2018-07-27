import hashlib

def _hash(string):
    return hashlib.sha512(string.encode('utf-8')).hexdigest()

FAMILY_NAME = 'todo'

NAMESPACE = _hash(FAMILY_NAME)[:6] # namespace

PROJECT_METANODE = '00' # tag character defines address type
TODO_TASK = '02'


def make_task_address(project_name,task_name):


def make_project_node_address(project_name):




