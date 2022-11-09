echo VIBHAVASU - EP20BTECH11015
echo THIS IS THE EXECUTION BASH SCRIPT FOR CHARGER ASSIGNMENT

cd codes
echo Running python codes in
pwd

python3 e1.1.py
echo e1.1.py ran successfully
sleep 5

python3 e2.3.py
echo e2.3.py ran successfully
sleep 5

python3 e2.6.py
echo e2.6.py ran successfully
sleep 5

python3 e3.8.py
echo e3.8.py ran successfully
sleep 5

python3 e3.9.py
echo e3.9.py ran successfully
sleep 5

python3 e3.10.py
echo e3.10.py ran successfully
sleep 5

python3 e4.3.py
echo e4.3.py ran successfully
sleep 5

python3 e5.3.py
echo e5.3.py ran successfully
sleep 5

python3 e5.4.py
echo e5.4.py ran successfully
sleep 5

echo All python codes ran successfully

cd ..

echo Compiling tex file in
pwd

pdflatex main.tex
xdg-open main.pdf


echo THANK YOU
