import logging
import sys

formatter = logging.Formatter(
    fmt="[%(asctime)s:%(module)s:%(lineno)s:%(levelname)s] %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
"""
LOGGING
-------
Defaults -
* Shows WARNING & higher (ERROR, CRITICAL) level logs
* Uses root logging object

Singleton pattern -
* The singleton pattern is a design pattern that restricts the instantiation of a class to one object.
* This allows the global object to be shared across the application. For example - DB Connection, logger

Handlers -
* Destination for logging object.
* Could be either of file, stdout, rotating file, network sockets, etc
* Handlers can have their own logging level

Foramtters -
* String specifying the format for displaying message
"""

"""
LOGGING
-------
Defaults -
* Shows WARNING & higher (ERROR, CRITICAL) level logs
* Uses root logging object

Singleton pattern -
* The singleton pattern is a design pattern that restricts the instantiation of a class to one object.
* This allows the global object to be shared across the application. For example - DB Connection, logger

Handlers -
* Destination for logging object.
* Could be either of file, stdout, rotating file, network sockets, etc
* Handlers can have their own logging level

Foramtters -
* String specifying the format for displaying message
"""


def singleton_logger():
    # creates application wide log
    global logger
    # create logger object
    logger = logging.getLogger(name="SimpleLogger")
    if not logger.hasHandlers():
        # set logging level
        logger.setLevel(logging.DEBUG)

        # create a handler object - choose type of handler
        streamhandler = logging.StreamHandler(sys.stdout)
        # set handler's logging level
        streamhandler.setLevel(logging.DEBUG)
        # define format to display log message

        # set format to handler
        streamhandler.setFormatter(formatter)
        # add handler to logger
        logger.addHandler(streamhandler)
    return logger
