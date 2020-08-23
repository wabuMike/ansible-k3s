import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('k3s_server')


def test_node(host):
    get_nodes = host.run('kubectl get node molecule-k3s-agent')

    assert get_nodes.rc == 0

def test_iptables_running_and_enabled(host):
    iptables = host.service("iptables")
    assert iptables.is_running
    assert iptables.is_enabled
