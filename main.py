import logging
import json



logging.basicConfig(
    format='%(asctime)s %(process)d %(levelname)s %(name)s %(message)s', filename="logs.txt")
logger = logging.getLogger(__name__)
logger.info('Logger init ... OK')

if __name__ == '__main__':
    
    
    logger.info('Reading application config')

    appConfig = open("config.json")
    configData = json.load(appConfig)

    message = configData['message']
    
    logger.info('Terminal message')
    print(message)

    logger.info('Executed task.')



