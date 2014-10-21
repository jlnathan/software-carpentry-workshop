echo Cleaning up 
rm *.txt
rm *.tmp
rm *.csv

echo Download data
curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L

echo Unpack data
unzip rawdata.zip
rm rawdata.zip

rm *.tmp


for f in *.txt
do
	mv $f ${f/txt/csv}
done

echo Available .csv files
ls *.csv 

# ipython analyze_mosquito_data_script.py A2_mosquito_data.csv
for f in *data.csv
do
	ipython analyze_mosquito_data_script.py $f
done

mv *png figures/
mv *parameters.csv parameters/
