# Build some file's for Developer </>

cat > .gitignore << ENDOFFILE
#--GITIGNORE--
.gitignore
*.bash
ENDOFFILE


cat > README.md << ENDOFFILE
# Project Name

---
## Software Requirements
- Name of Software: Software v3.7.*


---
## OutPut of File: FileName.html
	- Some description..
<kbd><img src="/imgs-readme/img-black-blank_v1-1.jpg" alt="img_alternative_txt_v1-1" title="hover_title.."></img></kbd>
ENDOFFILE

mkdir imgs-readme
mx=1280;my=720;head -c "$((3*mx*my))" /dev/urandom | convert -depth 8 -size "${mx}x${my}" RGB:- imgs-readme/img-black-blank_v1-1.jpg


cat > CHANGELOG.md << ENDOFFILE
# ChangeLog
## Release Notes

---
## v1.1 (190505)
### Added
	- Add new feature.
ENDOFFILE
# Author: Ashish Sondagar (Software Engineer)


cat > Notes3.md << ENDOFFILE
# Note

- Some points

---
# Note for Developer

- Road map of project.. or
- Some milestone..
ENDOFFILE


cat > NoteCommands.md << ENDOFFILE
# Commands
	
---
- description..
- => pwd
ENDOFFILE


cat > NoteMySQLquery.sql << ENDOFFILE
DESCRIBE table_name;
SHOW CREATE TABLE table_name;
SHOW TABLES LIKE '%key_word%';
SHOW INDEX FROM table_name;
SELECT * FROM table_name;


SELECT * FROM table_name ORDER BY 1 DESC;
SELECT * FROM table_name ORDER BY 1 DESC;
SELECT * FROM table_name ORDER BY 1 DESC;
ENDOFFILE


cat > gitPushW.bash << ENDOFFILE
echo "pingpong"

git status

git add .
#git add -A
#git add -f .

echo Write your commit:
read cmmt
echo You commit: \$cmmt
git commit -m "\$cmmt </> \$(date +"%a, %Y-%m-%d, %H:%M:%S %Z %j")"

git pull origin home
git push origin home
#git push -f origin home

git status

\$SHELL
ENDOFFILE


sudo chmod -R 0777 *
