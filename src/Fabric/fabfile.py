def setup():
    """
    Setup a fresh virtualenv as well as a few useful directories, then run
    a full deployment
    """
    sudo('aptitude install -y python-setuptools apache2 libapache2-mod-wsgi')
    sudo('easy_install pip')
    sudo('pip install virtualenv')
    sudo('pip install virtualenvwrapper')
    put('.bash_profile', '~/.bash_profile')
    run('mkdir -p %(workon_home)s' % env)
    with settings(warn_only=True):
        # just in case it already exists, let's ditch it
        run('rmvirtualenv %(project_name)s' % env)
    run('mkvirtualenv --no-site-packages %(project_name)s' % env)
    # [... plus other useful stuff.]

def install_requirements():
    "Install the required packages from the requirements file using pip"
    with cd('%(path)s' % env):
        run('workon %(project_name)s && pip install -r ./releases/%(release)s/requirements.txt' % env)
