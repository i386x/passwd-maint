#                                                         -*- coding: utf-8 -*-
#! \file    ./tools/t25l.py
#! \author  Jiří Kučera, <jkucera AT redhat.com>
#! \stamp   2018-04-09 00:47:10 (UTC+01:00, DST+01:00)
#! \project passwd maintenance tools
#! \license MIT
#! \version 0.0.0
#! \fdesc   Translation management tool.
#

import sys
import os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, here)

import data


PT_LOCATOR = "#:"
PT_FLAG = "#,"
PT_MSGID = "msgid"
PT_MSGSTR = "msgstr"

PO_FLAGS = [ "c-format" ]

HK_ON_SHOWLOC = "on-show-location"
HK_ON_SHOWILOC = "on-show-item-location"

ED_NOP = 0
ED_REM = 1
ED_RPL = 2

LN_REMOVE = lambda x: (ED_REM, x)
LN_REPLACE = lambda x, y: (ED_RPL, x, y)


def on_showloc(po, loc):
    return "%s:%d" % (po.path, loc + 1)


def on_showiloc(po, k):
    return "%d" % po.items_map[k][0].msgid.pos[0] + 1


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
    if len(s) < 2:
        return "???"
    return s[1]


def msgstr2s(msgstr):
    s = ""
    for x in msgstr:
        if x and x[0] == '\"':
            x = x[1:-1]
        s += x
    return s


class T25LError(Exception):
    pass


class PoError(T25LError):
    pass


class TaskError(T25LError):
    pass


class Logger(object):
    __slots__ = []

    def __init__(self):
        pass

    def write(self, s):
        pass


class Tee(Logger):
    __slots__ = [ 'streams' ]

    def __init__(self, streams):
        Logger.__init__(self)
        self.streams = streams

    def write(self, s):
        for stream in self.streams:
            stream.write(s)


class MergeOptions(object):
    __slots__ = [ 'dry_run', 'force_dump', 'logger' ]

    def __init__(self):
        self.dry_run = False
        self.force_dump = False
        self.logger = None


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

    def show_locator(self):
        return " ".join(["%s:%d" % x for x in list(zip(*self.locator.data))])


