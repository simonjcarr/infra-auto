"""A Python Pulumi program"""

import pulumi
import pulumi_hcloud as hcloud

class CreateVMAppArgs:
  def __init__(
      self,
      name: pulumi.Input[str],
      cpu: pulumi.Input[int],
      ram: pulumi.Input[int],
      disk: pulumi.Input[int]
      ):
    self.name = name
    self.cpu = cpu
    self.ram = ram
    self.disk = disk

class CreateVMApp(pulumi.ComponentResource):
  def __init__(
      self, name: str, args: CreateVMAppArgs, opts: pulumi.ResourceOptions = None
  ):
    super().__init__("createvmapp:index:CreateVMApp", name, {}, opts)

    vm = hcloud.Server(name,
      opts=pulumi.ResourceOptions(parent=self),
      name=name,
      server_type="cax11",
      image="ubuntu-22.04",
      location="nbg1",
    )

    pulumi.export("vm_id", vm.id)
    pulumi.export("ipv4", vm.ipv4_address)
    pulumi.export("vm_name", vm.name)
    pulumi.export("backups_enabled", vm.backups)
    pulumi.export("iso", vm.iso)