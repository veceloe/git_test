import platform  
  
system = platform.system()  
release = platform.release()  
version = platform.version()  
machine = platform.machine()  
  
print(f"Операционная система: {system}")  
print(f"Версия операционной системы: {release}")  
print(f"Версия системы: {version}")  
print(f"Архитектура процессора: {machine}") 
