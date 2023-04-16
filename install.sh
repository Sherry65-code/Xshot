echo "Installing.."
sudo cp ./xshot /usr/bin/
cp ./app.py ~/
echo "$(pwd)" > loc.txtx
cp loc.txtx ~/
desktop-file-install --dir=$HOME/.local/share/applications $(pwd)/xshot.desktop
echo "Installed\nType xshot click a screenshot"
