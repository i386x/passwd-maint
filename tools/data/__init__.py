#                                                         -*- coding: utf-8 -*-
#! \file    ./tools/data/__init__.py
#! \author  Jiří Kučera, <jkucera AT redhat.com>
#! \stamp   2018-04-10 01:17:03 (UTC+01:00, DST+01:00)
#! \project passwd maintenance tools
#! \license MIT
#! \version 0.0.0
#! \fdesc   Translation data initialization.
#

from . import tr20140118


def setup(t25l, tr):
    return dict(
        tr20140118 = tr20140118.setup(t25l)
    ).get(tr)
