from functions.get_files_info import get_files_info

get_files_info("calculator", ".")
get_files_info("calculator", "pkg")
returned =get_files_info("calculator", "/bin")
print(returned)
ret = get_files_info("calculator", "../")
print(ret)