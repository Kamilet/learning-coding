import os, platform, logging
#platform 模块获取平台信息
#logging模块纪录信息

if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'),\
								os.getenv('HOMEPATH'),
								'test.log')
else:
	logging_file = os.path.join(os.getenv('HOME'),
								'test.log')

print('logging to', logging_file)

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s : %(levelname)s : %(message)s',
	filename=logging_file,
	filemode='w'
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')