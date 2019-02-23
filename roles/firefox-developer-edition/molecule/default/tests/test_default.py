import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_firefox_installed(host):
    """
    Ensure the firefox package is installed.
    """
    ff_bin_location = "/root/.local/share/firefox/firefox"
    ff_bin_sym = host.file("/root/.local/bin/firefox-developer-edition")
    ff_bin = host.file(ff_bin_location)

    assert ff_bin_sym.is_symlink
    assert ff_bin.is_file
    assert ff_bin_sym.linked_to == ff_bin_location
