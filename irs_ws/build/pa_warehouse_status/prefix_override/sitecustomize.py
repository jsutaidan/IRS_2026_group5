import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aidan/workspace/irs_ws/install/pa_warehouse_status'
