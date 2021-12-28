import time
from contextlib import contextmanager


class cm_timer_1:
	def __enter__(self):
		self.one = time.perf_counter()
		# return 333

	def __exit__(self, exp_type, exp_value, traceback):
		self.two = time.perf_counter()
		print(f'time: {self.two - self.one}')


@contextmanager
def cm_timer_2():
	one = time.perf_counter()
	yield
	two = time.perf_counter()
	print(f'time: {two - one}')


if __name__ == '__main__':
	with cm_timer_1():
		time.sleep(2)
	with cm_timer_2():
		time.sleep(2)
