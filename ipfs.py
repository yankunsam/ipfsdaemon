import daemon
import subprocess


class Ipfs:
    initCmdList = ['ipfs','init']
    runCmdList = ['ipfs','daemon']
    ManageConfigCmdList = ['ipfs','config','--json']
    def __init__(self,bootstrap,storagemax,datadir):
        self.bootstrap = bootstrap
        self.storagemax = storagemax
        self.datadir = datadir

    def ipfsInit(self):
        print('In ipfsInit')
        subprocess.run(self.initCmdList)

    def ipfsManageConfig(self,key,configValue):
        subprocess.run(self.ManageConfigCmdList + [key,configValue])

    def ipfsDaemonRun(self):
        log = open(("%s/%s" % (self.datadir,"ipfs.log")),'w+')
        with daemon.DaemonContext(stdout=log,stderr=log):
            subprocess.Popen(self.runCmdList)
