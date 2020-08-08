from setuptools import setup

setup(
    name="autosuspend-nfs",
    version="0.1",
    description="autosuspend checks for your NFS server",
    url="https://github.com/nikp123/autosuspend-nfs",
    author="nikp123",
    license="MIT",
    packages=["autosuspend_nfs"],
    install_requires=[
        "autosuspend",
    ],
    zip_safe=True
)
