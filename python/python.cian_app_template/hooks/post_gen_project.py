from subprocess import call


def install_deps():
    commands = [
        "pip install pip -U",
        "pip install pipenv -U",
        "pipenv --python 3.6 install -e .",
        "pipenv install --dev",
        "pipenv run pip install ply",
        "pipenv run pip install ply config-generator",
        "pipenv run config-generator-tools validate -m {{ cookiecutter.microservice_name }}",
    ]
    try:
        for com in commands:
            call(com.split())
    except Exception:
        print('Failed to Install a Dependencies')
        print('To install dependencies, run the following commands')
        for com in commands:
            print(com)
    else:
        print('Congratulations!')


# Install dependencies? {% if cookiecutter.install_deps == 'y' %}
install_deps()
# {% endif %}
