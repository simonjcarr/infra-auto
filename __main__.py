
from app import CreateVMApp, CreateVMAppArgs
from pulumi import automation as auto
from dotenv import load_dotenv
load_dotenv()
def createVM():
  newvm = CreateVMApp("newvm", CreateVMAppArgs(
    name="newvm",
    cpu=2,
    ram=4,
    disk=40
  ))
  return newvm

stack = auto.create_or_select_stack(
  stack_name="dev",
  project_name="infra-api",
  program=createVM
)

stack.workspace.install_plugin("hcloud", "1.16.1")

up_res = stack.destroy(on_output=print)

print("****IPV4: " + up_res.outputs["ipv4"].value)

