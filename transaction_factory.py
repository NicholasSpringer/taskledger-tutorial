import hashlib
import secp256k1
import base64
import time
import requests
import urllib.request, json


# Sawtooth SDK
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.batch_pb2 import Batch
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader
from sawtooth_sdk.protobuf.batch_pb2 import BatchList

from protobuf.payload_pb2 import *
from protobuf.project_node_pb2 import *
from protobuf.task_pb2 import *
from addressing import *


def _get_batcher_public_key(signer):
    return signer.pubkey.serialize().hex()


def _get_time():
    return int(time.time())


def _create_signer(private_key):
    signer = secp256k1.PrivateKey(privkey=bytes.fromhex(str(private_key)))
    return signer
    

class Txn_Factory():
    def create_project(self, args):
        ''' Creates a transaction that includes a create_project payload

            args: [password/signer, project_name]
        '''


    def create_task(self, args):
        ''' Creates a transaction that includes a create_task payload

            args: [password/signer, project_name, task_name, description]
        '''


    def progress_task(self, args):
        ''' Creates a transaction that includes a progress_task payload

            args: [password/signer, project_name, task_name]
        '''


    def edit_task(self, args):
        ''' Creates a transaction that includes a create_project payload

            args: [password/signer, project_name, task_name, description]
        '''


    def add_user(self, args):
        ''' Creates a transaction that includes an add_user payload

            args: [password/signer, project_name, password]
        '''



    def create_transaction(self, signer, payload_bytes):
        '''Bundles together a transaction that includes the given payload and is signed by given signer'''


    def create_batch(self, signer, txn):
        '''Bundles together a batch that includes txn and is signed by given signer'''



def send_it(batch_list_bytes):
    '''Sends batch to REST API where it'''

