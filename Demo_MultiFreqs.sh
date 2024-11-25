: 'Collect traces:'
#python3 CODEs/multi_freqs/script_Collect.py -p Configs/config_demo_multiFreqs.txt --dataset_name profile --data_input S --nb_traces 15000 --time_div 10 --plot 0
#python3 CODEs/multi_freqs/script_Collect.py -p Configs/config_demo_multiFreqs.txt


: 'Analysis attack: build profile and realize the attack'
#python3 CODEs/multi_freqs/script_Analysis.py -p Configs/config_demo_multiFreqs.txt --dataset_name profile --profile 1 --nb_traces 15000 --time_div 10
#python3 CODEs/multi_freqs/script_Analysis.py -p Configs/config_demo_multiFreqs.txt --plot_pges 1
#python3 CODEs/multi_freqs/script_Analysis.py -p Configs/config_demo_multiFreqs.txt --plot_pges 1 --bruteforce 32


: 'Plot attack results:'
#python3 CODEs/multi_freqs/script_Fig.py -p Configs/config_demo_multiFreqs.txt






