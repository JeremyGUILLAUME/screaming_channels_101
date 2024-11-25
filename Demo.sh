: 'Show traces:'
python3 CODEs/script_Collect.py -p Configs/config_demo.txt --dataset_name profile --nb_traces 1 --time_div 10 --plot 1
#python3 CODEs/script_Collect.py -p Configs/config_demo.txt --dataset_name profile --nb_traces 1 --time_div 500 --plot 1


: 'Collect traces:'
#python3 CODEs/script_Collect.py -p Configs/config_demo.txt --dataset_name profile --data_input S --nb_traces 15000 --time_div 10 --plot 0
#python3 CODEs/script_Collect.py -p Configs/config_demo.txt


: 'Analysis attack: build profile and realize the attack'
#python3 CODEs/script_Analysis.py -p Configs/config_demo.txt --dataset_name profile --profile 1 --nb_traces 15000 --time_div 10 --plot 1
#python3 CODEs/script_Analysis.py -p Configs/config_demo.txt --plot_pges 1
: 'Analysis attack: Bruteforce the key'
#python3 CODEs/script_Analysis.py -p Configs/config_demo.txt --plot_pges 1 --bruteforce 24
#python3 CODEs/script_Analysis.py -p Configs/config_demo.txt --plot_pges 1 --bruteforce 32


: 'Plot attack results:'
#python3 CODEs/script_Fig.py -p Configs/config_demo.txt


