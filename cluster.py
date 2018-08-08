import daemon
import subprocess
import os
import json


class Cluster(object):
    initCmdList = ['ipfs-cluster-service','init']
    runCmdList = ['ipfs-cluster-service','daemon','--bootstrap']
    genesisRunCmdList = ['ipfs-cluster-service','daemon']
    stopCmdList = ['killall','ipfs-cluster-service']
    """docstring for IpfsClusterService."""
    def __init__(self, bootstrap,datadir,clustersecret):
        super(Cluster, self).__init__()
        self.bootstrap = bootstrap
        self.datadir = datadir
        self.clustersecret = clustersecret

    def clusterInit(self):
        os.environ['CLUSTER_SECRET'] = self.clustersecret
        subprocess.run(self.initCmdList)

    def clusterDaemonRun(self):
        log = open(("%s/%s" % (self.datadir,"cluster.log")),'w+')
        with daemon.DaemonContext(stdout=log,stderr=log):
            subprocess.Popen(self.runCmdList + [self.bootstrap])

    def clusterGenesisRun(self):
        log = open(("%s/%s" % (self.datadir,"cluster.log")),'w+')
        with daemon.DaemonContext(stdout=log,stderr=log):
            subprocess.Popen(self.genesisRunCmdList)

    def clusterDaemonStop(self):
        subprocess.run(self.stopCmdList)

    def getClusterId(self):
        with open('/Users/sam/.ipfs-cluster/service.json') as service:
            data = json.load(service)
            print(data['cluster']['id'])
            return (data['cluster']['id'])
