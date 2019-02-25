def test_writing_bytes():
	with open('testfile.egt', 'wb') as f:
		f.write(bytearray([14, 1]))


def try_writing_settings(se):
	hf = [ "hf1", "hf2" ]
	hl = len(hf)

	h = bytearray([0, hl])
	s = bytearray([getattr(se, si) for si in hf ])

	with open('test_twd.egt', 'wb') as f:
		f.write(h)
		f.write(s)


class Sett:
	def __init__(self):
		self.hf1 = 2
		self.hf2 = 12
		self.hf3 = 5

from fractions import Fraction

def try_fraction_generation(n):
	print("Generating fractional representation of {}.".format(n))

	f = Fraction(n).limit_denominator(64)

	print("Fraction object: {}".format(f))
	print("Fraction numerator property: {}".format(f.numerator))
	print("Fraction denominator property: {}".format(f.denominator))


from .marshaller import Marshaller
from modelling.settings import Settings

def try_writing_real_settings():
	s = Settings(5, 30, 1, 3, 1/2, 3/2, 0.1, 0.1, 5, 20)

	m = Marshaller(s, name="test")


def try_bitshifting():
	n = 2500

	n1 = n >> 8
	n2 = n - (n1 << 8)

	with open('testbitshift', 'wb') as f:
		f.write(bytearray([n1, n2]))


#def try_append_grid():
#	g = Grid(2)
#	g2 = Grid(2)

#	g.add_agent(new Agent
	

print("starting!")

# try_writing_settings(Sett())
# try_fraction_generation(3.168394098234987298)

try_writing_real_settings()
# try_bitshifting()

print("finished!")
