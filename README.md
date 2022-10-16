# lw4o6-automation

Building a Test-Bed for lw4o6 IPv6 Transition Technology.

Ansible software was used, playbooks were written to automate the process of installing and configuration the whole thing.

Just get the toplogy built, as shown belwo: -





![test-bed](https://user-images.githubusercontent.com/45686881/193809234-a9ccf9fd-67e5-4ed4-8ede-4b61d0d26141.png)




All machines are CentOS-7 and built using VMware Workstation Player.

Pre-requisites:-

1- yum update

2- yum install epel-release

3- yum install ansible


To run snabb software on lwAFTR machine: -

``
cd /root/snabb
``


Note: the server and lwB4 machine must be on, so that ARP from lwAFTR towards IPv4 Server and lwB4 work.



## Building lwB4 Router: -

``
cd /root/lw4o6-automation
``


``
ansible-playbook lwB4.yml
``



## Building lwAFTR Router: -

``
cd /root/lw4o6-automation
``


``
ansible-playbook lwAFTR.yml
``

``
isolcpu=2,3
``

``
sudo src/snabb lwaftr run --name "test-lwaftr" --cpu 2-3 --conf lwaftr-start.conf &
``



## Building IPv4 Server: -


``
cd /root/lw4o6-automation
``

``
ansible-playbook server.yml
``



