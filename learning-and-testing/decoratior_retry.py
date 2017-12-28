from time import sleep
from functools import warps
import logging
logging.basicConfig()
log = logging.getLogger('retry')

def retry(f):
	@warps(f)
	def warpped_f(*args, **kwargs):
		MAX_ATTEMPTS = 5	#最大重试次数
		for attempt in range(1, MAX_ATTEMPTS + 1):
			try:
				