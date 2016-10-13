Introdução a Criação de modulos
===============================

Objetivo
--------

- Entender como um modulo do tipo backend Odoo é estruturado;
- Como realizar o desenvolvimento incremental do mesmo;
- Desenvolvimento Orientado a Testes (TDD);

Criando e instalando um novo modulo
###################################

.. code-block:: shell

    cd specific-parts
    mkdir open_academy
    cd open_academy
    touch __init__.py
    nano __openerp__.py

- Adicione no aquivo __openerp__.py um dicionário

.. code-block:: python

    {'name': 'Open Academy'}

Instalando o módulo:
####################

1. Inicie o odoo
2. Ative o modo desenvolvedor
3. Acesse configurações > Atualizar lista de modulos ( Devemos fazer isso sempre que um novo modulo é disponibilizado em um banco de dados )
4. Procure seu modulo na lista de modulos e o instale-o.

Definições:
###########

- Um modulo odoo é um diretório contendo arquivos;
- O nome da pasta é o nome tecnico;
- O 'name' definido no dicionário do manifesto é o Titulo do modulo.
- O arquivo __openerp__.py é o manifesto do modulo. Ele contem um dicionário com os detalhes do modulo: descrição, dependencias, data que deve ser carregada e etc;
- O diretorio deve ser importável pelo python, ou seja ter um arquivo __init__.py mesmo que vazio. Ele tambem pode conter os modulos python e submodulos que devem ser importados.

Arquivo de Manifesto
--------------------
1. Preencha seu arquivo de manifesto com as chaves mais significativas conforme o exemplo:

.. code-block:: python

    # -*- coding: utf-8 -*-
    {
        'name': "Title",
        'summary': "Short subtitle phrase",
        'description': """Long description""",
        'author': "Your name",
        'license': "AGPL-3",
        'website': "http://www.example.com",
        'category': 'Uncategorized',
        'version': '8.0.1.0.0',
        'depends': ['base'],
    }


.. nextslide::

