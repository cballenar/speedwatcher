# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.provision :shell, path: "Vagrant.bootstrap.sh"

  # Set hostname with Vagrant Hostsupdater
  config.vm.network "private_network", ip: "192.168.0.12"
  config.vm.hostname = "speedwatcher.dev"
end
