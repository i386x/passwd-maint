#                                                         -*- coding: utf-8 -*-
#! \file    ./tools/t25l.py
#! \author  Jiří Kučera, <jkucera AT redhat.com>
#! \stamp   2018-04-09 00:47:10 (UTC+01:00, DST+01:00)
#! \project passwd maintenance tools
#! \license MIT
#! \version 0.0.0
#! \fdesc   Translation management tool.
#

import os
import .data

PT_LOCATOR = "#:"
PT_FLAG = "#,"
PT_MSGID = "msgid"
PT_MSGSTR = "msgstr"

HK_ON_SHOWLOC = "on-show-location"
HK_ON_SHOWILOC = "on-show-item-location"


def on_showloc(po, loc):
    return "%s:%d" % (po.path, loc)

def on_showiloc(po, k):
    return "%d" % po.items_map[k][0].msgid.pos[0]

def locfroms(s):
    i = s.find(PT_LOCATOR)
    if i < 0:
        return "???"
    s = s[i:]
    i = s.find('\n')
    if i < 0:
        return "???"
    s = s[:i]
    s = s.split(' ')
    if len(s) != 2:
        return "???"
    return s[1]


class PoError(Exception):
    pass


class PoToken(object):
    __slots__ = [ 'tag', 'pos', 'data' ]

    def __init__(self, tag, pos, *data):
        self.tag = tag
        self.pos = pos
        self.data = data


class PoItem(object):
    __slots__ = [ 'po', 'locator', 'flags', 'msgid', 'msgstr' ]

    def __init__(self, po, locator, flags, msgid, msgstr):
        self.po = po
        self.locator = locator
        self.flags = flags
        self.msgid = msgid
        self.msgstr = msgstr


