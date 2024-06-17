import os
import pm4py
import time
import sys

if __name__ == "__main__":

    # 构建XES
    log_BPIC13cp = pm4py.read_xes('BPIC13cp.xes')
    log_BPI_Challenge_2012 = pm4py.read_xes('BPI_Challenge_2012.xes')
    BPIC15_1f = pm4py.read_xes('BPIC15_1f.xes')
    BPIC15_2f = pm4py.read_xes('BPIC15_2f.xes')
    BPIC15_3f = pm4py.read_xes('BPIC15_3f.xes')
    BPIC15_4f = pm4py.read_xes('BPIC15_4f.xes')
    BPIC15_5f = pm4py.read_xes('BPIC15_5f.xes')
    SEPSIS = pm4py.read_xes('SEPSIS.xes')


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "alpha":
            start = time.perf_counter()
            # Alpha Miner
            net, im, fm = pm4py.discover_petri_net_alpha(log_BPIC13cp, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第一个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(log_BPI_Challenge_2012, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第二个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_1f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第三个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_2f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第四个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_3f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第五个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_4f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第六个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(BPIC15_5f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第七个运行完")
            net, im, fm = pm4py.discover_petri_net_alpha(SEPSIS, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第八个运行完")

            end = time.perf_counter()
            print("Alpha Miner耗时: " + str(end - start) + "秒")

        elif param == "inductive":
            # inductive Miner
            start = time.perf_counter()
            net, im, fm = pm4py.discover_petri_net_inductive(log_BPIC13cp, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第一个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(log_BPI_Challenge_2012, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第二个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_1f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第三个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_2f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第四个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_3f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第五个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_4f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第六个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_5f, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第七个运行完")
            net, im, fm = pm4py.discover_petri_net_inductive(SEPSIS, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            print("第八个运行完")
            end = time.perf_counter()
            print("inductive Miner耗时: " + str(end - start) + "秒")

        elif param == "heuristics":
            start = time.perf_counter()
            # Heuristics Miner
            net, im, fm = pm4py.discover_petri_net_heuristics(log_BPIC13cp, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第一个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(log_BPI_Challenge_2012, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第二个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_1f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第三个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_2f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第四个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_3f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第五个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_4f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第六个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(BPIC15_5f, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第七个运行完")
            net, im, fm = pm4py.discover_petri_net_heuristics(SEPSIS, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            print("第八个运行完")
            end = time.perf_counter()
            print("Heuristics Miner耗时: " + str(end - start) + "秒")

        elif param == "ilp":
            start = time.perf_counter()
            # ILP Miner
            net, im, fm = pm4py.discover_petri_net_ilp(log_BPIC13cp, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            print("第一个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(log_BPI_Challenge_2012, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            print("第二个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_1f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第三个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_2f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第四个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_3f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第五个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_4f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第六个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(BPIC15_5f, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第七个运行完")
            net, im, fm = pm4py.discover_petri_net_ilp(SEPSIS, activity_key='concept:name',
                                                              case_id_key='case:concept:name',
                                                              timestamp_key='time:timestamp')
            print("第八个运行完")

            end = time.perf_counter()
            print("ILP Miner耗时: " + str(end - start) + "秒")

    else:
        print("没有提供任何命令行参数")
