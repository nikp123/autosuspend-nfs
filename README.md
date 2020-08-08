# autosuspend-nfs

This Python package provides a NFS (Network File System)
check for [autosuspend](https://github.com/languitar/autosuspend).

## Quickstart

To suspend your server when there are no connections to the NFS server
add the following section to your `autosuspend.conf`:
```ini
[check.NFS]
class = autosuspend_nfs.ClientConnected
enabled = true
```

