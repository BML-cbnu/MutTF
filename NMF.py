import os
import argparse
from SigProfilerExtractor import sigpro as sig

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='sigprofiler_extractor')

# 입력받을 인자값 등록
parser.add_argument('--ref_genome', required=True, help='select reference genome(e.g. GRCh37)')
parser.add_argument('--min', required=True, help='enter minimum_signatures')
parser.add_argument('--max', required=True, help='enter maximum_signatures')
parser.add_argumnet('--input_dir', required=True, help = 'input directory')
parser.add_argumnet('--output_dir', required=True, help = 'output directory')

# 입력받은 인자값을 args에 저장 (type: namespace)
args = parser.parse_args()















def main():    
    # to get input from table format (mutation catalog matrix)
    path_to_example_table = sig.importdata("matrix")
    data = path_to_example_table # you can put the path to your tab delimited file containing the mutational catalog matrix/table
    sig.sigProfilerExtractor("matrix", args.output_dir,
                         f"{args.input_dir}/output/SBS/DATA.SBS96.all", reference_genome=str(args.ref_genome),
                             minimum_signatures=int(args.min), maximum_signatures=int(args.max), nmf_replicates=100, cpu=-1)
    
#sig_extract()
if __name__ == '__main__':
    main()