- O trecho -*- coding: utf-8 -*- permite que utilizemos caracteres não ASCII no arquivo.
- **name:** O titulo do modulo
- **summary:** Um subtitulo com uma linha
- **description:** Deve ser escrito no padrão `ReStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_
- **author:** O nome dos autores separados por virgula.
- **license:** AGPL-3 , LGPL-3 , Other OSI approved license etc.
- **website:** Url para dar mais informações sobre os autores
- **category:** `Lista de categorias possiveis <https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml>`_

.. nextslide::

- **versao:** Versão do modulo
- **depends:** É uma lista de com os nomes tecnicos que este modulo depende.

**Importante:** Se não depender de nenhum modulo, ao menos deve depender do modulo **base**

Qualquer referencia que seu modulo realize com xmls ids, visões ou modelos refenciados por este modulo.

Esta lista garante que tudo será carregado na ordem correta.

.. nextslide::

- **data:** Lista dos caminhos dos arquivos de dados
- **demo:** Lista dos caminhos dos arquivos de demo


Estrutura de arquivos do modulo
-------------------------------

.. code-block:: shell

    .
    ├── __init__.py
    ├── __openerp__.py
    │
    ├── controllers
    │
    └── __init__.py
    ├── data
    ├── i18n
    ├── models
    │
    └── __init__.py
    ├── security
    ├── static
    │
    └── description
    └── views

.. nextslide::

Um modudo Odoo pode conter três tipos de aquivos:

- Arquivos python
- Arquivos de dados: XML / CSV / YML
- Arquivos Web: Css / Qweb / HTML


Mapeamento Objeto relacional
----------------------------
- Model é uma representação de um objeto de negócio, eles podem ser persistentes e abstratos:

.. code-block:: python

    class A(models.Model):
        ...
    class B(models.AbstractMethod):
        ...
    class C(models.TransientMethod):
        ...

- Modelos Odoo são objetos derivados da classe Odoo Model.
- Quando um novo modulo é definido ele é adicionado a tabela de modelos (ir_model)

.. nextslide::

- Modelos tem alguns atributos definidos com underline. O mais importante é o _name que define um identificador unico do modelo na intancia
- As mudanças nos Modelos são carregadas quando atualizamos os modulos;

.. nextslide::

- A camada de ORM do Odoo evita que seja necessário escrever SQL;
- As classes python que extendem Models, se tornam automaticamente persistentes;

Model Fields
------------

Os campos de um modelo definiem o que pode ser armazenado e onde. Fields são definidos como atributos da classe.

.. code-block:: python

    from openerp import models, fields

    class AModel(models.Model):

        _name = 'a_name'
        name = fields.Char(
            string="Name",                   # Optional label of the field
            compute="_compute_name_custom",  # Transform the fields in computed fields
            store=True,                      # If computed it will store the result
            select=True,                     # Force index on field
            readonly=True,                   # Field will be readonly in views
            inverse="_write_name"            # On update trigger
            required=True,                   # Mandatory field
            translate=True,                  # Translation enable
            help='blabla',                   # Help tooltip text
            company_dependent=True,          # Transform columns to ir.property
            search='_search_function'        # Custom search function mainly used with compute
        )
       # The string key is not mandatory by default it wil use the property name Capitalized
       name = fields.Char()  #  Valid definition

Tipos de campos
###############

**Boolean**

Boolean type field: ::

    abool = fields.Boolean()

**Char**

Store string with variable len.: ::

    achar = fields.Char()


Specific options:

* size: data will be trimmed to specified size
* translate: field can be translated

.. nextslide::

**Text**

Used to store long text.: ::

    atext = fields.Text()

Specific options:

* translate: field can be translated

**HTML**

Used to store HTML, provides an HTML widget.: ::

    anhtml = fields.Html()

.. nextslide::

**Integer**

Store integer value. No NULL value support. If value is not set it returns 0: ::

    anint = fields.Integer()

**Float**

Store float value. No NULL value support. If value is not set it returns 0.0
If digits option is set it will use numeric type: ::

    afloat = fields.Float()
    afloat = fields.Float(digits=(32, 32))
    afloat = fields.Float(digits=lambda cr: (32, 32))

.. nextslide::

**Date**

.. code::

    >>> from openerp import fields

    >>> adate = fields.Date()
    >>> fields.Date.today()
    '2014-06-15'
    >>> fields.Date.context_today(self)
    '2014-06-15'
    >>> fields.Date.context_today(self, timestamp=datetime.datetime.now())
    '2014-06-15'
    >>> fields.Date.from_string(fields.Date.today())
    datetime.datetime(2014, 6, 15, 19, 32, 17)
    >>> fields.Date.to_string(datetime.datetime.today())
    '2014-06-15'

.. nextslide::

**DateTime**

::

    >>> fields.Datetime.context_timestamp(self, timestamp=datetime.datetime.now())
    datetime.datetime(2014, 6, 15, 21, 26, 1, 248354, tzinfo=<DstTzInfo 'Europe/Brussels' CEST+2:00:00 DST>)
    >>> fields.Datetime.now()
    '2014-06-15 19:26:13'
    >>> fields.Datetime.from_string(fields.Datetime.now())
    datetime.datetime(2014, 6, 15, 19, 32, 17)
    >>> fields.Datetime.to_string(datetime.datetime.now())
    '2014-06-15 19:26:13'


**Binary**

Store file encoded in base64 in bytea column: ::

    abin = fields.Binary()

.. nextslide::

**Selection**

Store text in database but propose a selection widget.
It induces no selection constraint in database.
Selection must be set as a list of tuples or a callable that returns a list of tuples: ::

    aselection = fields.Selection([('a', 'A')])
    aselection = fields.Selection(selection=[('a', 'A')])
    aselection = fields.Selection(selection='a_function_name')

.. nextslide::

When extending a model, if you want to add possible values to a selection field,
you may use the `selection_add` keyword argument::

   class SomeModel(models.Model):
       _inherits = 'some.model'
       type = fields.Selection(selection_add=[('10', '10ª opção'), ('11', '11ª opção')])

.. nextslide::

**Reference**

Store an arbitrary reference to a model and a row: ::

    aref = fields.Reference([('model_name', 'String')])
    aref = fields.Reference(selection=[('model_name', 'String')])
    aref = fields.Reference(selection='a_function_name')

Specific options:

* selection: a list of tuple or a callable name that take recordset as input

.. nextslide::

**Many2one**

Store a relation against a co-model: ::

    arel_id = fields.Many2one('res.users')
    arel_id = fields.Many2one(comodel_name='res.users')
    an_other_rel_id = fields.Many2one(comodel_name='res.partner', delegate=True)


.. nextslide::

**One2many**

Store a relation against many rows of co-model: ::

    arel_ids = fields.One2many('res.users', 'rel_id')
    arel_ids = fields.One2many(comodel_name='res.users', inverse_name='rel_id')

.. nextslide::

**Many2many**

Store a relation against many2many rows of co-model: ::

    arel_ids = fields.Many2many('res.users')
    arel_ids = fields.Many2many(comodel_name='res.users',
                                relation='table_name',
                                column1='col_name',
                                column2='other_col_name')

Exercicio: Adicionando modelos
##############################

Crie um arquivo na pasta models, chamado de course.py com o conteudo:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from openerp import models, fields, api

    class Course(models.Model):
        _name = 'openacademy.course'

        name = fields.Char(string="Title", required=True)
        description = fields.Text()

Crie um arquivo __init__.py na pasta models importando o seu modulo:

.. code-block:: python

    from . import course

.. nextslide::

Edite o arquivo __init__.py da raiz para importar a pasta models:

.. code-block:: python

    from . import models

Atualize seu modulo e verifique o banco de dados foi alterado e as tabelas de dados.


Dados:
------
Depois que um módulo Odoo é carregado a maioria dos arquivos é convertida em dados e salva no banco de dados da instância. Representando:

- Os módulos instalados;
- Os modelos desses módulos;
- Os campos desses módulos;
- Dados pré inseridos;
- Dados de demonstração;
- Visões, Filtros padrão;
- Relatórios;
- ETC;

Exercicio: Adicionando dados de demonstração
############################################

Crie um arquivo openacademy/demo/demo.xml para incluir alguns dados:

.. code-block:: xml

    <openerp>
        <data>
            <record model="openacademy.course" id="course0">
                <field name="name">Course 0</field>
                <field name="description">Course 0's description

    Can have multiple lines
                </field>
            </record>
            <record model="openacademy.course" id="course1">
                <field name="name">Course 1</field>
                <!-- no description for this one -->
            </record>
            <record model="openacademy.course" id="course2">
                <field name="name">Course 2</field>
                <field name="description">Course 2's description</field>
            </record>
        </data>
    </openerp>

Adicionando Ações e menus
--------------------------
- Ações e menus são dados regularmente inseridos no banco de dados;

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <openerp>
        <data>
            <act_window
                id="meu_modulo_action"
                name="Minha Ação"
                res_model="meu.modulo" />

            <menuitem
                id="meu_modulo_menu"
                name="Meu Menu"
                action="meu_modulo_action"
                parent=""
                sequence="5" />
        </data>
    </openerp>

Exercicio: Definindo ações e menus
##################################

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <openerp>
        <data>
            <!-- window action -->
            <!--
                The following tag is an action definition for a "window action",
                that is an action opening a view or a set of views
            -->
            <record model="ir.actions.act_window" id="course_list_action">
                <field name="name">Courses</field>
                <field name="res_model">openacademy.course</field>
                <field name="view_type">form</field>
                <field name="view_mode">tree,form</field>
                <field name="help" type="html">
                    <p class="oe_view_nocontent_create">Create the first course
                    </p>
                </field>
            </record>

.. nextslide::

.. code-block:: xml

            <!-- top level menu: no parent -->
            <menuitem id="main_openacademy_menu" name="Open Academy"/>
            <!-- A first level in the left side menu is needed
                 before using action= attribute -->
            <menuitem id="openacademy_menu" name="Open Academy"
                      parent="main_openacademy_menu"/>
            <!-- the following menuitem should appear *after*
                 its parent openacademy_menu and *after* its
                 action course_list_action -->
            <menuitem id="courses_menu" name="Courses" parent="openacademy_menu"
                      action="course_list_action"/>
            <!-- Full id location:
                 action="openacademy.course_list_action"
                 It is not required when it is the same module -->
        </data>
    </openerp>


Defina um visões personalizado.
-------------------------------

Visões personalizadas definiem a forma como os dados serão exibidos e organizados nos diversões tipos de visões:

- Formulário;
- Gráficos;
- Lista;
- Calendário;
- Mapa/Geolocalização;
- Kanban;
- ETC;

.. nextslide::

Exemplo:

.. code-block:: xml

     <record id="meu_modulo_view_type" model="ir.ui.view">
        <field name="name">Meu modulo Type</field>
        <field name="model">meu.modulo</field>
        <field name="arch" type="xml">
            <!-- view content: <form>, <tree>, <graph>, ... -->
        </field>
     </record>

Visão formulário
################

.. code-block:: xml

     <record id="meu_modulo_view_form" model="ir.ui.view">
        <field name="name">Meu modulo Form</field>
        <field name="model">meu.modulo</field>
        <field name="arch" type="xml">
            <form>
                <group>
                    <field name="name"/>
                    <field name="partner_ids" widget="many2many_tags"/>
                </group>
                <group>
                    <field name="date"/>
                </group>
            </form>
        </field>
     </record>

Visão lista
###########

.. code-block:: xml

    <record id="meu_modulo_view_tree" model="ir.ui.view">
    <field name="name">Meu Modulo List</field>
    <field name="model">meu.modulo</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="date"/>
            </tree>
        </field>
    </record>

Busca personalizada
###################

.. code-block:: xml

    <record id="meu_modulo_view_search" model="ir.ui.view">
        <field name="name">Meu modulo Search</field>
        <field name="model">meu.modulo</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <field name="partner_ids"/>
                <filter string="S/ Parceiros"
                    domain="[('partner_ids','=',False)]"/>
            </search>
        </field>
    </record>


Exercicio: Customizando um formulário
#####################################

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <openerp>
        <data>
            <record model="ir.ui.view" id="course_form_view">
                <field name="name">course.form</field>
                <field name="model">openacademy.course</field>
                <field name="arch" type="xml">
                    <form string="Course Form">
                        <sheet>
                            <group>
                                <field name="name"/>
                                <field name="description"/>
                            </group>
                        </sheet>
                    </form>
                </field>
            </record>

            <!-- window action -->
            <!--
                The following tag is an action definition for a "window action",

Exercicio: Search view
######################

.. code-block:: xml

        <record model="ir.ui.view" id="course_search_view">
            <field name="name">course.search</field>
            <field name="model">openacademy.course</field>
            <field name="arch" type="xml">
                <search>
                    <field name="name"/>
                    <field name="description"/>
                </search>
            </field>
        </record>

Recordset
---------

- Um objeto Recordset representa os registros em uma tabela base ou os registros resultantes da execução de uma consulta.

- Quando metodos definidos em um modelo são executados o atributo self é um recorset.

.. code-block:: python

    def do_operation(self):
        print self # => a.model(1, 2, 3, 4, 5)
        for record in self:
            print record # => a.model(1), then a.model(2), then a.model(3), ...

Acesso aos campos
#################

**Recordsets proveem um padrão denominado "Active-Record"**:

Em Engenharia de software, active record é um padrão de projeto encontrado em softwares que armazenam seus dados em Banco de dados relacionais. Assim foi nomeado por Martin Fowler em seu livro Patterns of Enterprise Application Architecture[1].

A interface de um certo objeto deve incluir funções como por exemplo:

- Inserir(Insert) / Atualizar(Update) / Apagar(Delete);
- Propriedades que correspondam de certa forma diretamente às colunas do banco de dados associado.

.. nextslide::

Portanto modelos podem ser escritos e lidos de forma direta através de um record.

Mas somente nos singletons(apenas uma instancia de model). Setar um field dispara um update no banco de dados. Exemplo

.. code-block:: python

    >>> record.name
    Example Name
    >>> record.company_id.name
    Company Name
    >>> record.name = "Bob"
    >>> record.do_operation()

Exercicio: ipython
##################