class PoFile(object):
    __slots__ = [
        'path', 'lang', 'lines', 'items', 'items_map', 'cursor', 'hooks'
    ]

    class StateGuard(object):
        __slots__ = [ 'po', 'lines', 'cursor', 'hooks' ]

        def __init__(self, po):
            self.po = po
            self.lines = []
            self.cursor = 0
            self.hooks = {}

        def __enter__(self):
            self.lines = self.po.lines
            self.cursor = self.po.cursor
            self.hooks = self.po.hooks
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            self.po.lines = self.lines
            self.po.cursor = self.cursor
            self.po.hooks = self.hooks
            return False

    def __init__(self, path):
        self.path = path
        self.lang = os.path.splitext(os.path.basename(path))[0]
        self.lines = []
        self.items = []
        self.items_map = {}
        self.cursor = 0
        self.hooks = {}

    @classmethod
    def from_scratch(cls, lang):
        return cls("%s.po" % lang)

    def additem(self, s):
        loc = locfroms(s)
        def h(po, l):
            return "%s@%s+%d" % (po.path, loc, l)
        def hh(po, k):
            item, pos = po.items_map[k]
            f, l = item.locator.data[0:2]
            return "@%s:%d+%d" % (f, l, pos)
        hooks = {
            HK_ON_SHOWLOC: h,
            HK_ON_SHOWILOC: hh
        }
        with self.__class__.StateGuard(self):
            self.lines = s.split('\n')
            self.cursor = 0
            self.hooks = hooks
            self.parse_items()

    @classmethod
    def from_file(cls, path):
        po = cls(path)
        try:
            with open(path) as f:
                po.lines = f.read().split('\n')
        except FileNotFoundError:
            raise PoError("Cannot open %r. File not found." % path)
        po.make_items()
        return po

    def make_items(self):
        self.cursor = 0
        self.skip_comments()
        self.skip_preamble()
        self.parse_items()

    def skip_empties(self):
        i = self.cursor
        l = len(self.lines)
        while i < l and self.lines[i].strip() == "":
            i += 1
        self.cursor = i

    def skip_comments(self):
        i = self.cursor
        l = len(self.lines)
        while i < l:
            s = self.lines[i]
            if s[0:2] in ('#', "# "):
                i += 1
        self.cursor = i

    def skip_preamble(self):
        i = self.cursor
        l = len(self.lines)
        if i < l and self.lines[i].startswith('msgid ""'):
            i += 1
        if i < l and self.lines[i].startswith('msgstr ""'):
            i += 1
        if i - self.cursor < 2:
            raise PoError(
                "%s:%d: bad preample (msg{id,str} \"\" not found)" \
                % (self.path, i)
            )
        while i < l and self.lines[i].startswith('"'):
            i += 1
        self.cursor = i

    def parse_item_locator(self):
        i = self.cursor
        l = len(self.lines)
        h = self.hooks.get(HK_ON_SHOWLOC, on_showloc)
        if not (i < l and self.lines[i].startswith(PT_LOCATOR)):
            raise PoError(
                "%s: expected '%s'-line" % (h(self.path, i), PT_LOCATOR)
            )
        try:
            fn_ln = self.lines[i].split(' ')
            assert len(fn_ln) == 2
            fn_ln = fn_ln[1].split(':')
            assert len(fn_ln) == 2
            fname = fn_ln[0]
            lnum = int(fn_ln[1])
        except:
            raise PoError(
                "%s: ill-formed '%s'-line" % (h(self.path, i), PT_LOCATOR)
            )
        tok = PoToken(PT_LOCATOR, i, fname, lnum)
        self.cursor += 1
        return tok

    def parse_item_flag(self, flags):
        h = self.hooks.get(HK_ON_SHOWLOC, on_showloc)
        s = self.lines[self.cursor]
        try:
            s = s.split(' ')
            assert len(s) == 2
            s = s[1]
            assert s in PO_FLAGS
        except:
            raise PoError(
                "%s: ill-formed '%s'-line" \
                % (h(self.path, self.cursor), PT_FLAG)
            )
        flags.append(PoToken(PT_FLAG, self.cursor, s))
        self.cursor += 1

    def parse_item_flags(self, flags):
        while self.cursor < len(self.lines) \
        and self.lines[self.cursor].startswith(PT_FLAG):
            self.parse_item_flag(flags)

    def parse_item_msgx(self, x):
        i = self.cursor
        l = len(self.lines)
        h = self.hooks.get(HK_ON_SHOWLOC, on_showloc)
        if not (i < l and self.lines[i].startswith(x)):
            raise PoError("%s: expected %s" % (h(self.path, i), x))
        locs = []
        parts = []
        s = self.lines[i][len(x):]
        if not s.startswith(" \""):
            raise PoError("%s: ill-formed %s" % (h(self.path, i), x))
        locs.append(i)
        parts.append(s[1:])
        i += 1
        # Seek for parts:
        while i < l and self.lines[i].startswith('"'):
            locs.append(i)
            parts.append(self.lines[i])
            i += 1
        tok = PoToken(x, tuple(locs), tuple(parts))
        self.cursor = i
        return tok

    def parse_item(self):
        # EOF?
        if not self.cursor < len(self.lines):
            return
        poi = PoItem(self, None, [], None, None)
        poi.locator = self.parse_item_locator()
        self.parse_item_flags(poi.flags)
        poi.msgid = self.parse_item_msgx(PT_MSGID)
        poi.msgstr = self.parse_item_msgx(PT_MSGSTR)
        k = poi.msgid.data
        pos = poi.msgid.pos[0]
        if k in self.items_map:
            h = self.hooks.get(HK_ON_SHOWLOC, on_showloc)
            hh = self.hooks.get(HK_ON_SHOWILOC, on_showiloc)
            raise PoError(
                "%s: duplicit %s (first defined at %s)" \
                % (h(self.path, p), PT_MSGID, hh(self, k))
            )
        self.items_map[k] = (poi, len(self.items))
        self.items.append(poi)

    def parse_items(self):
        while self.cursor < len(self.lines):
            self.skip_empties()
            self.parse_item()
