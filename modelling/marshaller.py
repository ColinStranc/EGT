from datetime import datetime
from strategy.contribution.cooperate import Cooperate
from strategy.contribution.defect import Defect 
from strategy.contribution.opportunistic import Opportunistic
from strategy.punishment.anti_social import AntiSocial
from strategy.punishment.non_punishing import NonPunishing 
from strategy.punishment.responsible import Responsible
from strategy.punishment.spiteful import Spiteful


class Marshaller:
	# need save location. Do I get it here or in marshall call?
	# Or do I choose?
	def __init__(self, settings, save_path="storage", name=None):
		self._model_settings = settings
		self._dir = save_path
		self._name = name

		self._version = 0

		self._initialize()
		self._append_settings()

	def append_grid_status(self, grid, round_number):
		agents = grid.get_agents()

		with open(self._full_rel_path, 'ab') as f:
			l1 = len(agents) >> 8
			l2 = len(agents) - (l1 << 8)
			f.write(bytearray([round_number, l1, l2]))

			for agent in agents:
				f.write(self._agent_bytearray(agent, grid.get_coordinates_of_agent(agent), round_number))

	def _agent_bytearray(self, agent, coordinates, n):
		n1 = n >> 8
		n2 = n - (n1 << 8)

		contribute_int = 1 if agent.get_contributed() else 0
		
		return bytearray([n1, n2, coordinates[0], coordinates[1], self._cs(agent._cstrat), self._ps(agent._pstrat), contribute_int])

	def _cs(self, cs_instance):
		cs = cs_instance.__class__

		if cs is Cooperate:
			return 1
		if cs is Defect:
			return 2
		if cs is Opportunistic:
			return 3

	def _ps(self, ps_instance):
		ps = ps_instance.__class__

		if ps is Responsible:
			return 1
		if ps is AntiSocial:
			return 2
		if ps is Spiteful:
			return 3
		if ps is NonPunishing:
			return 4

	def _append_settings(self):
		header_fields = self._get_header_fields()
		header_length = len(header_fields)

		header = self._create_header(header_length)
		settings = self._create_settings(header_fields)

		with open(self._full_rel_path, 'wb') as f:
			f.write(header)
			f.write(settings)

	def _initialize(self):
		time = datetime.now().strftime("%m_%d_%H%M_%s")
		file_name = "egt_{}".format(time) if self._name is None else "egt_{}_{}".format(self._name, time);
		self._full_rel_path = "{}/{}.egt".format(self._dir, file_name)

		# create the file
		open(self._full_rel_path, 'w').close()

	def _create_header(self, length):
		return bytearray([self._version, length])

	def _create_settings(self, field_names):
		field_values = [ getattr(self._model_settings, field_name) for field_name in field_names ]
		return bytearray(field_values)

	def _get_header_fields(self):
		return ['base_pay', 'contribution_cost_num', 'contribution_cost_dn', 'multiplication_factor',
			'punishment_cost_num', 'punishment_cost_dn', 'punishment_fine_num', 'punishment_fine_dn',
			'mutation_rate_num', 'mutation_rate_dn', 'death_rate_num', 'death_rate_dn', 'threat_level',
			'dimension', 'rounds']
