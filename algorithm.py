import gzip
import shutil
import os
import pm4py
import time
import sys

if __name__ == "__main__":

    BPIC12_output_file = '/app/data/BPIC12.xes'
    BPIC13_cp_output_file = '/app/data/BPIC13_cp.xes'
    BPIC13_i_output_file = '/app/data/BPIC13_i.xes'
    BPIC14_f_output_file = '/app/data/BPIC14_f.xes'
    BPIC15_1f_output_file = '/app/data/BPIC15_1f.xes'
    BPIC15_2f_output_file = '/app/data/BPIC15_2f.xes'
    BPIC15_3f_output_file = '/app/data/BPIC15_3f.xes'
    BPIC15_4f_output_file = '/app/data/BPIC15_4f.xes'
    BPIC15_5f_output_file = '/app/data/BPIC15_5f.xes'
    BPIC17_f_output_file = '/app/data/BPIC17_f.xes'
    RTFMP_output_file = '/app/data/RTFMP.xes'
    SEPSIS_output_file = '/app/data/SEPSIS.xes'
    # 加载解压后的 .xes 文件
    BPIC12 = pm4py.read_xes(BPIC12_output_file)
    BPIC13_cp = pm4py.read_xes(BPIC13_cp_output_file)
    BPIC13_i = pm4py.read_xes(BPIC13_i_output_file)
    BPIC14_f = pm4py.read_xes(BPIC14_f_output_file)
    BPIC15_1f = pm4py.read_xes(BPIC15_1f_output_file)
    BPIC15_2f = pm4py.read_xes(BPIC15_2f_output_file)
    BPIC15_3f = pm4py.read_xes(BPIC15_3f_output_file)
    BPIC15_4f = pm4py.read_xes(BPIC15_4f_output_file)
    BPIC15_5f = pm4py.read_xes(BPIC15_5f_output_file)
    BPIC17_f = pm4py.read_xes(BPIC17_f_output_file)
    RTFMP = pm4py.read_xes(RTFMP_output_file)
    SEPSIS = pm4py.read_xes(SEPSIS_output_file)

    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "alpha":
            start = time.perf_counter()
            # Alpha Miner
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC12, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC13_cp, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC13_i, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC14_f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_1f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_2f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_3f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_4f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_5f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC17_f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(RTFMP, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_alpha(SEPSIS, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            

            end = time.perf_counter()
            print("Alpha Miner耗时: " + str(end - start) + "秒")
        elif param == "alphaPlus":
            # inductive Miner
            start = time.perf_counter()
            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC12, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC13_cp, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_pluse(BPIC14_f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC15_1f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC15_2f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC15_3f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC15_4f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(BPIC15_5f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_pluse(BPIC17_f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_net_alpha_plus(RTFMP, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            net, im, fm = pm4py.discover_petri_alpha_plus(SEPSIS, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')

            end = time.perf_counter()
            print("alpha plus Miner耗时: " + str(end - start) + "秒")
        elif param == "inductive":
            # inductive Miner
            start = time.perf_counter()
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC12, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC13_cp, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC14_f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_1f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_2f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_3f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_4f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_5f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC17_f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(RTFMP, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_inductive(SEPSIS, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            

            end = time.perf_counter()
            print("inductive Miner耗时: " + str(end - start) + "秒")

        elif param == "heuristics":
            start = time.perf_counter()
            # Heuristics Miner
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC12, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC13_cp, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC14_f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_1f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_2f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_3f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_4f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_5f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC17_f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(RTFMP, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_heuristics(SEPSIS, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            
            end = time.perf_counter()
            print("Heuristics Miner耗时: " + str(end - start) + "秒")

        elif param == "ilp":
            start = time.perf_counter()
            # ILP Miner
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC12, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC13_cp, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC13_i, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC14_f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_1f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_2f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_3f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_4f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_5f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC17_f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(RTFMP, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            
            net, im, fm = pm4py.discover_petri_net_ilp(SEPSIS, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')     

            end = time.perf_counter()
            print("ILP Miner耗时: " + str(end - start) + "秒")

    else:
        print("没有提供任何命令行参数")