class PoFile(object):
    __slots__ = [
        'path', 'lang', 'lines', 'items', 'items_map', 'cursor', 'hooks',
        'editor'
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
        self.editor = {}

    def merge(self, po, options):
        dry_run = options.dry_run
        if po.lang != self.lang:
            raise PoError(
                "Failing to merge %r and %r (language missmatch)"
                % (self.path, po.path)
            )
        report = options.logger.write
        report("%s: Merging %r:\n" % (self.path, po.path))
        for item in po.items:
            k = item.msgid.data[0]
            if k in self.items_map:
                report("@ merging item #: %s\n" % item.show_locator())
                v = self.items_map[k][0]
                fnames, lnums = v.locator.data
                fnames_, lnums_ = item.locator.data
                if fnames != fnames_ or lnums != lnums_:
                    report("! Different locators:\n")
                    report(
                        "! %r's locator: %s\n" % (self.path, v.show_locator())
                    )
                    report(
                        "! %r's locator: %s\n" % (po.path, item.show_locator())
                    )
                flags = [ t.data[0] for t in v.flags ]
                flags_ = [ t.data[0] for t in item.flags ]
                if flags != flags_:
                    report("! Different flags:\n")
                    report("! %r's flags: %s\n" % (self.path, " ".join(flags)))
                    report("! %r's flags: %s\n" % (po.path, " ".join(flags_)))
                    raise PoError(
                        "Failing to merge %r and %r (flag missmatch)"
                        % (self.path, po.path)
                    )
                msgstr = v.msgstr.data[0]
                msgstr_ = item.msgstr.data[0]
                if msgstr == msgstr_:
                    report("* Items has same msgstr.\n")
                elif msgstr2s(msgstr) == msgstr2s(msgstr_):
                    report("* Items has same msgstr up to the formatting.\n")
                else:
                    report("| Different msgstrs, patching")
                    if dry_run:
                        report(" [dry run]")
                    report(".\n")
                    # Make edit actions:
                    for ln in v.msgstr.pos:
                        if ln in self.editor:
                            raise PoError(
                                "Line #%d has already attached edit action"
                                % ln
                            )
                        self.editor[ln] = LN_REMOVE(v.show_locator())
                    self.editor[v.msgstr.pos[-1]] = LN_REPLACE(
                        v.show_locator(), msgstr_
                    )
            else:
                report("?? no item #: %s (skipping)\n" % item.show_locator())

    def dump(self, options):
        if not self.editor and not options.force_dump:
            # No changes
            return
        dry_run = options.dry_run
        if dry_run:
            self.dump_to_file(Logger(), options)
        else:
            with open(self.path, "w") as f:
                self.dump_to_file(f, options)

    def dump_to_file(self, f, options):
        locator = ""
        report = options.logger.write
        report("\n%s\n" % self.path)
        for i, line in enumerate(self.lines):
            if i not in self.editor:
                f.write("%s\n" % line)
            else:
                ea = self.editor[i]
                if ea[0] == ED_REM:
                    if locator != ea[1]:
                        locator = ea[1]
                        report("\n#: %s\n" % locator)
                    report("< %s\n" % line)
                elif ea[0] == ED_RPL:
                    if locator != ea[1]:
                        locator = ea[1]
                        report("\n#: %s\n" % locator)
                    report("< %s\n" % line)
                    parts = ea[2]
                    first = "msgstr %s" % parts[0]
                    parts = parts[1:]
                    report("> %s\n" % first)
                    f.write("%s\n" % first)
                    for part in parts:
                        report("> %s\n" % part)
                        f.write("%s\n" % part)
                else:
                    report("! unknown edit operation (%d)\n" % ea[0])
        report("\n")

    @classmethod
    def from_scratch(cls, lang):
        return cls("%s.po" % lang)

    def additem(self, s):
        loc = locfroms(s)

        def h(po, l):
            return "%s@%s+%d" % (po.path, loc, l + 1)

        def hh(po, k):
            item, pos = po.items_map[k]
            fs, ls = item.locator.data
            return "@%s:%d+%d" % (fs[0], ls[0], pos + 1)

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
            if po.lines and po.lines[-1] == "":
                del po.lines[-1]
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
        while i < l and self.lines[i][0:2] in ('#', "# "):
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
                "%s:%d: bad preample (msg{id,str} \"\" not found)"
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
                "%s: expected '%s'-line" % (h(self, i), PT_LOCATOR)
            )
        fnames = []
        lnums = []
        try:
            for fnln in self.lines[i].split(' ')[1:]:
                fn_ln = fnln.split(':')
                assert len(fn_ln) == 2
                fnames.append(fn_ln[0])
                lnums.append(int(fn_ln[1]))
        except:
            raise PoError(
                "%s: ill-formed '%s'-line" % (h(self, i), PT_LOCATOR)
            )
        tok = PoToken(PT_LOCATOR, i, tuple(fnames), tuple(lnums))
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
                "%s: ill-formed '%s'-line"
                % (h(self, self.cursor), PT_FLAG)
            )
        flags.append(PoToken(PT_FLAG, self.cursor, s))
        self.cursor += 1

    def parse_item_flags(self, flags):
        while (
            self.cursor < len(self.lines)
            and self.lines[self.cursor].startswith(PT_FLAG)
        ):
            self.parse_item_flag(flags)

    def parse_item_msgx(self, x):
        i = self.cursor
        l = len(self.lines)
        h = self.hooks.get(HK_ON_SHOWLOC, on_showloc)
        if not (i < l and self.lines[i].startswith(x)):
            raise PoError("%s: expected %s" % (h(self, i), x))
        locs = []
        parts = []
        s = self.lines[i][len(x):]
        if not s.startswith(" \""):
            raise PoError("%s: ill-formed %s" % (h(self, i), x))
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
        k = poi.msgid.data[0]
        pos = poi.msgid.pos[0]
        if k in self.items_map:
            h = self.hooks.get(HK_ON_SHOWLOC, on_showloc)
            hh = self.hooks.get(HK_ON_SHOWILOC, on_showiloc)
            raise PoError(
                "%s: duplicit %s (first defined at %s)"
                % (h(self, pos), PT_MSGID, hh(self, k))
            )
        self.items_map[k] = (poi, len(self.items))
        self.items.append(poi)

    def parse_items(self):
        while self.cursor < len(self.lines):
            self.skip_empties()
            self.parse_item()


