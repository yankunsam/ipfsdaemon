import daemon
import subprocess
import os


class Ipfs:
    initCmdList = ['ipfs','init']
    runCmdList = ['ipfs','daemon']
    ManageConfigCmdList = ['ipfs','config','--json']
    stopCmdList = ['killall','ipfs']
    def __init__(self,bootstrap,storagemax,datadir,clustersecret):
        self.bootstrap = bootstrap
        self.storagemax = storagemax
        self.datadir = datadir
        self.clustersecret = clustersecret

    def ipfsInit(self):
        print('In ipfsInit')
        os.environ['CLUSTER_SECRET'] = self.clustersecret
        print(os.environ['CLUSTER_SECRET'])
        subprocess.run(self.initCmdList)

    def ipfsManageConfig(self,key,configValue):
        subprocess.run(self.ManageConfigCmdList + [key,configValue])

    def ipfsDaemonRun(self):
        log = open(("%s/%s" % (self.datadir,"ipfs.log")),'w+')
        with daemon.DaemonContext(stdout=log,stderr=log):
            subprocess.Popen(self.runCmdList)

    def ipfsDaemonStop(self):
        subprocess.run(self.stopCmdList)
