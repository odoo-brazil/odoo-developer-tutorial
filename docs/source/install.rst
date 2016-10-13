Instalação
==========

1. Acesse: https://github.com/odoo-brazil/odoo-developer-tutorial
2. Faça um fork do repositório
3. Clone o seu fork:

.. code-block:: shell

    git clone git@github.com:user/odoo-developer-tutorial.git
    cd odoo-developer-tutorial
    sh dependencies.sh

Dependencias
############

.. literalinclude:: ../../dependencies.sh
   :language: sh
   :linenos:

Buildout
########

.. code-block:: shell

    virtualenv . --system-site-packages
    bin/pip install --upgrade pip setuptools zc.buildout

Crie um arquivo buildout.cfg com o conteúdo:

.. literalinclude:: ../../buildout.cfg.in
   :linenos:

Execute o comando para realizar o download do Odoo e suas dependencias:

.. code-block:: shell

    bin/buildout

Inicie o odoo com:

.. code-block:: shell

    bin/start_odoo

GIT
###

.. code-block:: shell

    git config --global user.name "Your Name"
    git config --global user.email youremail@example.com

