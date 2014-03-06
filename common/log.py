#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#__author__ = 'qgw'
import logging
import logging.config

logging.config.fileConfig("log.conf")
logger = logging.getLogger("example")