class PoFileSet(object):
    __slots__ = [ 'objects', 'objects_map' ]

    def __init__(self):
        self.objects = []
        self.objects_map = {}

    def add(self, po):
        lang = po.lang
        if lang in self.objects_map:
            raise PoError("Language %s has been already added" % lang)
        self.objects_map[lang] = (po, len(self.objects))
        self.objects.append(po)

    def merge(self, fileset, options):
        report = options.logger.write
        for item in fileset.objects:
            if item.lang not in self.objects_map:
                report("No target for %r (skipping).\n" % item.path)
                continue
            self.objects_map[item.lang][0].merge(item, options)

    def dump(self, options):
        for item in self.objects:
            item.dump(options)

    @classmethod
    def from_dir(cls, d):
        try:
            files = os.listdir(d)
            files.sort()
        except FileNotFoundError:
            raise PoError("%r is not an existing directory" % d)
        pofiles = cls()
        for f in files:
            p = os.path.join(d, f)
            if not os.path.isfile(p):
                continue
            if os.path.splitext(f)[1] != ".po":
                continue
            pofiles.add(PoFile.from_file(p))
        return pofiles


class T25LTask(object):
    NAME = "?"
    DESC = "?"
    __slots__ = [ 't25l', 'args', 'arg2action_map', 'arg2desc_map' ]

    def __init__(self, t25l, args):
        self.t25l = t25l
        self.args = args
        self.arg2action_map = {}
        self.arg2desc_map = {}

    def addarg(self, arg, desc, action):
        if arg in self.arg2action_map:
            raise TaskError(
                "%s: %r has been already defined" % (self.NAME, arg)
            )
        self.arg2action_map[arg] = action
        self.arg2desc_map[arg] = desc

    def process_args(self):
        args = self.args[:]
        while args:
            arg = args.pop(0)
            if arg not in self.arg2action_map:
                raise TaskError("%s: Unkonwn argument %r" % (self.NAME, arg))
            self.arg2action_map[arg](self, arg, args)

    def help(self):
        wout = self.t25l.wout
        wout("%s - %s\n" % (self.NAME, self.DESC))
        wout("\n")
        wout("Arguments:\n")
        wout("\n")
        for a in self.arg2desc_map:
            wout("  %s%s\n" % (a, self.arg2desc_map[a]))
        wout("\n")

    def run(self):
        pass


class HelpTask(T25LTask):
    NAME = "help"
    DESC = "print general info or info about selected task"
    __slots__ = [ 'task_given' ]

    def __init__(self, t25l, args):
        T25LTask.__init__(self, t25l, args)
        self.task_given = len(args) > 0

    def help(self):
        wout = self.t25l.wout
        wout("%s [TASK] - %s\n")
        wout("\n")
        wout("If no TASK is given, print general info.\n")

    def run(self):
        wout = self.t25l.wout
        if self.task_given:
            task = self.t25l._registered_tasks.get(self.args[0])
            if task is None:
                raise TaskError(
                    "%s: No help for %r task exists."
                    % (self.NAME, self.args[0])
                )
            task(self.t25l, []).help()
            return
        appname = self.t25l.name()
        tl = self.t25l._registered_tasks
        wout("Translation management tool\n")
        wout("\n")
        wout("Usage: %s TASK [ARGS]\n" % appname)
        wout("\n")
        wout("The list of available TASKs is\n")
        wout("\n")
        for t in tl:
            tc = tl[t]
            wout("  %s\n" % tc.NAME)
            wout("  | %s\n" % tc.DESC)
        wout("\n")
        wout("For more info about selected task, run %s help TASK\n" % appname)
        wout("\n")


