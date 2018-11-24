for role in direnv git pipenv stack i3
do
    (cd roles/$role; molecule test)
done
