import logging  # logging is an inbuilt package in python

# let's do some basic configuration, give log file name to be created and written to
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# all the following messages will be written to example.log file we created above
logging.debug('This message should go to the log files')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# everytime we run this code, mode messages will be added at bottom, that is, rewrite instead of overwrite

# let's create a more meaningful log at a different location
# the below configuration will not work unless the previous configuration is deleted
logging.basicConfig(filename='details.log', format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', \
                    level = logging.DEBUG)
logging.debug("A Debug Logging Message")
logging.info("A Info Logging Message")
logging.warning("A Warning Logging Message")
logging.error("An Error Logging Message")
logging.critical("A Critical Logging Message")
