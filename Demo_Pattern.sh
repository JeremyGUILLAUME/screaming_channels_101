: 'Collect initial raw trace:'
#python3 CODEs/extract_pattern/script_Collect_RawTrace.py -p Configs/config_pattern.txt

: 'Find the most precise Cryptographic Process (CP) length:'
#python3 CODEs/extract_pattern/script_Extract_Pattern_VT.py -p Configs/config_pattern.txt -s 1
#python3 CODEs/extract_pattern/script_Extract_Pattern_VT.py -p Configs/config_pattern.txt -s 2
#python3 CODEs/extract_pattern/script_Extract_Pattern_VT.py -p Configs/config_pattern.txt -s 2 --center 0 --span 5e-7 --res 1e-10
#python3 CODEs/extract_pattern/script_Extract_Pattern_VT.py -p Configs/config_pattern.txt -s 2 --center 0 --span 5e-9 --res 1e-12
#python3 CODEs/extract_pattern/script_Extract_Pattern_VT.py -p Configs/config_pattern.txt -s 3
#python3 CODEs/extract_pattern/script_Extract_Pattern_VT.py -p Configs/config_pattern.txt -s 4 --shift 1792
