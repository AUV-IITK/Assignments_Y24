import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sreeja/aaa stuff/ros_new/install/py_pubsub'
