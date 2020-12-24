mkdir -p nams_env
tar -xzf nams.tar.gz -C nams_env
source nams_env/bin/activate
conda-unpack
source nams_env/bin/deactivate
