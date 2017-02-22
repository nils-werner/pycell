from optparse import OptionParser
import sys
import os
import re

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

    if not sys.argv[1:]:
        parser.print_help()
        sys.exit(2)

    (options, args) = parser.parse_args()
    sys.argv[:] = args

    if len(args) > 0:
        progname = args[0]
        sys.path.insert(0, os.path.dirname(progname))

        with open(progname, 'rb') as fp:
            codestr = split_cells(fp.read())[options.cell]
            code = compile(codestr, progname, 'exec')
        globs = {
            '__file__': progname,
            '__name__': '__main__',
            '__package__': None,
        }

        exec_(code, globs, None)
    else:
        parser.print_usage()
    return parser


def split_cells(data):
    delimiters = [
        '# %s' % s for s in ['\%\%', '<codecell>', 'In\[ \]:', 'In\[\d+\]:']
    ]
    return re.split('|'.join(delimiters), data)


if __name__ == '__main__':
    main()
