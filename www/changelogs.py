#!/usr/bin/env python

import ConfigParser
import os
import sys
import re


def link_to_launchpad(line):
    return _lp_ticket.sub(r'`LP #\g<1> <%s\g<1>>`_' % _lp_url, line)
_lp_ticket = re.compile(r'LP\s+#?\s*(\d+)', re.IGNORECASE)
_lp_url    = 'https://bugs.launchpad.net/karl3/+bug/'

def fixup_changelog(changelog_path, package_name):
    f = open(changelog_path, 'rb+')
    lines = f.readlines()

    lines[0] = package_name + '\n'
    lines[1] = ('*' * len(package_name)) + '\n'

    for i, line in enumerate(lines):
        lines[i] = link_to_launchpad(line)

    f.seek(0)
    f.truncate(0)
    f.write( ''.join(lines) ) 
    f.close()

def main():
    here = os.path.abspath(os.path.dirname(__file__))

    config = ConfigParser.ConfigParser()
    config.read(os.path.join(here, 'changelogs.ini'))

    index_file = open(os.path.join(here, 'changelogs', 'index.rst'), 'w')
    index_file.write('Package Changelogs\n******************\n\n')
    index_file.write('.. toctree::\n   :maxdepth: 1\n\n')

    for package in sorted(config.sections()):
        underscored_package = package.replace('.', '_')

        changelog_url = config.get(package, 'changelog_url')
        changelog_filename = '%s_changelog.rst' % underscored_package
        changelog_path = os.path.join(here, 'changelogs', changelog_filename)

        cmd = "svn export --force '%s' '%s'" % (changelog_url, changelog_path)
        sys.stdout.write(cmd + "\n")
        os.system(cmd)

        fixup_changelog(changelog_path, package)

        index_file.write('   %s_changelog\n' % underscored_package)
    
    index_file.write('\n')
    index_file.close()   


if __name__ == '__main__':
    main()
    