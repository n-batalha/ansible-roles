set -e

for role in $(ls roles/)
do
    (cd roles/$role; molecule test) || exit
done
