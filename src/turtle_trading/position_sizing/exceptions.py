#!/usr/bin/env python
# -*- coding: utf8 -*-
""" risk management rules """

class SingleMarketsException(Exception):
  """ Single Markets - A maximum of 4 Units per market. """


class CloselyCorrelatedMarketsException(Exception):
  """ Closely Correlated Markets - A maximum of 6 Units in one particular direction. """


class LooselyCorrelatedMarketsException(Exception):
  """ Loosely Correlated Markets - A maximum of 10 Units in one particular direction. """


class SingleDirectionException(Exception):
  """ Single Direction - A maximum of 12 Units in one direction, long or short.  """