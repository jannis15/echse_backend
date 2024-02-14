import base64
import psutil
import wmi
from typing import List
import icoextract
from collections import namedtuple
from abc import ABC

from lib.schemas import ProcessSchema

PDetails = namedtuple("PDetails", ["name", "exe"])


class ProcessesApiClient(ABC):
    @staticmethod
    def get_running_processes() -> List[ProcessSchema]:
        wmi_obj = wmi.WMI()
        p_details_list = []
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
                if (
                        p.name().endswith(".exe") and
                        p.status() == "running" and
                        p.exe() and
                        not p.exe().lower().startswith("c:\\windows") and
                        not p.exe().lower().startswith("c:\\program files\\amd")
                ):
                    processes = wmi_obj.Win32_Process(ProcessId=p.pid)
                    if processes and processes[0].SessionId != 0:
                        p_details_list.append(
                            PDetails(ProcessesApiClient.__capitalize_first_letter(p.name()[:-4]), p.exe()))
            except Exception as e:
                print(e)
        p_details_list = ProcessesApiClient.__filter_processes_by_blacklist(p_details_list)
        p_details_list = sorted(p_details_list, key=lambda x: x.name)
        p_details_list = ProcessesApiClient.__filter_similar_process_names(p_details_list)
        result = []
        for p_detail in p_details_list:
            base64str = ''
            try:
                ie = icoextract.IconExtractor(p_detail.exe)
                base64str = base64.b64encode(ie.get_icon().getvalue())
            except:
                pass
            result.append(ProcessSchema(name=p_detail.name, icon=base64str, duration=1))
        return result

    @staticmethod
    def __capitalize_first_letter(process_name: str):
        return process_name[0].upper() + process_name[1:]

    @staticmethod
    def __filter_processes_by_blacklist(processes: List[PDetails]) -> List[PDetails]:
        keywords_to_exclude = ["python", "powertoys", "pwsh", "code", "cpumetricsserver", "lghub"]
        return [process for process in processes if
                not any(keyword in process.name.lower() for keyword in keywords_to_exclude)]

    @staticmethod
    def __filter_similar_process_names(processes: List[PDetails]) -> List[PDetails]:
        filtered_names = []
        existing_starts = set()
        for process in processes:
            if len(process.name) >= 4:
                start_chars = process.name[:4].lower()
                if start_chars not in existing_starts:
                    filtered_names.append(process)
                    existing_starts.add(start_chars)
            else:
                if not any(existing.startswith(process.name.lower()) for existing in existing_starts):
                    filtered_names.append(process)
                    existing_starts.add(process.name.lower())
        return filtered_names
