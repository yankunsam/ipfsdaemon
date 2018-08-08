from ipfs import Ipfs
import argparse
import json
import configparser
import os
from cluster import Cluster


def addArgument(parser,argList):
    parser.add_argument("command",help="start a bios node",choices=argList)
    parser.add_argument("--key",help="the key for ipfs config")
    parser.add_argument("--value",help="the value for key in ipfs config")


def args_switch(ipfsInstance,clusterInstance,args):
    switcher = {
    'ipfsinit': ipfsInstance.ipfsInit,
    'ipfsmanageconfig': ipfsInstance.ipfsManageConfig,
    'ipfsrun': ipfsInstance.ipfsDaemonRun,
    'ipfsstop': ipfsInstance.ipfsDaemonStop,
    'clusterinit': clusterInstance.clusterInit,
    'clusterrun': clusterInstance.clusterDaemonRun,
    'clustergenesisrun': clusterInstance.clusterGenesisRun,
    'clusterstop': clusterInstance.clusterDaemonStop,
    'getclusterid': clusterInstance.getClusterId
    }
    if(args.command != 'ipfsmanageconfig'):
        switcher.get(args.command,'nothing')()
    else:
        switcher.get(args.command,'nothing')(args.key,args.value)



def parseconfigfile():
    config = configparser.ConfigParser()
    dirname = os.path.dirname(__file__)
    configfile = os.path.join(dirname, './config.ini')
    config.read(configfile)
    return config


def main():
    parser = argparse.ArgumentParser()
    addArgument(parser,['ipfsinit','ipfsmanageconfig','ipfsrun','ipfsstop','clusterinit','clusterrun','clustergenesisrun','clusterstop','getclusterid'])
    config = parseconfigfile()
    args = parser.parse_args()
    ipfsInstance = Ipfs(config['Init']['bootstrap'],config['Init']['storagemax'],config['Init']['datadir'],config['Init']['clustersecret'])
    clusterInstance = Cluster(config['Init']['bootstrap'],config['Init']['datadir'],config['Init']['clustersecret'])
    args_switch(ipfsInstance,clusterInstance,args)


if __name__ == "__main__":
    main()
