
import os
import ezdxf

for foot,dirs,checkdxffiles in os.walk('.\\DXF\\'):
    pass
dxflist=list(filter(lambda checkdxffiles:checkdxffiles.lower().find('.dxf') !=-1,checkdxffiles))
   
#if len(tklist) !=1 :  
if not os.path.exists("tk.dxf"):  
    print(r"下缺少图框文件或者有多个图框文件,需要把图框复制到tk文件夹下")
elif len(dxflist) ==0:
    print(r".\dxf 下缺少dxf文件,需要把dxf复制到DXF文件夹下")
else:
    for foot,dirs,checkdxffiles in os.walk('.\\DXF\\'):
    	pass
    tkdxffiles=list(filter(lambda checkdxffiles:checkdxffiles.lower().find('.dxf') !=-1,checkdxffiles))    
    for file in tkdxffiles:
         target_drawing = ezdxf.readfile('.\\tk\\tk.dxf')
         source_drawing = ezdxf.readfile('.\\dxf\\'+file)
         print('正在处理文件：' + file )
         modelspace = target_drawing.modelspace()
         for e in modelspace:
            if e.dxftype() == 'TEXT':
                text = e.dxf.text
                a,p1,p2=e.get_pos()
         importer = ezdxf.Importer(source_drawing, target_drawing)
         importer.import_all()
         target_drawing.saveas('.\\dwg\\'+file)

print("处理完毕！")

