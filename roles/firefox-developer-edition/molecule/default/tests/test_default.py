import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_firefox_installed(host):
    """
    Ensure the firefox package is installed.
    """
    p = host.package('firefox')
    assert p.is_installed
