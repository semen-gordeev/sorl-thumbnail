# -*- encoding: utf8 -*-
from __future__ import unicode_literals

import logging

__author__ = "Mikko Hellsing"
__license__ = "BSD"
__version__ = '11.12.1b'
__maintainer__ = "Mario César Señoranis Ayala"
__email__ = "mariocesar@creat1va.com"
__status__ = "Beta"

logger = logging.getLogger('sorl')
hdlr = logging.FileHandler('/tmp/sorl.log')
formatter = logging.Formatter(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)