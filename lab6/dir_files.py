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

#Task 4

def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file_path = '/Users/danialkozhakhmet/Library/Group Containers/UBF8T346G9.Office/SolutionPackages/f1d4d15c65a935ba2139bb5afaa623b0/PackageResources/fluidhost/static/js/13255.3bc6efaf.chunk.js.LICENSE.txt'
line_count = count_lines(file_path)
print(f"Количество строк в файле: {line_count}")

#Task 5 открываем и пишем туда 
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

data = ["Kendrick", "Kanye", "Steve Lacy"]

#Task 6

def generate_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for letter in range(ord('A'), ord('Z') + 1):
        file_name = f"{chr(letter)}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write(f"Это файл {file_name}")

directory = "рандом"
generate_files(directory)
print(f"Созданы 26 файлов в папке : {directory}")

#Task 7

def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source:
        with open(destination_path, 'w') as destination:
            destination.write(source.read())

source_path = "исходник"  
destination_path = "куда"  
copy_file(source_path, destination_path)
print(f"Содержимое файла {source_path} скопировано в {destination_path}")


#Task 8

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):  #доступ к файлу
            os.remove(file_path) #удаляем 
            print(f"Файл {file_path} удалён.")
        else:
            print(f"Нет доступа для удаления файла {file_path}.")
    else:
        print(f"Файл {file_path} не существует.")


delete_file(file_path)




    
    
    

    
    
    
    
