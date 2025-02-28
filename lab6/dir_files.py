import os
path = os.getcwd()
current_file_path = os.path.abspath(__file__)

# print(os.getcwd())  Выведет текущую рабочую директорию

# print(os.listdir("."))   Список файлов и папок в текущей директории

#Task 1
def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    
    print("\nAll entries:")
    for entry in os.listdir(path):
        print(entry)

list_directories_files(path)

print("\n")

#Task 2
def check_path_access(path):
   
    if os.path.exists(path):
        print(f"Путь '{path}' существует.")
    else:
        print(f"Путь '{path}' не существует.")
        return  
    
   
    if os.access(path, os.R_OK):  
        print(f"Путь '{path}' доступен для чтения.")
    else:
        print(f"Путь '{path}' недоступен для чтения.")

   
    if os.access(path, os.W_OK):
        print(f"Путь '{path}' доступен для записи.")
    else:
        print(f"Путь '{path}' недоступен для записи.")

    
    if os.access(path, os.X_OK):
        print(f"Путь '{path}' доступен для выполнения.")
    else:
        print(f"Путь '{path}' недоступен для выполнения.")

check_path_access(path)

print("\n")

#Task 3
def check_file(path):
    
    if os.path.exists(path):
        print(f"Путь '{path}' существует")
    
        directory, filename = os.path.split(path)
        print(f"Директория: {directory}")
        print(f"Имя файла: {filename}")
    
    else:
        print(f"Путь '{path}' не существует.")

check_file(current_file_path)
    
    
    

    
    
    
    
