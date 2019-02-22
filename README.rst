Ansible roles collection
========================

.. image:: https://travis-ci.com/n-batalha/ansible-roles.svg?branch=master
    :target: https://travis-ci.com/n-batalha/ansible-roles

See `introductory blog post <https://spotofdata.com/automated-local-environments/?utm_source=github&utm_campaign=ansible_roles/>`_.

Roles
-----

* direnv
* git
* i3
* pipenv
* haskell stack
* git-subrepo

Supported distributions
-----------------------

* Fedora 29

Ubuntu might work (as roles often consider it) but it is not currently tested. Please open a ticket if interested, or submit a Pull Request.

Warning
-------

This is a monorepo with multiple Ansible roles which isn't currently natively supported by Ansible. While this support will come with `Mazer <https://github.com/ansible/mazer>`_, Mazer is currently experimental and breaking too often to be used even in less critical setups. Instead we rely on `a common undocumented feature <https://github.com/ansible/ansible/issues/16804>`_ of stable Ansible until it is replaced by Mazer.

How to use
----------

Setup an environment with  (as the current stable Ansible Galaxy does not support roles in a monorepo).

Because :code:`pipenv` might not yet be installed (as it is a role we provide), we just assume Python 3 is:

.. code-block::

  python3 -m venv ~/.virtualenvs/n-batalha-roles
  . ~/.virtualenvs/n-batalha-roles/bin/activate
  pip install -r requirements.txt

  echo "\
  - src: git@github.com:n-batalha/ansible-roles.git
    scm: git
    name: ansible-roles
    version: master\
  " >> requirements.yml

  # we ignore errors because of the temporary monorepo setup discussed above
  ansible-galaxy install --roles-path ~/.ansible/roles/ --ignore-errors --force -r requirements.yml

Now you can refer to the roles in your playbook like this:

.. code-block::

  - hosts: localhost
    roles:
      - role: ansible-roles/roles/git
        vars:
             email: "your_email@email.com"
             user_name_long: Your Name Here
             git_settings:
               - name: core.editor
                 value: nano
               - name: user.name
                 value: "{{ user_name_long }}"
               - name: user.email
                 value: "{{ email }}"
               - name: alias.ch
                 value: checkout
               - name: alias.c
                 value: commit
               - name: alias.s
                 value: status
      - role: ansible-roles/roles/direnv
      - role: ansible-roles/roles/i3
      - role: ansible-roles/roles/pipenv

Contributing
------------

Please see `CONTRIBUTING <CONTRIBUTING.rst>`_.
