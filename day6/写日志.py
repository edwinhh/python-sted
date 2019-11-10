import nnlog

log = nnlog.Logger('test.log',level='debug',backCount=5)
log.debug('debug级别')
log.debug("test")
#debug
#info
#waring
#error