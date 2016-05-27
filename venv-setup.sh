set -x
VENV="$(which virtualenv)"
if [ -z "$VENV" ]; then
   pip install virtualenv
fi
if [[ -d 'network' ]]; then
   rm -rf ./network
   echo 'xx';
fi
virtualenv network
source network/bin/activate && pip install -r requirements.txt
echo "Run 'source network/bin/activate' to begin"

python checkenv.py