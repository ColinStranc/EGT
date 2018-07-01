from modelling.leader import Leader

import logging

logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

leader = Leader(5, 30, 3, 0.1, 0.1)
leader.execute_simulation()