su vagrant <<'EOF'
sudo apt-get update
sudo apt-get install -y python-setuptools
sudo easy_install pip
sudo apt-get install -y xvfb firefox
sudo pip install virtualenv virtualenvwrapper
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bash_profile
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> ~/.bash_profile
source ~/.bash_profile
mkvirtualenv django-contact-form
pip install Django==1.6.2
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby
source /home/vagrant/.rvm/scripts/rvm
gem install --no-rdoc --no-ri cucumber rspec selenium-webdriver headless chronic capybara
EOF
