from fabric.api import local


def run_manage(command):
    local('/home/vagrant/.virtualenvs/le-code-test/bin/python /vagrant/testsite/manage.py %s' % command)


def web():
    run_manage('runserver 0.0.0.0:8888')

def migrate():
    run_manage('migrate')

def make_migrations():
    run_manage('makemigrations')

def requirements():
    local('/home/vagrant/.virtualenvs/le-code-test/bin/pip install -r requirements.txt ')

def wipe_database():
    run_manage('flush')

def create_users():
    run_manage('loaddata fixtures/user.json')
    
def create_items():
    run_manage('loaddata fixtures/items.json')

def start_roy_test():
    run_manage('flush')
    run_manage('loaddata fixtures/user.json')
    run_manage('loaddata fixtures/items.json')

