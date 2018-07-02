import os
import subprocess
import sys
import time

import parcel
from parcel.lib.exceptions import NPMNotInstalledException, NodeNotInstalledException


def check_node_installed():
    try:
        result = subprocess.run(['node', '-v'], stdout=subprocess.PIPE, universal_newlines=True)
        parcel.Parcel.node_version = result.stdout.strip()[1:]
    except subprocess.CalledProcessError:
        raise NodeNotInstalledException

def test_npm():
    result = subprocess.run(
        f'mkdir -p {parcel.Parcel.client_path} && cd {parcel.Parcel.client_path} && npm init -y',
        shell=True,
        stdout=subprocess.DEVNULL
    )