import argparse, json
import logging
import os, sys

from argparse import ArgumentParser


try:
   from flask import Flask
except ImportError:
   print('No module! Run:\n  pip3 install flask')
   exit(3)

try:
   from prometheus_flask_exporter import PrometheusMetrics
except ImportError:
   print('No module! Run:\n  pip3 install prometheus_flask_exporter')
   exit(3)


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

k8sConfigMapTest = os.environ.get('K8S_CONF_TEST', 'False')


api = Flask("DevOpsRocketTask")


@api.route('/')
def index():
    try:
      return "This is index latest page <a href=/companies>Check Companies</a><br><br>K8S_CONF_TEST = "+k8sConfigMapTest
    except Exception as e:
      return "Error on index page"


#metrics = PrometheusMetrics(api)
#metrics.info('app_info', 'Application info', version='1.0.0')
#@metrics.gauge('in_progress', 'Long running requests in progress')

@api.route('/companies', methods=['GET','POST','DELETE'])
def companies():
  companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
  return json.dumps(companies)






if __name__ == '__main__':

  logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

  logger = logging.getLogger()

  logger.info(f' * Starting app, Debug mode = {args.debug}')

  api.run(args.address, args.port, processes=args.processes, threaded=args.threaded, debug=args.debug)

#
