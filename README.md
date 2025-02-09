# Lw4o6-builder

Building a Test-Bed for light-weigth 4o6 IPv6 Transition Technology.

Ansible software was used, to automate the process of installation and configuration of the whole topology elements.

Just get the toplogy built, as shown below: -


– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – -– –



![lw-test-bed](https://github.com/ameen-mcmxc/lw4o6-automation/assets/45686881/cf608106-2438-49da-85ad-946c32ae7090)


– -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – – -– – – – -– – – – -– – – – -– – – – -– – -– –
– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – – – -– – -– – – – -– – – – -– – – – -– – – – -– – – – -– – -– –


All machines are CentOS-7 and built using VMware Workstation Player.


## IP configurations

IPv4 client: must be manually configured

LwB4: ens34 must be manually configured, the script will take care of the rest.

(Make sure that LwB4 has two interfaces: ens34 IPv4 capable interface &  ens35 IPv6 capable interface)

LwAFTR: The script will take care of everything. 

(Make sure that LwAFTR has two interfaces: ens34 IPv6 capable interface &  ens35 IPv4 capable interface)

IPv4 Server: must be manually configured. 


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

Make sure that you adjust interface names according to your topology.

Login to IPv4-client Machine.

``
cd /root/lw4o6-automation
``

``
ansible-playbook IPv4-client.yml
``

## Building lwB4 Router: -

Make sure that you adjust interface names according to your topology.

Login to lwB4 Machine.

``
cd /root/lw4o6-automation
``

``
ansible-playbook lwB4.yml
``

## Building IPv4 Server: -

Make sure that you adjust interface names according to your topology.

Login to IPv4-server Machine.

``
cd /root/lw4o6-automation
``

``
ansible-playbook IPv4-server.yml
``


## Building lwAFTR Router: -

Make sure that you adjust interface names according to your topology.

Login to lwAFTR Machine.

``
cd /root/lw4o6-automation
``

``
ansible-playbook lwAFTR.yml
``

## Running Snabb

For Snabb to work, run the commands below on lwAFTR: 

``
isolcpus=2,3
``

``
sudo src/snabb lwaftr run --name "test-lwaftr" --cpu 2-3 --conf lwaftr-start.conf &
``

To stopp Snabb: -

``
killall -9 snabb
``


Note: the IPv4 Server and lwB4 machines MUST be ON, so that ARP from lwAFTR towards IPv4 Server and lwB4 works.

