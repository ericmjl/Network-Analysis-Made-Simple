mkdir -p nams
tar -xzf nams.tar.gz -C nams
source nams/bin/activate
conda-unpack
source nams/bin/deactivate
# A check -- just to make sure nams is installed
conda env list | grep nams
