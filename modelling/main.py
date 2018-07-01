from modelling.leader import Leader

import logging

logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

leader = Leader(5, 10, 3, 0.5)
leader.execute_simulation()