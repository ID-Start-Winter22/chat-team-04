# COPY WEB-STUFF TO APACHE2 DEFAULT DIR
IP=$1
if [ -z "$IP" ]
then 
  echo "IP param is unset! Aborting..."
  exit
else 
  echo "IP is set to '$1'"
fi

DIR=static
if [ -d "$DIR" ];
then # updated frontend is in use
    echo "$DIR directory exists. Replace localhost with $IP in constants.js..."
    sed -i -e "s/localhost/$IP/g" static/js/constants.js    
    sed -i -r 's/(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b'/"$IP"/ static/js/constants.js # if the IP is not aliased, or has already been changed.
    sudo cp -r $DIR /var/www/html
else # default frontend is in use
    echo "$DIR directory does not exist. Replace localhost with $IP in index.html..."
    sed -i -e "s/localhost/$IP/g" index.html
    sed -i -r 's/(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b'/"$IP"/ index.html # if the IP is not aliased, or has already been changed.
fi
sudo cp index.html /var/www/html
sudo systemctl restart apache2
