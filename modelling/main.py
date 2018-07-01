from modelling.leader import Leader
from modelling.agent import Agent
import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps

import logging

logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

leader = Leader()
leader.execute_simulation()