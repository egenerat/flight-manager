cat ../gpg_key | gpg --passphrase-fd 0 archive.tar.gpg
tar xvf archive.tar
rm archive.tar
