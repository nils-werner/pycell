from optparse import OptionParser
import sys
import os
import re
import itertools

# Python 3 compatibility. Mostly borrowed from SymPy
PY3 = sys.version_info[0] > 2

if PY3:
    import builtins
    exec_ = getattr(builtins, "exec")
else:
    def exec_(_code_, _globs_=None, _locs_=None):
        """Execute code in a namespace."""
        if _globs_ is None:
            frame = sys._getframe(1)
            _globs_ = frame.f_globals
            if _locs_ is None:
                _locs_ = frame.f_locals
            del frame
        elif _locs_ is None:
            _locs_ = _globs_
        exec("exec _code_ in _globs_, _locs_")


def main():
    usage = ("usage: pycell [options] scriptfile [arg] ...")
    parser = OptionParser(usage=usage)
    parser.allow_interspersed_args = False

    parser.add_option(
        '-c', '--cell',
        dest="cell",
        type=int,
        help="select cell to run, defaults to the last one",
        default=-1
    )
    parser.add_option(
        '-s', '--strip-magics',
        dest="strip",
        action="store_true",
        help="strip IPython magic commands from source",
    )

    if not sys.argv[1:]:
        parser.print_help()
        sys.exit(2)

    (options, args) = parser.parse_args()
    sys.argv[:] = args

    if len(args) > 0:
        progname = args[0]
        sys.path.insert(0, os.path.dirname(progname))

        with open(progname, 'rb') as fp:
            codelist = split_cells(fp)[options.cell]

            if options.strip:
                codelist = strip_magics(codelist)

            code = compile("\n".join(codelist), progname, 'exec')
        globs = {
            '__file__': progname,
            '__name__': '__main__',
            '__package__': None,
        }

        exec_(code, globs, None)
    else:
        parser.print_usage()


def strip_magics(seq):
    return [l for l in seq if l[0] != '%']


def split_cells(seq):
    delimiters = '|'.join([
        '# %s' % s for s in ['\%\%', '<codecell>', 'In\[ \]:', 'In\[\d+\]:']
    ])

    return [
        list(x[1]) for x in
        itertools.groupby(seq, lambda i: re.match(delimiters, i))
        if not x[0]
    ]


if __name__ == '__main__':
    main()
