# lw4o6-automation

Building a Test-Bed for light weigth 4o6 IPv6 Transition Technology.

Ansible software was used, to automate the process of installing and configuration the whole topology elemnts.

Just get the toplogy built, as shown below: -


– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – -– –


![test-bed](https://user-images.githubusercontent.com/45686881/193809234-a9ccf9fd-67e5-4ed4-8ede-4b61d0d26141.png)


– -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– –
– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – -– – – – -– – – – -– – – – -– – – – -– – -– –


All machines are CentOS-7 and built using VMware Workstation Player.


## IP configurations

IPv4 client: must be manually configured

LwB4: ens34 must be manually configured, the script will take care of the rest.

LwAFTR: The script will take care of everything

IPv4 Server: must be manually configured


Now, the machines are built, the required IPs are configured.

## Preparation for automation.

Pre-requisites on every machine:-


``
yum update
``

``
yum install epel-release
``

``
yum install ansible
``

``
yum install git
``

``
git clone https://github.com/ameen-mcmxc/lw4o6-automation.git
``

Now, it's time to confiugre each machine alone: -

I assumed that you logged in as "root".


## Building IPv4 Client: -

``
cd /root/lw4o6-automation
``

``
ansible-playbook IPv4-client.yml
``

## Building lwB4 Router: -

Make sure that you adjust inteface names according to your topology.

``
cd /root/lw4o6-automation
``

``
ansible-playbook lwB4.yml
``

## Building IPv4 Server: -

Make sure that you adjust inteface names according to your topology.

``
cd /root/lw4o6-automation
``

``
ansible-playbook IPv4-server.yml
``


## Building lwAFTR Router: -

Make sure that you adjust inteface names according to your topology.

``
cd /root/lw4o6-automation
``

``
ansible-playbook lwAFTR.yml
``

## Running Snabb

For Snabb ro work, run the commands below on lwAFTR: 

``
isolcpu=2,3
``

``
sudo src/snabb lwaftr run --name "test-lwaftr" --cpu 2-3 --conf lwaftr-start.conf &
``

To stopp Snabb: -

``
killall -9 snabb
``


Note: the IPv4 Server and lwB4 machines MUST be on, so that ARP from lwAFTR towards IPv4 Server and lwB4 works.

