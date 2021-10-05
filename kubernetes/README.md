1. openstack stack create -t appli-common-stack.yml -e vm-keys.yml kubernetes-bastion
openstack stack create -t appli-kubernetes-stack.yml -e vm-keys.yml kubernetes-conts-workers

2. cp config ~/.ssh/config
3. change bastion with floating ip found here https://openstack.imt-atlantique.fr/project/instances/
4. ssh ubuntu@bastion
ssh ubuntu@k8s-worker-1
ssh ubuntu@k8s-cont-1
...

until all have been rebooted (look at packages list that need to be updated 30 is good 100 is bad)
6. supplementary_addresses_in_ssl_keys task with the floating ip





