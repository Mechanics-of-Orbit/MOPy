from log import Log

def main():
    log = Log(loglevel=8)
    log.emergency('Test emergency Print by importing')
    log.alert('Test alert Print by importing')
    log.critical('Test crtical Print by importing')
    log.error('Test error Print by importing')
    log.warning('Test warning Print by importing')
    log.notice('Test notice Print by importing')
    log.debug('Test Debug Print by importing')
    log.info('Test info Print by importing')

if __name__ == '__main__':
    main()