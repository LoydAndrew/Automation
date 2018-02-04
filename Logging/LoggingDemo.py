import logging
from HandyWrapper import customLogger as cl

class LogginDemo():
    log = cl(logging.DEBUG)
    def method1(self):
        self.log.debug('debug')
        self.log.info('info')
        self.log.warn('warning')
        self.log.error('error')
        self.log.critical('critical')

    def method2(self):
        m2Log = cl(logging.INFO)
        m2Log.debug('debug')
        m2Log.info('info')
        m2Log.warn('warning')
        m2Log.error('error')
        m2Log.critical('critical')

    def method3(self):
        m3Log = cl(logging.INFO)
        m3Log.debug('debug')
        m3Log.info('info')
        m3Log.warn('warning')
        m3Log.error('error')
        m3Log.critical('critical')


demo = LogginDemo()
demo.method1()
demo.method2()
demo.method3()
