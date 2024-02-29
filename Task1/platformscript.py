import platform

def get_user_agent_info():
    system_info = platform.uname()
    print(system_info)
    user_agent = f"System: {system_info.system} {system_info.release}\n" \
                 f"Machine: {system_info.machine}\n" \
                 f"Processor: {system_info.processor}"
    return user_agent


print("Welcome to 2022")
print("User Agent Information:")
print(get_user_agent_info())

