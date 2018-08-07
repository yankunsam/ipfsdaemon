from ipfs import Ipfs
import argparse
import json
import configparser
import os


def addArgument(parser,argList):
    parser.add_argument("command",help="start a bios node",choices=argList)
    parser.add_argument("--key",help="the key for ipfs config")
    parser.add_argument("--value",help="the value for key in ipfs config")


def args_switch(ipfsInstance,args):
    switcher = {
    'init': ipfsInstance.ipfsInit,
    'manageconfig': ipfsInstance.ipfsManageConfig,
    'run': ipfsInstance.ipfsDaemonRun
    }
    if(args.command != 'manageconfig'):
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
    addArgument(parser,['init','manageconfig','run'])
    config = parseconfigfile()
    args = parser.parse_args()
    ipfsInstance = Ipfs(config['Init']['bootstrap'],config['Init']['storagemax'],config['Init']['datadir'])
    args_switch(ipfsInstance,args)


if __name__ == "__main__":
    main()
