Contributing
------------

Setup the development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Molecule setup and requirements <https://molecule.readthedocs.io/en/latest/installation.html#requirements>`_ for system requirements.

Pipenv
++++++

.. code-block:: bash

    # We use --site-packages as it needs bindings that only exist in a system package
    # https://github.com/ansible/ansible/issues/34340

    # strange temporary pipenv flow due to a bug
    # https://github.com/pypa/pipenv/issues/3504#issuecomment-464453146

    pipenv --site-packages --three
    pipenv install --dev

If you install new dependencies needed for users, please make sure to export them to `requirements.txt` as new users might not have pipenv installed (as it is provided as a role):

.. code-block:: bash

  pipenv lock -r >requirements.txt

Note
++++

* At the time of writing, Mazer is changing quickly and does not seem to have a working way (documented at least) to work locally on a set of roles. If you want to install a role locally without going through a repository, make a symlink / copy of the role to the desired location to install.
* To run a role locally without writing a playbook, just use the included `./bin/ansible-role.sh`

Tests
~~~~~

These are ran on:

* `Travis CI <https://travis-ci.com/n-batalha/ansible-roles>`_
* locally via `./bin/test-local-docker.sh` (it assumes pipenv is configured)
  * the above runs all tests, to test a single role you can run:

  .. code-block:: Bash

    pipenv run bash -c "(cd roles/<tested_role>; molecule test)"

Add more roles
~~~~~~~~~~~~~~

.. code-block::

    pipenv run molecule init role --driver-name docker -r roles/<role_name> --verifier-name testinfra

Then

1. In the role dir, make use of the shared boilerplate `molecule.yml`: `rm molecule/default/molecule.yml && ln -s ../../../molecule-shared.yml molecule/default/molecule.yml`
2. Add role to :code:`.travis-ci.yml`
3. Add role to the list in this file
4. Make sure tests pass

FAQ
---

:code:`Fedora: `Unknown Error occured: coreutils-single conflicts with coreutils-8.30-6.fc29.x86_64", "rc": 1, "results": []}`

At the time of writing, this is an `open issue on GitHub <https://github.com/ansible/ansible/issues/49060>`_. Remove the use of :code:`update_cache` in the :code:`dnf` module.
