# Install go-ipfs, ipfs-cluster-ctl and ipfs-cluster-service
  https://dist.ipfs.io/#go-ipfs
# Start BIOS
## Create configure file
```
python3 run.py ipfsinit
```
## Clean Bootstrap Array(~/.ipfs/config)

```
"Bootstrap": [
  ],
```
## Modify Gateway and API
```
"API": "/ip4/0.0.0.0/tcp/5001",
"Gateway": "/ip4/0.0.0.0/tcp/8080"

```
## Run IPFS

```
python3 run.py ipfsrun
```
## Create cluster configure file

```
python3 run.py  clusterinit

```
## Run ipfs-cluster-service

```
python3 run.py clustergenesisrun
```
You will see like "/ip4/127.0.0.1/tcp/9096/ipfs/QmW3HteXiyz7Hb4edNj76VAHH38jwsUAtJEBoTRvxmYyMJ". It will be used later.

# Add another node

## Create configure file

```
python3 run.py ipfsinit
```
## Modify the Bootstrap Array

```
"Bootstrap": [
    "/ip4/127.0.0.1/tcp/9096/ipfs/QmW3HteXiyz7Hb4edNj76VAHH38jwsUAtJEBoTRvxmYyMJ"
  ],
```

## Run IPFS
```
python3 run.py ipfsrun
```
## Create cluster configure file

```
python3 run.py  clusterinit

```
## Modify the config.ini

```
bootstrap = /ip4/192.168.1.184/tcp/9096/ipfs/QmW3HteXiyz7Hb4edNj76VAHH38jwsUAtJEBoTRvxmYyMJ
```
## Run ipfs-cluster-service


```
python3 run.py clusterrun
```
