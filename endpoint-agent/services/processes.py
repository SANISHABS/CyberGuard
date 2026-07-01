import psutil


def get_running_processes():
    processes = []

    try:
        for process in psutil.process_iter(
                ['pid', 'name', 'cpu_percent', 'memory_info']):

            try:
                process_info = process.info

                processes.append({
                    "pid": process_info['pid'],
                    "name": process_info['name'],
                    "cpu": round(process_info['cpu_percent'], 2),
                    "memory": round(
                        process_info['memory_info'].rss / (1024 * 1024), 2
                    )  # Convert bytes to MB
                })

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):

                continue

        return {
            "total_processes": len(processes),
            "processes": processes
        }

    except Exception as e:

        return {
            "total_processes": 0,
            "processes": [],
            "error": str(e)
        }