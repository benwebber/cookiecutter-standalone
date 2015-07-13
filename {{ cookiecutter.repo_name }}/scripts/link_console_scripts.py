#!/usr/bin/env python

import argparse
import errno
import logging
import os
import sys

import pkg_resources


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def force_symlink(target, name):
    """
    Create a symlink even if the destination exists.
    """
    makedirs(os.path.dirname(name))
    try:
        os.symlink(target, name)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(name)
            os.symlink(target, name)


def makedirs(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e


def get_console_scripts(name):
    entry_points = pkg_resources.get_entry_map(name)
    return entry_points.get('console_scripts')


def install(args):
    """
    Install setuptools console_script symlinks.
    """
    scripts = get_console_scripts(args.package)
    for script in scripts:
        src = os.path.join(args.source, script)
        dest = os.path.join(args.destination, script)
        logger.info('symlinking {1} to {0}'.format(dest, src))
        force_symlink(src, dest)


def uninstall(args):
    """
    Uninstall setuptools console_script symlinks.
    """
    scripts = get_console_scripts(args.package)
    for script in scripts:
        path = os.path.join(args.destination, script)
        logger.info('removing {0}'.format(path))
        os.remove(path)


def parse_args(argv):
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: parsed arguments.
    """
    parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('install')
    parser_install.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='show verbose output',
    )
    parser_install.add_argument(
        '-s', '--source',
        default=os.path.dirname(__file__),
        help='executable source directory (default: %(default)s)',
    )
    parser_install.add_argument(
        '-d', '--destination',
        default='/usr/local/bin',
        help='executable destination directory (default: %(default)s)',
    )
    parser_install.add_argument('package')
    parser_install.set_defaults(func=install)

    parser_uninstall = subparsers.add_parser('uninstall')
    parser_uninstall.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='show verbose output',
    )
    parser_uninstall.add_argument(
        '-d', '--destination',
        default='/usr/local/bin',
        help='executable destination directory (default: %(default)s)',
    )
    parser_uninstall.add_argument('package')
    parser_uninstall.set_defaults(func=uninstall)

    args = parser.parse_args(argv)
    return args


def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    args = parse_args(argv)

    if args.verbose:
        logger.setLevel(level=logging.INFO)

    args.func(args)


if __name__ == '__main__':
    sys.exit(main())
