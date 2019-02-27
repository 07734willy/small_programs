from typing import Tuple


def find_bit_sum(top: int, pad_length: int) -> int :
	"""."""
	return pad_length * (top + 1)


def find_pad_length(top: int) -> int :
	"""."""
	return len(bin(top)) - 2  # -"0b"


def guess_certain(top: int, pad_length: int) -> Tuple[int, int, int] :
	"""."""
	_both = find_bit_sum(top, pad_length)
	_ones = sum(sum(int(_i_in) for _i_in in bin(_i_out)[2 :]) for _i_out in range(1, top + 1))
	return _both - _ones, _ones, _both  # zeros, ones, sum


def guess(top: int, pad_length: int) -> Tuple[int, int, int] :  # zeros then ones then sum
	"""."""
	_bit_sum = find_bit_sum(top, pad_length)  # number of bits in total
	_zeros = _bit_sum  # ones are deducted
	_ones = 0  # _bit_sum - _zeros
	# detect ones
	for _indexed in range(pad_length) :
		_ones_found = int(top // (2 ** (_indexed + 1))) * (2 ** (_indexed)) + max(0, (top % (2 ** (_indexed + 1))) - (2 ** _indexed) + 1)# HELP!!!
		_ones_found = ((top >> _indexed + 1) << _indexed) + max(0, (top & (1 << _indexed + 1) - 1) - (1 << _indexed) + 1)# HELP!!!
		_zeros -= _ones_found
		_ones += _ones_found
	#
	return _zeros, _ones, _bit_sum


def test_the_guess(max_value: int) -> bool :  # the range is int [0, max_value + 1)
	pad = find_pad_length(max_value)
	_zeros0, _ones0, _total0 = guess_certain(max_value, pad)
	_zeros1, _ones1, _total1 = guess(max_value, pad)
	return _ones0 - _ones1
	"""return all((
		_zeros0 == _zeros1,
		_ones0 == _ones1,
		_total0 == _total1
	))"""


if __name__ == '__main__' :  # should produce a lot of True
	for x in range(3000):
		print("HI", x)
		print(test_the_guess(x))
