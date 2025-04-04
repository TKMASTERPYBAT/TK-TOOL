clear
echo "\033[31mMake Sure To Run As Root, Or It Wont Work!"
echo "\033[32mSetting Things Up...\n"
pip install -r requirements.txt
sudo cp tk-tool.py /usr/local/bin/tk-tool 
sudo chmod +x /usr/local/bin/tk-tool 
clear
echo "\033[31m+=====================================================+"
echo "\033[31m|\033[32mAll set. Now just type 'tk-tool' in the command line.\033[31m|"
echo "\033[31m+=====================================================+"
