import os
import subprocess
import sys
import time
import glob

import parcel
from parcel.lib.exceptions import NPMNotInstalledException, NodeNotInstalledException


def check_node_installed():
    try:
        result = subprocess.run(['node', '-v'], stdout=subprocess.PIPE, universal_newlines=True)
        parcel.Parcel.node_version = result.stdout.strip()[1:]
    except subprocess.CalledProcessError:
        raise NodeNotInstalledException

def configure_parcel_project():
    subprocess.run(
        f'mkdir -p {parcel.Parcel.client_path} && cd {parcel.Parcel.client_path} && npm init -y',
        shell=True,
        stdout=subprocess.DEVNULL
    )
    subprocess.Popen(
        f'cd {parcel.Parcel.client_path} && npm i -D parcel',
        shell=True,
    ).wait()

def start_parcel_development_server():
    subprocess.Popen(
        f'cd {parcel.Parcel.client_path} && npx parcel watch',
        shell=True,
    )

def find_dist_files():
    dist_files = glob.glob(parcel.Parcel.client_path + 'dist/*') 
    print(dist_files)