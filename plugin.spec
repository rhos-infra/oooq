plugin_type: install
description: plugin for oooq
subparsers:
    oooq:
        # FIXME(yfried): duplicates "description"
        help: plugin for oooq
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Group A
              options:
                  foo-bar:
                      type: Value
                      help: "foo.bar option"
                      default: "default string"
                  foo-bool:
                      type: Bool
