if [ $(which apt-get) ]; then
    echo "checking for python"
    sudo apt-get -y install python3
fi

echo "running tests"
python3 test_main.py

echo "symlinking"
sudo ln -sf $(pwd)/where /usr/local/bin/where

echo "Where install successful"