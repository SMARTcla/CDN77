# DevOps Project: Infrastructure Automation

## Project description
The goal of this project is to create a virtual infrastructure that will perform some basic operations in our environment. The tasks are divided into the following groups: installation and configuration of services, testing functionality and project documentation.

## Installation and usage instructions
1. Install Ansible on your management server.
2. Clone the repository to your local machine: git clone https://github.com/SMARTCla/CDN77.git
3. Edit the `inventory.ini` file to add the IP addresses of your virtual machines or containers.
4. Run the main playbook `site.yml`: ansible-playbook -i inventory.ini playbooks/site.yml
5. To run individual tasks, use the appropriate playbooks from the `playbooks/` directory.

## Project structure
- `inventory.ini` - Ansible inventory file with information about all managed nodes.
- `playbooks/` - Directory with Ansible playbooks for various tasks.
- `roles/` - A directory containing Ansible roles for each installation and configuration task.
- `scripts/` - Directory with monitoring scripts and auxiliary utilities.
- `tests/` - Directory with tests for checking configurations and functionality of services.
- `LICENSE` - File with the text of the project license.
- `README.md` - This file contains a description of the project and installation instructions.

## License
This project is distributed under the MIT license. See the LICENSE file for details.