# Assumptions
1. Docker is installed on the machine and running
2. Ansible (supporting Python 3 only) is installed on the machine
3. Python3 and Pytest (installed using pip3) is installed on the machine
4. Port 8080 is available

# Structure of the project:

This project build and serves a [Tomcat Application Server](https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/)
using [Ansible playbooks](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html).
Also, it uses [Pytest](https://docs.pytest.org/en/latest/) to make sure we can ping the server in
`http://localhost:8080/sample`.


```bash
    .
    ├── ...
    ├── requirements.yml              # Requirements needed by the project, install ansible module
    ├── Dockerfile
    ├── sample.war
    ├── serve-tomcat.yml              # Ansible playbook to serve the tomcat container
    ├── roles
    │   ├── build_dockerfile          # Role in charge of building the image
    │   ├── run_container             # Role in charge of running the container
    │   └── ping_container            # Role in charge of pinging the container
    ├── test_ping.py                  # Python tests to ping the url
    ├── README.md
    └── ...
```

# Run requirements to install ansible modules
```bash
ansible-galaxy collection install -r requirements.yml
```

# Execute the playbook to run the container
```bash
ansible-playbook serve-tomcat.yml
```
