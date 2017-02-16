# oooq
Infrared plugin for oooq
```
(ir_venv)[yfried ~/workspace/git/infrared] # ir plugin add git@github.com:rhos-infra/oooq.git

Cloning into 'oooq'...
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 0), reused 5 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), 12.79 KiB | 0 bytes/s, done.
Checking connectivity... done.

(ir_venv)[yfried ~/workspace/git/infrared] # infrared plugin list

┌───────────┬────────────────────┐
│ Type      │ Name               │
├───────────┼────────────────────┤
│ provision │ beaker             │
│           │ foreman            │
│           │ openstack          │
│           │ virsh              │
├───────────┼────────────────────┤
│ install   │ collect-logs       │
│           │ oooq               │
│           │ packstack          │
│           │ tripleo-overcloud  │
│           │ tripleo-undercloud │
├───────────┼────────────────────┤
│ test      │ rally              │
│           │ tempest            │
└───────────┴────────────────────┘
(ir_venv)[yfried ~/workspace/git/infrared] # infrared oooq -h

usage: infrared oooq [-h] [--foo-bool FOO-BOOL] [--foo-bar FOO-BAR] [-v]
                     [--ansible-args ANSIBLE-ARGS] [--inventory INVENTORY]
                     [-i INPUT] [-e EXTRA-VARS] [--dry-run] [-o OUTPUT]
                     [--from-file FROM-FILE]
                     [--generate-answers-file GENERATE-ANSWERS-FILE]

plugin for oooq

optional arguments:
  -h, --help            show this help message and exit

Group A:
  --foo-bool FOO-BOOL
  --foo-bar FOO-BAR     foo.bar option
                        Default value: 'default string'.

Ansible options:
  -v, --verbose         Control Ansible verbosity level
  --ansible-args ANSIBLE-ARGS
                        Extra variables for ansible - playbook tool
                        Should be specified as a list of ansible-playbook options, separated with ";".
                        For example, --ansible-args="tags=tagging,overcloud;forks=500"

Inventory:
  --inventory INVENTORY
                        Inventory file

Common options:
  -i INPUT, --input INPUT
                        Input settings file to be loaded before the merging of user args
  -e EXTRA-VARS, --extra-vars EXTRA-VARS
                        Extra variables to be merged last
  --dry-run             Only generate settings, skip the playbook execution stage
  -o OUTPUT, --output OUTPUT
                        File to dump the generated settings into (default: stdout)

Answers file:
  --from-file FROM-FILE
                        reads arguments from file.
  --generate-answers-file GENERATE-ANSWERS-FILE
                        generate configuration file with default values
(ir_venv)[yfried ~/workspace/git/infrared] # infrared oooq --foo-bool yes --foo-bar no

WARNING [oooq] Argument 'dry-run' was set to 'False' from the spec defaults source.
WARNING [oooq] Argument 'verbose' was set to '0' from the spec defaults source.
install:
  foo:
    bar: 'no'
    bool: true

No config file found; using defaults

PLAY [Main Play] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "install.foo": {
        "bar": "no",
        "bool": true
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0


```
