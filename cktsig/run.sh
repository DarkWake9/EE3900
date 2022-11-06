echo VIBHAVASU - EP20BTECH11015
echo THIS IS THE EXECUTION BASH SCRIPT FOR CKTSIG ASSIGNMENT

cd codes
echo Running python codes in
pwd

python3 e2.6.py
echo e2.6.py ran successfully
sleep 10

python3 e3.4.py
echo e3.4.py ran successfully
sleep 10

python3 e4.3.py
echo e4.3.py ran successfully
sleep 10

python3 e4.7.py
echo e4.7.py ran successfully
sleep 10

echo All python codes ran successfully

cd ..

echo Compiling tex file in
pwd

pdflatex main.tex
xdg-open main.pdf
echo THANK YOU
