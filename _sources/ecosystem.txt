Sobre o Odoo
============

Um pouco de arquitetura, historia e experiências.

O Odoo
######

    Fazendo companhias um lugar melhor. Um app por vez.

Odoo é uma plataforma de codigo aberto de aplicativos de gestão empresárial.

- Utilizado por grandes companhias, pequenas empresas e diferentes tipos de negócios de organizações de for a auxilia-los a gerenciar, automatizar, medir e otimizar suas operações, finanças e projetos.

História
########

2005

- "Então, em 2005, eu comecei a desenvolver o TinyERP.."
- "Para fazer as coisas acontecer, eu trabalhei duro, muito duro. Eu trabalhei 13 horas por dia, 7 dias por semana, sem férias por 7 anos.
- Pode imaginar qual pequeno eu me senti quando um dos diretores da Danone me perguntou: Por que eu deveria pagar milhoes de dolares em um pequeno(Tiny) software

.. nextslide::

2010

- OpenERP um produto poderoso, porem feio;
- O pivo/mudança de estratégia: Empresa de serviços se tornou um editor de software;
- 9.8 milhoes de Euros: Pesquisa e desenvolvimento / Equipe de vendas / 500 parceiros / 100 paises:
- Contratos com 6 zeros.

.. nextslide::

Então, o sonho começou a se tornar realidade. Começamos a ter pistas de que o que fizemos poderia mudar o mundo

- Com 1000 instaçoes por dia, nos tornamos o software de gerenciamento com mais instaçoes por dia.
- Analistas das 4 maiores empresas de contabilidade (EY, PwC, Deloitte e KPMG) começaram a preferir o Odoo ao invés do SAP
- OpenERP é agora uma disciplina obrigatória para o bacharelado em França como o Word, Excel e PowerPoint
- 60 novos módulos são liberados a cada mês (que se tornou o wikipedia do software de gestão, graças à nossa comunidade forte)

.. nextslide::

2013

- Tivemos 2.000.000 usuários no mundo inteiro;
- Algo estava acontecendo ... E era grande! Novos financiamentos em 2014;
- Depois de anos de crescimento rápido, conseguimos mais um gol incrível;
- USD 10 Milhões de financiamento;

.. nextslide::

2014

- A ascensão do Openerp
- Muito além das tradicionais de ERP;
- Em junho de 2014, lançou a versão 8 com uma incrível CMS e eCommerce, um ponto de venda, um motor integrado de Business Intelligence e muito mais. (e 3000 módulos);
- Mudamos o nome da empresa e do produto para Odoo. E uma nova história apenas começou ...

Fonte: https://www.odoo.com/blog/odoo-news-5/post/the-odoo-story-56

OCA
###

O que tornou o Odoo grande? Comunidade!

.. code::

    # -*- coding: utf-8 -*-
    # © 2016 Daniel Torres
    #  License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
    # Import odoo community association
    from oca import indio

The Odoo Community Association
------------------------------

Associação da comunidade Odoo, ou OCA, é uma organização sem fins lucrativos
cuja a missão é promover o uso generalizado do Odoo e apoiar o desenvolvimento
colaborativo de recursos do Odoo.

- Apoio finaneiro;
- Suporte legal e organizacional a comunidade codigo aberto odoo;
- Independente dos interesses da Odoo SA;

OCA: Objetivos
--------------

- Promover a colaboraçao
- Coordernar
- Defender os interesses
- Divulgar o Odoo
- Facilitar: Sinergia, colaboraçao e levantar fundos
- Roadmaps, implementaçao


OCA: Organização
----------------

.. image:: image/oca-structure.jpg
    :align: center

OCA: Links importantes
----------------------

- OCA TWITTER; @odoocommunity @OCA_Bot
- OCA lists: https://odoo-community.org/groups
- OCA Membership: https://odoo-community.org/page/Membership
- OCA lists: https://odoo-community.org/groups
- Blog: https://odoo-community.org/blog/oca-news-1

Odoo no Brasil
--------------

- Localização Brasileira é mantida pela OCA;
- Código: https://github.com/oca/l10n-brazil
- Lista: https://www.odoo-community.org/groups/brazil-12

Como contribuir?
----------------

    Talk is cheap, show me the code!

-- Linus Torvalds

.. nextslide::

1. Entenda as regras
    - Odoo: https://github.com/odoo/odoo/wiki/Contributing
    - OCA: https://odoo-community.org/page/review
2. Siga as regras
3. Faça pelos outros para que eles façam por voce;

"Gaste o seu tempo de espera revendo as contribuições dos outros "[...] As coisas mais interessantes que aprendi sobre programação em geral e especificamente em Odoo era por ter o meu código revisto ou revendo o código de outras pessoas."
-- Holger Brunn, membro da comunidade.

Arquitetura
-----------

- Arquitetura cliente/servidor, onde os clientes são navegadores web, acessando o servidor Odoo via RPC;
- Mútiplos motores de relatório;
- Motor de workflow;
- Serviços web: XML-RPC / JSON-RPC;
- Modelos extensíveis;
- Visualizações extensíveis;
- Relatórios extensíveis;

.. nextslide::

