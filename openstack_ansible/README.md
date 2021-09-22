1. openstack stack create -t mongo-bastion-stack.yml -e vm-keys.yml singlemongo
2. cp config ~/.ssh/config
3. change bastion with floating ip found here https://openstack.imt-atlantique.fr/project/instances/
4. ansible-playbook -i inventory -u ubuntu --private-key ~/.ssh/osvm enable-root-access.yaml
5. ansible-playbook -i inventory -u ubuntu --private-key ~/.ssh/osvm mongo-playbook.yml.yaml
6. profit!

