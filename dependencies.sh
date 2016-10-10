pip install -q flake8 Click pylint-mccabe
# Install pylint plugin depends without lxml
wget -q https://raw.githubusercontent.com/OCA/pylint-odoo/master/requirements.txt -O ${HOME}/maintainer-quality-tools/travis/pylint_odoo_requirements.txt
find -L ${HOME}/maintainer-quality-tools/travis -name pylint_odoo_requirements.txt -exec sed -i '/lxml/d'  {} \;  #  lxml depends is too slow
pip install --upgrade -r ${HOME}/maintainer-quality-tools/travis/pylint_odoo_requirements.txt
pip install --upgrade --pre --no-deps git+https://github.com/OCA/pylint-odoo.git   # To use last version ever
npm install -g jshint  # Extra package for pylint-odoo plugin

ln -s `which nodejs` $HOME/maintainer-quality-tools/travis/node
npm install -g less less-plugin-clean-css

