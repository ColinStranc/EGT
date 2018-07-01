from modelling.leader import Leader

import logging

logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

leader = Leader(5, 30, 3)
leader.execute_simulation()