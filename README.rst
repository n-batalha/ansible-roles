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

How to use
----------

Setup an environment with `Mazer <https://github.com/ansible/mazer>`_ (as the current stable Ansible Galaxy does not support roles in a monorepo).

Because :code:`pipenv` might not yet be installed, we just assume Python 3 is:

.. code-block::

  python3 -m venv ~/.virtualenvs/n-batalha-roles
  . ~/.virtualenvs/n-batalha-roles/bin/activate
  pip install -r requirements.txt

  # install [all roles] and make sure we replace existing roles
  mazer install -f --namespace n-batalha git@github.com:n-batalha/ansible-roles.git

Now you can refer to the roles in your playbook like this:

.. code-block::

  - hosts: localhost
    roles:
      - role: n-batalha.ansible-roles.git
        tags: 'git'
        vars:
             email: "your_email@email.com"
             user_name_long: Your Name Here
             git_settings:
               - name: core.editor
                 value: nano
               - name: color.ui
                 value: auto
               - name: user.name
                 value: "{{ user_name_long }}"
               - name: user.email
                 value: "{{ email }}"
               - name: alias.ch
                 value: checkout
               - name: alias.br
                 value: branch
               - name: alias.c
                 value: commit
               - name: alias.s
                 value: status
               - name: alias.unstage
                 value: reset HEAD --
               - name: alias.last
                 value: log -1 HEAD
               - name: alias.visual
                 value: "!gitg"
               - name: core.excludesfile
                 value: "{{ global_git_ignore_file }}"
               - name: commit.gpgsign
                 value: true
      - { role: n-batalha.ansible-roles.direnv, tags: 'direnv' }
      - { role: n-batalha.ansible-roles.i3, tags: 'i3' }
      - { role: n-batalha.ansible-roles.pipenv, tags: 'pipenv'}

Development
-----------

Setup the development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Molecule setup and requirements <https://molecule.readthedocs.io/en/latest/installation.html#requirements>`_ for system package requirements (currently not available to a virtualenv).

Pipenv
++++++

.. code-block:: bash
  # --site-packages as it needs ssl bindings that only exist as system package
  # https://github.com/ansible/ansible/issues/34340

  # temporary pipenv flow due to a bug
  # https://github.com/pypa/pipenv/issues/3504#issuecomment-464453146

  pipenv --site-packages --three
  pipenv install --dev

  # you can now run the tests locally with
  pipenv run bash ./bin/test-local-docker.sh

If you install new dependencies needed for users, please make sure to export them to `requirements.txt` as new users might not have pipenv installed (as it is provided as a role):

.. code-block:: bash

  pipenv lock -r --dev >requirements.txt

Note
++++

At the time of writing, Mazer is changing quickly and does not seem to have a way (documented at least) to work locally on a set of roles. Only via packaging a hacky tar file and installing that (in :code:`./bin/build-install.sh`)

Add more roles
~~~~~~~~~~~~~~

.. code-block::

    cd roles
    molecule init scenario --driver-name docker -r <role_name> --verifier-name testinfra

Then

1. Configure supported :code:`platforms` in :code:`molecule.yml`
2. Add role to :code:`.travis-ci.yml`
3. Add role to the list in this file

FAQ
---

:code:`Fedora: `Unknown Error occured: coreutils-single conflicts with coreutils-8.30-6.fc29.x86_64", "rc": 1, "results": []}`

At the time of writing, this is an `open issue on GitHub <https://github.com/ansible/ansible/issues/49060>`_. Remove the use of :code:`update_cache` in the :code:`dnf` module.
