# until mazer supports local sources

cd ..
tar cvf /tmp/ansible-roles.tar ansible-roles
mazer install --namespace n-batalha /tmp/ansible-roles.tar
mv ~/.ansible/content/n-batalha/tmp/ansible-roles.tar ~/.ansible/content/n-batalha/ansible-roles
