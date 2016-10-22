Instalação
==========

Instalação
----------

1. Acesse: https://github.com/odoo-brazil/odoo-developer-tutorial
2. Faça um fork do repositório
3. Clone o seu fork e instale as dependências:

.. code-block:: shell

    git clone git@github.com:user/odoo-developer-tutorial.git
    cd odoo-developer-tutorial
    sh dependencies.sh

Buildout
########

Iniciando o buildout

.. code-block:: shell

    virtualenv . --system-site-packages
    bin/pip install --upgrade pip setuptools zc.buildout

Crie um arquivo buildout.cfg com o conteúdo:

.. literalinclude:: ../../buildout.cfg.in
   :linenos:

.. nextslide::

Execute o comando para realizar o download do Odoo e suas dependências:

.. code-block:: shell

    bin/buildout

Inicie o odoo com:

.. code-block:: shell

    bin/start_odoo

- Acesse: https://localhost:8069
- Login: admin
- senha: admin