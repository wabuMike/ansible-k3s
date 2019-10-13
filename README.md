# Setup k3s

This ansible role downloads, installs and starts [k3s](https://k3s.io/), a lightweight Kubernetes  distribution.

## What's special about this role
There are a few other k3s Ansible roles available on Ansible Galaxy. These points make this script special:

- when downloading k3s binaries, the old ones remain in the subdirectory within `k3s_install_path`. Only the links from /usr/local/bin/ are updated. This means, that if you want to go to a specific version, you are always free to go back to the other version just by replacing the symlinks 'k3s', 'kubectl' and 'crictl' in /usr/local/bin.

- this role uses the same terminology as k3s does: server, agent, etc.

- fully tested with Molecule

## Variables

You might want to override the following variables (i.e. in group_vars or host_vars):

- k3s_install_path: "/opt/k3s"
- k3s_server_options:
- k3s_agent_options:
- k3s_version:

## Server group

Make sure to declare the host, which should act as server, in the following group: `[k3s_server]`.

## Example

Hosts file:

```
[k3s]
192.168.2.90
192.168.2.91
192.168.2.92

[k3s_server]
192.168.2.90
```

Playbook:

```
- hosts: k3s
  become: true
  roles:
    - role: k3s
```

## Test

- Run `molecule test --all`
  - Scenarios exist for Debian (default), Ubuntu and CentOS
