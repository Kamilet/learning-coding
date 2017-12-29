from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger('retry')

def retry(f):
	@wraps(f)
	def warpped_f(*args, **kwargs):
		MAX_ATTEMPTS = 5	#最大重试次数
		for attempt in range(1, MAX_ATTEMPTS + 1):
			try:
				return f(*args, **kwargs)
			except:
				log.exception("Attempt %s/%s failed: %s",
							   attempt,
							   MAX_ATTEMPTS,
							   (args, kwargs))
				sleep(10 * attempt)
		log.critical('All %s attempts failed : %s',
			MAX_ATTEMPTS,
			(args, kwargs))
	return warpped_f

counter = 0

@retry
def save_to_database(arg):
	print('Write to a database or make a network call or etc.')
	print('This will be automatically retried if exception is thrown.')
	global counter
	counter +=1
	#第一次运行将异常，第二次将正常！
	if counter < 2:
		raise ValueError(arg)

if __name__ == '__main__':
	save_to_database('some bad value')