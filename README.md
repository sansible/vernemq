# vernemq

Master: [![Build Status](https://travis-ci.org/sansible/vernemq.svg?branch=master)](https://travis-ci.org/sansible/vernemq)  
Develop: [![Build Status](https://travis-ci.org/sansible/vernemq.svg?branch=develop)](https://travis-ci.org/sansible/vernemq)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role installs and configures the [VerneMQ MQTT publish/subscribe message broker](https://vernemq.com/).


## Installation and Dependencies

To install run `ansible-galaxy install sansible.vernemq` or add this to your
`roles.yml`.

```YAML
- name: sansible.vernemq
  version: v2.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses tags: **build** and **configure**

* `build` - Installs and starts VerneMQ
* `configure` - Configures VerneMQ


## Arguments

Argument | Default | Description
----------|---------|------------
sansible_vernemq_cluster_discovery_node | | Cluster node to join in `nodename@ipaddress` format
sansible_vernemq_configuration | | `key: value` configuration option pairs
sansible_vernemq_download_url | | Explicit URL from which to download VerneMQ Debian package _mutually exclusive with the `version` option_
sansible_vernemq_nofile | 65536 | Max number of open files for the VerneMQ process
sansible_vernemq_version | 1.3.1 | Version of VerneMQ to be installed (**NOTE:** Version has to be available from [the official VerneMQ downloads page](https://vernemq.com/downloads/index.html)) _mutually exclusive with the `download_url` option_


## Examples

Install VerneMQ stable with default configuration:

```YAML
- name: Install VerneMQ
  hosts: "somehost"

  roles:
    - role: sansible.vernemq
```

Install VerneMQ v1.2.0, set the number of open maximum open files (`nofiles`) to 65536, join a cluster via 
`saturn@192.168.0.3`, and the `leveldb.maximum_memory.percent` configuration option to 8:

```YAML
- name: Install VerneMQ
  hosts: "somehost"

  roles:
    - role: sansible.vernemq
      sansible_vernemq:
        cluster_discovery_node: saturn@192.168.0.3
        configuration:
          leveldb.maximum_memory.percent: 8
        nofile: 65536
        version: 1.2.0

```

All [VerneMQ configuration options](https://vernemq.com/docs/configuration/) are supported.

The `configuration` section is also the place to
[manage VerneMQ plugins](https://vernemq.com/docs/configuration/plugins.html):

```YAML
- name: Install VerneMQ
  hosts: "somehost"

  roles:
    - role: sansible.vernemq
      sansible_vernemq:
        configuration:
          plugins.vmq_plugin: on
```  


## Development & Testing

If you want to work on this role, please start with running `make watch`; this will execute `make test` on any file
change.
