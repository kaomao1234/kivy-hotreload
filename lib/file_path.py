import os
"""
kv_files กับ python_files = เก็บ path และ importmodule object สำหรับทำ reload
"""
kv_files = set()
python_files = set()

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.kv'):
            kv_files.add(os.path.join(root, file))
        elif file.endswith('.py') and file != "main.py":
            path = os.path.join(root,file)
            module_path = f'{path}'.replace(os.getcwd(),"").replace("\\",".").replace(".py","")[1:]
            python_files.add(__import__(module_path,fromlist=['']))
            # lib. เป็นการเพิ่ม import object อีกแบบนึงไม่จำเป็นต้องเป็น lib เสมอไป เพื่อป้องกันการ import error
            python_files.add(__import__(f"lib.{module_path}",fromlist=['']))

