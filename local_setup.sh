cat ../AS/gpg_key | gpg --passphrase-fd 0 archive.tar.gpg
tar xvf archive.tar