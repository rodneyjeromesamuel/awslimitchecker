"""
awslimitchecker/version.py

The latest version of this package is available at:
<https://github.com/jantman/awslimitchecker>

################################################################################
Copyright 2015 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of awslimitchecker, also known as awslimitchecker.

    awslimitchecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    awslimitchecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with awslimitchecker.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/pydnstest> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
################################################################################
"""

_VERSION = '0.1.0'
_PROJECT_URL = 'https://pypi.python.org/pypi/awslimitchecker/{v}'.format(
    v=_VERSION)


def _get_version():
    """
    Returns the currently-installed awslimitchecker version.

    This is a future hook for a more AGPL-y way of getting the actual
    currently-running version, even if it's a git commit, etc.

    :returns: awslimitchecker version
    :rtype: string
    """
    return _VERSION


def _get_project_url():
    """
    Returns the awslimitchecker project URL.

    This is a future hook for a more AGPL-y way of getting the actual
    currently-running project URL, even if it's installed from git.

    :returns: awslimitchecker project URL
    :rtype: string
    """
    return _PROJECT_URL