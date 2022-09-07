try:
   from flask import Flask, render_template, request, flash, redirect, url_for
except ImportError:
   print('No module! Run:\n  pip3 install flask')
   exit(3)

import argparse, json
import logging
import os, sys

from argparse import ArgumentParser

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from socket import error as SocketError
import errno


parser = ArgumentParser()
parser.add_argument('--port',
                    help='service port',
                    required=False,
                    nargs='?',
                    type=int,
                    default=os.environ.get('APP_PORT', '8030'))
parser.add_argument('--address',
                    help='service adress',
                    required=False,
                    nargs='?',
                    default=os.environ.get('APP_ADDRESS', '0.0.0.0'))
parser.add_argument('--processes',
                    help='number of threads',
                    required=False,
                    nargs='?',
                    type=int,
                    default=os.environ.get('APP_PROCESSES', '1'))
parser.add_argument('--threaded',
                    help='turn on threads',
                    required=False,
                    nargs='?',
                    default=os.environ.get('APP_THREADED', 'False'))
parser.add_argument('--debug',
                    help='turn on debug mode',
                    required=False,
                    nargs='?',
                    default=os.environ.get('APP_DEBUG', 'False'))

args = parser.parse_args()

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
  if request.method == 'POST':
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))

    root_dir = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(root_dir, UPLOAD_FOLDER, f.filename)
    data = json.load(open(json_url))

    return data



if __name__ == '__main__':

  logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

  logger = logging.getLogger()

  logger.info(f' * Starting app')

  app.run(args.address, args.port, processes=args.processes, threaded=args.threaded, debug=args.debug)


