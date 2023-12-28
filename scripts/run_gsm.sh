DATASET='gsm_subset'
#DATASET='gsm'
MODEL='phi-2'
#MODEL='gpt-3.5-turbo-0613'

# cot
python src/solve.py --tag DEMO --range_start 0 --range_end end --dataset ${DATASET} --model ${MODEL} --mode cot
# eot
python src/solve.py --tag DEMO --range_start 0 --range_end end --dataset ${DATASET} --model ${MODEL} --mode eot
# check_eot
python src/solve.py --tag DEMO --range_start 0 --range_end end --dataset ${DATASET} --model ${MODEL} --mode check_eot --data_path outputs/gsm/eot/demo_eot_0_subset.jsonl
# pot
python src/solve.py --tag DEMO --range_start 0 --range_end end --dataset ${DATASET} --model ${MODEL} --mode pot
# check_pot
python src/solve.py --tag DEMO --range_start 0 --range_end end --dataset ${DATASET} --model ${MODEL} --mode check_pot --data_path outputs/gsm/pot/demo_pot_0_subset.jsonl
# plan
python src/solve.py --tag DEMO --range_start 0 --range_end end --dataset ${DATASET} --model ${MODEL} --mode plan