class PatchTask(T25LTask):
    NAME = "patch"
    DESC = "patch translation"
    __slots__ = [ '_dataset', '_podir', '_merge_options' ]

    def __init__(self, t25l, args):
        T25LTask.__init__(self, t25l, args)
        self._dataset = ""
        self._podir = os.getcwd()
        self._merge_options = MergeOptions()
        self._merge_options.logger = t25l._logger
        self.setup_arguments()

    def setup_arguments(self):
        self.addarg(
            '--dataset',
            " NAME\tset the name of translation data set",
            self.aa_dataset
        )
        self.addarg(
            '--podir',
            " PATH\t\tset the path to the directory whith .po files;"
            " the default is current working directory",
            self.aa_podir
        )
        self.addarg(
            '--dry-run',
            "\t\tprint what's going on, but perform no actions",
            self.aa_dry_run
        )
        self.addarg(
            '--force-dump',
            "\t\twrite to file even if no changes occured",
            self.aa_force_dump
        )

    def run(self):
        self.process_args()
        pofilesA = data.setup(self.t25l, self._dataset)
        if pofilesA is None:
            raise TaskError("%s: no %r data set" % (self.NAME, self._dataset))
        pofilesB = PoFileSet.from_dir(self._podir)
        pofilesB.merge(pofilesA, self._merge_options)
        pofilesB.dump(self._merge_options)

    @staticmethod
    def aa_dataset(task, arg, args):
        if not args:
            raise TaskError("%s: %s: missing data set name" % (task.NAME, arg))
        task._dataset = args.pop(0)

    @staticmethod
    def aa_podir(task, arg, args):
        if not args:
            raise TaskError(
                "%s: %s: missing path to the directory with .po files"
                % (task.NAME, arg)
            )
        task._podir = args.pop(0)

    @staticmethod
    def aa_dry_run(task, arg, args):
        task._merge_options.dry_run = True

    @staticmethod
    def aa_force_dump(task, arg, args):
        task._merge_options.force_dump = True


class T25L(object):
    PoFile = PoFile
    PoFileSet = PoFileSet
    __slots__ = [
        '_name', '_exit_status', '_logger', '_error_logger', '_tasklist',
        '_registered_tasks'
    ]

    def __init__(self):
        self._name = "t25l"
        self._exit_status = 0
        self._logger = None
        self._error_logger = None
        self._tasklist = []
        self._registered_tasks = {}
        self.register_tasks()

    def register_tasks(self):
        self.register_task(HelpTask)
        self.register_task(PatchTask)

    def register_task(self, task):
        if task.NAME in self._registered_tasks:
            self.fail("Task %r has been already registered" % task.NAME)
        self._registered_tasks[task.NAME] = task

    def add_task(self, name, args):
        tc = self._registered_tasks.get(name)
        if tc is None:
            self.fail("Task %r is not registered" % name)
        self._tasklist.append(tc(self, args))

    def add_task_from_argv(self, argv):
        if len(argv) == 0:
            self.fail("No task given in argument vector")
        self.add_task(argv[0], argv[1:])

    def runtasks(self):
        while self._tasklist:
            task = self._tasklist.pop(0)
            task.run()

    def cleartasks(self):
        self._tasklist.clear()

    def set_name(self, name):
        self._name = name

    def name(self):
        return self._name

    def set_logger(self, logger):
        self._logger = logger

    def set_error_logger(self, error_logger):
        self._error_logger = error_logger

    def wout(self, msg):
        if hasattr(self._logger, 'write'):
            self._logger.write(msg)

    def werr(self, msg):
        if hasattr(self._error_logger, 'write'):
            self._error_logger.write(msg)

    def set_exit_status(self, e):
        self._exit_status = e

    def exit_status(self):
        return self._exit_status

    def clear(self):
        self.set_exit_status(0)

    def fail(self, detail):
        self.set_exit_status(1)
        raise T25LError("%s: %s" % (self._name, detail))

    def report_error(self, e):
        self.werr("%s\n" % e.args[0])


def main(argv, f):
    try:
        t25l = T25L()
        t25l.set_name(argv[0])
        t25l.set_logger(Tee([sys.stdout, f]))
        t25l.set_error_logger(Tee([sys.stderr, f]))
        t25l.add_task_from_argv(argv[1:] or [ HelpTask.NAME ])
        t25l.runtasks()
    except T25LError as e:
        t25l.report_error(e)
    finally:
        t25l.cleartasks()
    return t25l.exit_status()


if __name__ == '__main__':
    logfile = "%s.log" % os.path.splitext(os.path.basename(sys.argv[0]))[0]
    with open(logfile, "w") as f:
        sys.exit(main(sys.argv, f))
