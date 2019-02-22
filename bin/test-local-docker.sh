set -e

for ROLE in $(ls roles/)
do
    pipenv run bash -c "(cd roles/${ROLE}; molecule test)" || exit
done
