import nidaqmx
from nidaqmx.constants import (
    LineGrouping)


with nidaqmx.Task() as task:
    task.do_channels.add_do_chan(
        'USB6009/port0/line0',
        line_grouping=LineGrouping.CHAN_PER_LINE)

    err = task.write(True, auto_start=True)
    print("{}".format(err))
    # try:
    #     print('N Lines 1 Sample Boolean Write (Error Expected): ')
    #     print(task.write([True, False, True, False]))
    # except nidaqmx.DaqError as e:
    #     print(e)
    #
    # print('1 Channel N Lines 1 Sample Unsigned Integer Write: ')
    # print(task.write(8))
    #
    # print('1 Channel N Lines N Samples Unsigned Integer Write: ')
    # print(task.write([1, 2, 4, 8], auto_start=True))