- Multipla visualização de dados:
    - Calendário;
    - Kanban;
    - Gráfico;
    - Cubo;
    - Mapa;

.. nextslide::

- Conectores:
    - AccountEDGE (MyOB);
    - CMIS (Affresco, Nuexo);
    - Plataforma de e-commerce (Magento, PrestaShop, WooCommerce);
    - Redmine;
    - Sage;
    - Salesforce;
    - Telefonia (Asterisk);

.. nextslide::

.. image:: image/odoo-arch.png
    :align: center

Desenvolvendo com Odoo
######################

- É uma otima plataforma para se desenvolver;
- Comunidade com os mesmos costumes da comunidade python!
- O core do framework é muito bom, te ajuda muito!
- Permite a contrução de aplicações do Zero;
- E adapatar aplicativos existentes para as suas necessidades através de uma mecanismo de extensão modular.
- A Versão 8 trouxe uma gama de novas possibilidades ao adicionar recursos para se desenvolver sites.

.. nextslide::

Problemas:

- O software e bem grande e e normal os ingressantes se sentirem um pouco perdidos.
- Durante anos, os desenvolvedores Odoo aprenderam seu oficio atraves da leitura do codigo fonte do core.
- Apesar de ser uma tecnica efetiva, e um processo demorado e voce acaba ficando sujeito a muitos erros.


Exemplo: Backend Views
######################

.. image:: image/backend2.png
    :align: center


Backend Code: Models
####################

.. code-block:: python

    class ProjectTask(models.Model):

        name = fields.Char('Name')
        date_start = fields.Date('Date Start')
        date_end = fields.Date('Date End')
        stage_id = fields.One2many('Stage', 'project.task.stage')
        ...
        @api.onchange('user_id')
        def _onchange_user(self):
            if self.user_id:
                self.date_start = fields.Datetime.now()
        @api.multi
        def copy(self, default=None):
            ...
        @api.constrains('date_start', 'date_end')
        def _check_dates(self):
            if any(self.filtered(lambda task: task.date_start and
            task.date_end and task.date_start > task.date_end)):
                return ValidationError(
                _('Error !))


Backend Code: Views
###################

.. code-block:: xml

     <record id="act_project_project_2_project_task_all" model="ir.actions.act_window">
            <field name="name">Tasks</field>
            <field name="res_model">project.task</field>
            <field name="view_mode">kanban,tree,form,calendar,pivot,graph</field>
      </record>

      <menuitem action="action_view_task" id="menu_action_view_task" parent="project.menu_project_management" sequence="5"/>

      <record id="view_task_tree2" model="ir.ui.view">
            <field name="name">project.task.tree</field>
            <field name="model">project.task</field>
            <field eval="2" name="priority"/>
            <field name="arch" type="xml">
                <tree decoration-bf="message_needaction==True" decoration-danger="date_deadline and (date_deadline&lt;current_date)" string="Tasks">
                    <field name="message_needaction" invisible="1"/>
                    <field name="sequence" invisible="not context.get('seq_visible', False)"/>
                    <field name="name"/>
                    <field name="project_id" invisible="context.get('user_invisible', False)"/>
                    <field name="user_id" invisible="context.get('user_invisible', False)"/>
                    <field name="planned_hours" invisible="context.get('set_visible',False)" groups="project.group_time_work_estimation_tasks"/>
                    <field name="date_deadline" invisible="context.get('deadline_visible',True)"/>
                    <field name="stage_id" invisible="context.get('set_visible',False)"/>
                </tree>
            </field>
        </record>
      [...]


Frontend Views
##############

- Responsivo

.. image:: image/my-tasks.jpg
    :align: center

Front-End Code: Rotas
#####################

.. code-block:: python

    class website_user_tasks(http.Controller):

    def _prepare_tasks(self, **kw):
        my_tasks = request.env['project.task'].search([
            ('user_id', '=', request.uid)
        ])
        return my_tasks

    @http.route(['/my/tasks'], type='http', auth="user", website=True)
    def tasks(self, **post):
        tasks = {'tasks': self._prepare_tasks()}
        return request.website.render("website_user_tasks.tasks_only", tasks)

Front-End Code: Views
#####################

.. code-block:: xml

    <template id="tasks" name="Minhas Tarefas">
        <h3 >Suas Tarefas</h3>
        <t t-if="not tasks">
            <p>Nao existem tarefas disponiveis.</p>
        </t>
        <t t-if="tasks">
            <div class="table-responsive">
                <table class="table table-hover o_my_status_table">
                    <thead>
                      <tr class="active">
                        <th>Task Code#</th>
                        <th>Nome</th>
                        <th>Inicio</th>
                        <th>Fim</th>
                        <th>Situacao</th>
                      </tr>
                    </thead>
                    <t t-foreach="tasks" t-as="task">
                        <tr>
                            <td><span t-field="task.id"/></td>
                            <td><span t-field="task.name"/></td>
                            <td><span t-field="task.date_start"/></td>
                            <td><span t-field="task.date_end"/></td>
                            <td><span t-field="task.stage_id"/></td>

                        </tr>
                    </t>
                </table>
            </div>
        </t>
    </template>


