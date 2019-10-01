#!/bin/bash

echo "Launching Bot."
# open virtual environment
echo "Starting Virtual Environment..."
source activate bot_env
# start flask server
echo "Launching Bot Server..."
python3 bot.py &
# save pid
echo $! >> ~/.trash_config
# print verify token
echo "Please Copy Verification Token for Callback:"
echo "#########################################"
echo $FACEBOOK_VERIFY_TOKEN
echo "#########################################"
echo "Use this code to establish a callback for your product in the Facebook Developer Portal."
echo
echo "You will also need the URL established by the ngrok http tunnel. This url will appear in 10 seconds..."
sleep 10
# open facebook dev website for verification
echo "Opening facebook Dev Portal to Verify Callback..."
open "https://developers.facebook.com/apps/423834951818436/messenger/settings/"
# start ngrock tunnel
echo "Creating http Tunnel..."
./ngrok http 5000

# wait for enter to clean up
read -p "Press enter to continue"
echo "Cleaning Up..."
kill -9 "$(cat ~/.trash_config)"
rm ~/.trash_config
source deactivate
echo "Done."
