echo "push file all"
scp all lh@192.168.0.180:/var/www/html/openthos/appstores
echo "push file game"
scp game lh@192.168.0.180:/var/www/html/openthos/appstores/data

echo "push all apk"
scp -r download lh@192.168.0.180:/var/www/html/openthos/appstores
echo "push all icon"
cp image icon -a
scp -r icon lh@192.168.0.180:/var/www/html/openthos/appstores
