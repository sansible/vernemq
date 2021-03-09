import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vernemq_nofiles(host):
    vmq_default_ulimit = "65536"
    vmq_pid = host.process.get(user='vernemq', comm='beam.smp').pid
    vmq_limits = host.file('/proc/{0}/limits'.format(vmq_pid)).content_string
    for line in vmq_limits.split('\n'):
        if line.startswith('Max open files'):
            vmq_actual_ulimit = line.split()[3]

    assert vmq_actual_ulimit == vmq_default_ulimit


def test_vernemq_config(host):
    vmq_config = host.file('/etc/vernemq/vernemq.conf')
    assert vmq_config.exists
    assert vmq_config.contains(
        r"^\s*distributed_cookie\s*=\s*moleculetest\s*$"
    )


def test_vernemq_listening(host):
    ip_address = host.interface("eth0").addresses[0]
    assert host.socket('tcp://{0}:44053'.format(ip_address)).is_listening


def test_vernemq_clustering(host):
    cluster_cmd = 'vmq-admin cluster show | grep true | wc -l | tr -d "\n"'
    assert host.run(cluster_cmd).stdout == '3'
